from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    myname = "one tow three"
    taisan = ["Dien Thoai", "máy tính", "Máy bay"]
    context = {"name":myname, "taisan":taisan}    

    return render(request,'pages/home.html',context)
