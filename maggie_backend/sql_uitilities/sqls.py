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