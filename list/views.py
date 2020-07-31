from django.shortcuts import render
from .models import List

# Create your views here.

def list(request):
    listdata = List.objects
    return render(request,'list.html',{'listdatas':listdata})