import traceback

from maggie_backend.constants.error_constants import *
from maggie_backend.service.base_service import BaseService
from django.db import connection

from maggie_backend.sql_uitilities.sqls import *
from maggie_backend.sql_uitilities.sql_util import *


class RevenueManagement(BaseService):
    def __init__(self, request):
        super(RevenueManagement, self).__init__(request)
        if request.method == 'POST':
            self.data = eval(request.body)
            print(self.data)
            logger.info(self.data)
        elif request.method == 'GET':
            self.data = request.GET

    def get_newest_revenue_id(self):
        try:
            cursor = connection.cursor()
            cursor.execute(GET_REVENUE_ID_SQL)
            print(GET_REVENUE_ID_SQL)
            num_dict = dictfetchone(cursor)
            print(num_dict)
            num = num_dict['nums']
            print(num)
            res = {
                'record_id': num+1
            }
            self._init_response()
            self.response.update(res)
            return self._get_response(HANDLE_OK, 1)

        except Exception as error:
            self._init_response()
            return self._get_response(SERVER_ERROR, -1)

    def get_revenue(self):
        try:
            cursor = connection.cursor()
            cursor.execute(GET_REVENUE_ORDER_SQL)
            rows = dictfetchall(cursor)
            res = {
                'records': rows
            }
            self._init_response()
            self.response.update(res)
            return self._get_response(HANDLE_OK, 1)

        except Exception as error:
            self._init_response()
            return self._get_response(SERVER_ERROR, -1)



    def add_revenue(self):
        try:
            actual_revenue = int(self.data['actual_revenue'])
            record_id = self.data['record_id']
            items = self.data['items']
            if len(items) == 0 or not record_id:
                return self._get_response(INVALID_BLANK, -1)

        except Exception as error:
            traceback.print_exc()
            self._init_response()
            return self._get_response(POST_ARG_ERROR, -1)

        try:
            cursor = connection.cursor()
            cursor.execute(CREATE_RECORD_SQL,
                           (record_id,))
            total_remained_value = 0
            total_expected = 0
            for item in items:
                cursor.execute(ADD_REVENUE_ITEM_AMOUNTS_SQL,(record_id, item['id'], item['amount']))
                cursor.execute(GET_ITEM_BY_ID_SQL, (item['id'],))
                items_dict = dictfetchone(cursor)
                item_selling_price = items_dict['selling_price']
                item_shelf_amount =items_dict['shelf_amount']
                cursor.execute(SET_ITEM_STOCK_AMOUNT_SQL, (item['amount'], item['id']))
                total_expected += (int(item_shelf_amount) - int(item['amount'])) * int(item_selling_price)
                total_remained_value += int(item_selling_price) * int(item['amount'])
            difference = total_expected - actual_revenue
            print(total_remained_value)
            cursor.execute(UPDATE_VALUE_INTO_RECORD, (actual_revenue,total_remained_value, total_expected, difference, record_id))
            connection.commit()
            self._init_response()
            return self._get_response(HANDLE_OK, 1)

        except Exception as error:
            traceback.print_exc()
            connection.rollback()
            self._init_response()
            return self._get_response(SERVER_ERROR, -1)
