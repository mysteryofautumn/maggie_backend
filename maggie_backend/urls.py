"""maggie_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from maggie_backend.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getItems/', get_items),
    path('addItem/', add_item),
    path('deleteItem/', delete_item),
    path('editItem/', edit_item),
    path('authentication/', authentication),
    path('getItemById/', get_item_by_id),
    path('addInstock/', add_instock),
    path('getNewestInorderId/', get_newest_inorder_id),
    path('getInstock/', get_instock),
    path('getNewestOutorderId/', get_newest_outorder_id),
    path('addOutstock/', add_outstock),
    path('addRevenue/', add_revenue),
    path('getRevenue/', get_revenue),
    path('getNewestRevenueId/',get_newest_revenue_id)


    # getItems
    # return: {
    #    id: '',
    #    name: '',
    #
    #   }
    #
    # addItem
    # deleteItem
    # editItem
    # addInstockOrder
    # getInstockOrder get every instock-order's cost
    # addOutstockOrder
    # getReocrd
    # addRecord
]
