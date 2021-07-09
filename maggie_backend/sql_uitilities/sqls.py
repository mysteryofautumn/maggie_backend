ADD_ITEM_SQL = 'insert into item(name, purchasing_price,selling_price,stock_amount,shelf_amount,comment,restock) values (%s, %s, %s,%s, %s, %s, %s)'

GET_ITEMS_SQL = 'select * from item'

DELETE_ITEM_SQL = 'delete from item where id = %s'

EDIT_ITEM_SQL = 'update item set name=%s, ' \
                'purchasing_price = %s' \
                ',selling_price = %s' \
                ',stock_amount = %s' \
                ',shelf_amount = %s' \
                ',comment = %s' \
                ',restock = %s where id = %s'

AUTHENTICATION_SQL = 'select code from user_login where id=0'

GET_ITEM_BY_ID_SQL = 'select * from item where id = %s'

CREATE_INORDER_SQL = 'insert into instock_order(id) values(%s)'

ADD_ITEM_AMOUNTS_SQL = 'insert into instock_item_amount(order_id, item_id, amount) values(%s, %s, %s)'

ADD_ITEM_STOCK_AMOUNT_SQL = 'update item set stock_amount=stock_amount+%s where id=%s'

GET_INORDER_ID_SQL = 'select count(*) as nums from instock_order'

GET_ITEM_PRICE_BY_ID_SQL = 'select purchasing_price from item where id=%s'

ADD_COST_TO_INORDER_SQL = 'update instock_order set cost =%s where id = %s'

GET_INSTOCK_ORDER_SQL = 'select * from instock_order'

GET_OUTORDER_ID_SQL = 'select count(*) as nums from outstock_order'

CREATE_OUTORDER_SQL = 'insert into outstock_order(id) values(%s)'

ADD_OUT_ITEM_AMOUNTS_SQL = 'insert into outstock_item_amount(order_id, item_id, amount) values(%s, %s, %s)'

ADD_ITEM_SHELF_AMOUNT_SQL = 'update item set shelf_amount = shelf_amount+%s where id=%s'

MINUS_ITEM_STOCK_AMOUNT_SQL = 'update item set stock_amount = stock_amount-%s where id=%s'

GET_REVENUE_ID_SQL = 'select count(*) as nums from record'

GET_REVENUE_ORDER_SQL = 'select * from record'

CREATE_RECORD_SQL = 'insert into record(id) values (%s)'

ADD_REVENUE_ITEM_AMOUNTS_SQL = 'insert into record_item_amount(record_id, item_id, amount) values(%s, %s, %s)'

SET_ITEM_STOCK_AMOUNT_SQL = 'update item set shelf_amount = %s where id = %s '

GET_ITEM_SELLING_PRICE_BY_ID_SQL = 'select selling_price from item where id =%s'

UPDATE_VALUE_INTO_RECORD = 'update record set actual_revenue=%s,remained_value=%s, expected_revenue=%s, difference=%s where id=%s'


