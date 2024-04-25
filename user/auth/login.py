from django.views import View
from globals.decorators import login_required
from django.shortcuts import render, redirect
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.contrib import messages

class login_view (View) : 
    
    def get(self,request,**kwargs) :
        return render(request,'login.html')
    

    def post(self, request,**kwargs) : 
        data = {**request.POST}
        data.pop('csrfmiddlewaretoken')

        action = Action(
            url = MAIN_URL + "/user/auth/login/",
            data=data
        )

        action.post()
        
        if action.is_valid() : 
            user_token = action.json_data['access']
            res = redirect('profile')
            res.set_cookie('user',user_token)
            return res
        
        messages.error(request,'invalid email or password ')
        return redirect('login')
