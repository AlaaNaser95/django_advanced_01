from django.urls import path
from inventories import views


app_name = 'inventories'
urlpatterns = [
    path('list/<int:store_id>', views.inventory_list, name="list"),
    
]		