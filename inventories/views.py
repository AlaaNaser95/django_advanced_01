from django.shortcuts import render
from .models import Inventory
from stores.models import Store
# Create your views here.
def inventory_list(request, store_id):
	store=Store.objects.get(id=store_id)
	context={
	"inventories":store.inventory_set.all()
	}
	return render(request,"inventorylist.html",context)