from django.views import View
from globals.request_manager import Action
from globals.decorators import login_required
from django.shortcuts import render
from frontend.settings import MAIN_URL

class get_battle(View) :
    
    @login_required
    def get (self,request,battle_id,**kwargs) :
        headers = kwargs['headers']
        action = Action(
            url = MAIN_URL + f"/battle/get/{battle_id}/",
            headers=headers
        )

        action.get()

        print(action.json_data)

        return render(request,'battle.html',{
            'battle_id' : battle_id,
            'players' : action.json_data['players'],
            'text' : action.json_data['text'],
        })
