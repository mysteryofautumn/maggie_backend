import traceback

from maggie_backend.constants.error_constants import *
from maggie_backend.service.base_service import BaseService
from django.db import connection

from maggie_backend.sql_uitilities.sqls import *
from maggie_backend.sql_uitilities.sql_util import *


class ItemManagement(BaseService):
    def __init__(self, request):
        super(ItemManagement, self).__init__(request)
        if request.method == 'POST':
            self.data = eval(request.body)
            print(self.data)
            logger.info(self.data)
        elif request.method == 'GET':
            self.data = request.GET

    def add_item(self):
        try:
            name = self.data['name']
            purchasing_price = self.data['purchasing_price']
            selling_price = self.data['selling_price']
            stock_amount = self.data['stock_amount']
            shelf_amount = self.data['shelf_amount']
            comment = self.data['comment']
            restock = self.data['restock']
            if len(name) == 0 or \
                    len(purchasing_price) == 0 or len(selling_price) == 0 or len(stock_amount) \
                    == 0 or len(shelf_amount) == 0 or len(restock) == 0:
                self._init_response()
                return self._get_response(INVALID_BLANK, -1)


        except Exception as error:
            traceback.print_exc()
            self._init_response()
            return self._get_response(POST_ARG_ERROR, -1)

        try:
            cursor = connection.cursor()
            cursor.execute(ADD_ITEM_SQL,
                           (name, purchasing_price, selling_price, stock_amount, shelf_amount, comment, restock))
            connection.commit()
            self._init_response()
            return self._get_response(HANDLE_OK, 1)

        except Exception as error:
            traceback.print_exc()
            connection.rollback()
            self._init_response()
            return self._get_response(SERVER_ERROR, -1)

    def get_items(self):
        try:
            cursor = connection.cursor()
            connection.commit()
            cursor.execute(GET_ITEMS_SQL)
            rows = dictfetchall(cursor)
            reses = {
                "items": rows
            }
            self._init_response()
            self.response.update(reses)
            return self._get_response(HANDLE_OK, 1)

        except Exception as error:
            traceback.print_exc()
            connection.rollback()
            self._init_response()
            return self._get_response(SERVER_ERROR, -1)

    def delete_item(self):
        try :
            item_id = self.data['item_id']
        except Exception as error:
            traceback.print_exc()
            self._init_response()
            return self._get_response(POST_ARG_ERROR, -1)

        try:
            cursor = connection.cursor()
            cursor.execute(DELETE_ITEM_SQL, (item_id,))
            connection.commit()
            self._init_response()
            return self._get_response(HANDLE_OK, 1)

        except Exception as error:
            traceback.print_exc()
            connection.rollback()
            self._init_response()
            return self._get_response(SERVER_ERROR, -1)

    def edit_item(self):
        try:
            item_id = self.data['item_id']
            name = self.data['name']
            purchasing_price = self.data['purchasing_price']
            selling_price = self.data['selling_price']
            stock_amount = self.data['stock_amount']
            shelf_amount = self.data['shelf_amount']
            comment = self.data['comment']
            restock = self.data['restock']
        except Exception as error:
            traceback.print_exc()
            self._init_response()
            return self._get_response(POST_ARG_ERROR, -1)

        try:
            cursor = connection.cursor()
            cursor.execute(EDIT_ITEM_SQL,
                           (name, purchasing_price, selling_price, stock_amount, shelf_amount, comment, restock,item_id))
            connection.commit()
            self._init_response()
            return self._get_response(HANDLE_OK, 1)

        except Exception as error:
            traceback.print_exc()
            connection.rollback()
            self._init_response()
            return self._get_response(SERVER_ERROR, -1)

    def get_item_by_id(self):
        try:
            item_id = self.data['item_id']
        except Exception as error:
            traceback.print_exc()
            self._init_response()
            return self._get_response(POST_ARG_ERROR, -1)

        try:
            cursor = connection.cursor()
            cursor.execute(GET_ITEM_BY_ID_SQL, (item_id,))
            connection.commit()
            rows = dictfetchone(cursor)
            self._init_response()
            reses = {
                "name": rows['name'],
                "purchasing_price": rows['purchasing_price'],
                "selling_price":rows['selling_price'],
                "stock_amount":rows['stock_amount'],
                "shelf_amount":rows['shelf_amount'],
                "comment": rows['comment'],
                "restock": rows['restock']
            }
            self._init_response()
            self.response.update(reses)
            return self._get_response(HANDLE_OK, 1)

        except Exception as error:
            traceback.print_exc()
            connection.rollback()
            self._init_response()
            return self._get_response(SERVER_ERROR, -1)





