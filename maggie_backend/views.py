from maggie_backend.service.item_management.item_management import ItemManagement
from maggie_backend.logger import logger


def add_item(request):
    logger.info(request)
    return ItemManagement(request).add_item()


def get_items(request):
    return ItemManagement(request).get_items()


def delete_item(request):
    return ItemManagement(request).delete_item()


def edit_item(request):
    return ItemManagement(request).edit_item()