from django.views import View
from globals.decorators import login_required
from django.shortcuts import render

class profile_view (View) : 
    
    @login_required
    def get(self,request,**kwargs) :
        return render(request,'home.html')