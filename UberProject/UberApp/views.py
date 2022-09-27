from django.shortcuts import render 
from django.http import HttpResponse
from .models import Uber

def price(request,id):
     object_id = Uber.objects.get(pk=id)
     DBP = object_id.DBP
     D = object_id.Distance
     DAP = object_id.DAP
     TBP = object_id.TMF

     Total_Price = (DBP + (D*DAP))*TBP

     return HttpResponse(f"Total Price is {Total_Price}")



