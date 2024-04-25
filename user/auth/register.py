from django.views import View
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.shortcuts import render, redirect
from django.contrib import messages


class register_view (View) : 
    
    def get(self,request,**kwargs) :
        return render(request,'register.html')
    

    def post(self,request,**kwargs) : 
        data = {**request.POST}

        action = Action(
            url = MAIN_URL + "/user/auth/register/",
            data=data
        )

        if 'picture' in request.FILES : 
            action.files = {
                'picture' : request.FILES.get('picture')
            }

        
        action.post()

        if action.is_valid() : 
            user_token = action.json_data['access']
            res = redirect('profile')
            res.set_cookie('user',user_token)
            return res
        
        messages.error(request,'an error happened on registeration.')
        return redirect('register')