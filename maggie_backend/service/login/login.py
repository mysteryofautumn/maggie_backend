import traceback
from maggie_backend.constants.error_constants import *
from maggie_backend.constants.info_constants import *
from maggie_backend.service.base_service import BaseService
from django.db import connection
from maggie_backend.sql_uitilities.sqls import *
from maggie_backend.sql_uitilities.sql_util import *


class LoginManagement(BaseService):
    def __init__(self, request):
        super(LoginManagement, self).__init__(request)
        if request.method == 'POST':
            self.data = eval(request.body)
            print(self.data)
            logger.info(self.data)
        elif request.method == 'GET':
            self.data = request.GET

    def authentication(self):
        try:
            code = self.data['code']
        except Exception as error:
            traceback.print_exc()
            self._init_response()
            return self._get_response(POST_ARG_ERROR, -1)

        try:
            if code == LOGIN_CODE:
                self._init_response()
                return self._get_response(HANDLE_OK, 1)
            else:
                self._init_response()
                return self._get_response(WRONG_PASSWD, -1)

        except Exception as error:
            traceback.print_exc()
            self._init_response()
            return self._get_response(SERVER_ERROR, -1)
