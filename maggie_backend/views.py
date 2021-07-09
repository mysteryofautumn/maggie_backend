from maggie_backend.service.instock_management.instock_management import InstockManagement
from maggie_backend.service.item_management.item_management import ItemManagement
from maggie_backend.logger import logger
from maggie_backend.service.login.login import LoginManagement
from maggie_backend.service.outstock_management.outstock_management import OutstockManagement
from maggie_backend.service.record_management.revenue_management import RevenueManagement


def add_item(request):
    logger.info(request)
    return ItemManagement(request).add_item()


def get_items(request):
    return ItemManagement(request).get_items()


def delete_item(request):
    return ItemManagement(request).delete_item()


def edit_item(request):
    return ItemManagement(request).edit_item()


def authentication(request):
    return LoginManagement(request).authentication()


def get_item_by_id(request):
    return ItemManagement(request).get_item_by_id()


def add_instock(request):
    return InstockManagement(request).add_instock()


def get_newest_inorder_id(request):
    return InstockManagement(request).get_newest_inorder_id()

def get_instock(request):
    return InstockManagement(request).get_instock()

def get_newest_outorder_id(request):
    return OutstockManagement(request).get_newest_outorder_id()

def add_outstock(request):
    return OutstockManagement(request).add_outstock()


def get_revenue (request):
    return RevenueManagement(request).get_revenue()


def add_revenue(request):
    return RevenueManagement(request).add_revenue()


def get_newest_revenue_id(request):
    return RevenueManagement(request).get_newest_revenue_id()

