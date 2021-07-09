import traceback

from maggie_backend.constants.error_constants import *
from maggie_backend.service.base_service import BaseService
from django.db import connection

from maggie_backend.sql_uitilities.sqls import *
from maggie_backend.sql_uitilities.sql_util import *


class InstockManagement(BaseService):
    def __init__(self, request):
        super(InstockManagement, self).__init__(request)
        if request.method == 'POST':
            self.data = eval(request.body)
            print(self.data)
            logger.info(self.data)
        elif request.method == 'GET':
            self.data = request.GET

    def get_newest_inorder_id(self):
        try:
            cursor = connection.cursor()
            cursor.execute(GET_INORDER_ID_SQL)
            print(GET_INORDER_ID_SQL)
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

    def get_instock(self):
        try:
            cursor = connection.cursor()
            cursor.execute(GET_INSTOCK_ORDER_SQL)
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



    def add_instock(self):
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
            cursor.execute(CREATE_INORDER_SQL,
                           (order_id,))
            total_cost = 0
            for item in items:
                cursor.execute(ADD_ITEM_AMOUNTS_SQL, (order_id, item['id'], item['amount']))
                cursor.execute(ADD_ITEM_STOCK_AMOUNT_SQL, (item['amount'], item['id']))
                cursor.execute(GET_ITEM_PRICE_BY_ID_SQL, (item['id'],))
                price_dict = dictfetchone(cursor)
                item_purchasing_price = price_dict['purchasing_price']
                total_cost += int(item_purchasing_price) * int(item['amount'])
            cursor.execute(ADD_COST_TO_INORDER_SQL, (total_cost, order_id))
            connection.commit()
            self._init_response()
            return self._get_response(HANDLE_OK, 1)

        except Exception as error:
            traceback.print_exc()
            connection.rollback()
            self._init_response()
            return self._get_response(SERVER_ERROR, -1)
