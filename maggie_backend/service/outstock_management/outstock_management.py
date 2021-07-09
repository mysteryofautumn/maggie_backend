import traceback

from maggie_backend.constants.error_constants import *
from maggie_backend.service.base_service import BaseService
from django.db import connection

from maggie_backend.sql_uitilities.sqls import *
from maggie_backend.sql_uitilities.sql_util import *


class OutstockManagement(BaseService):
    def __init__(self, request):
        super(OutstockManagement, self).__init__(request)
        if request.method == 'POST':
            self.data = eval(request.body)
            print(self.data)
            logger.info(self.data)
        elif request.method == 'GET':
            self.data = request.GET

    def get_newest_outorder_id(self):
        try:
            cursor = connection.cursor()
            cursor.execute(GET_OUTORDER_ID_SQL)
            print(GET_OUTORDER_ID_SQL)
            num_dict = dictfetchone(cursor)
            print(num_dict)
            num = num_dict['nums']
            print(num)
            res = {
                'order_id': num+1
            }
            self._init_response()
            self.response.update(res)
            return self._get_response(HANDLE_OK, 1)

        except Exception as error:
            self._init_response()
            return self._get_response(SERVER_ERROR, -1)

    def get_outstock(self):
        try:
            cursor = connection.cursor()
            cursor.execute(GET_OUTORDER_ID_SQL)
            rows = dictfetchall(cursor)
            res = {
                'orders': rows
            }
            self._init_response()
            self.response.update(res)
            return self._get_response(HANDLE_OK, 1)

        except Exception as error:
            self._init_response()
            return self._get_response(SERVER_ERROR, -1)



    def add_outstock(self):
        try:
            order_id = self.data['order_id']
            items = self.data['items']
            if len(items) == 0 or not order_id:
                return self._get_response(INVALID_BLANK, -1)

        except Exception as error:
            traceback.print_exc()
            self._init_response()
            return self._get_response(POST_ARG_ERROR, -1)

        try:
            # 1. create order
            # 2. create item amounts
            # 3. only need to add the item's stock amount
            # 4. calculate the instock cost and insert the value


            cursor = connection.cursor()
            cursor.execute(CREATE_OUTORDER_SQL,
                           (order_id,))
            total_cost = 0
            for item in items:
                cursor.execute(ADD_ITEM_AMOUNTS_SQL, (order_id, item['id'], item['amount']))
                cursor.execute(ADD_ITEM_SHELF_AMOUNT_SQL, (item['amount'], item['id']))
                cursor.execute(MINUS_ITEM_STOCK_AMOUNT_SQL, (item['amount'], item['id']))
            connection.commit()
            self._init_response()
            return self._get_response(HANDLE_OK, 1)

        except Exception as error:
            traceback.print_exc()
            connection.rollback()
            self._init_response()
            return self._get_response(SERVER_ERROR, -1)
