from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



class HomeView(TemplateView):
    @method_decorator(login_required) # @method_decorator(login_required) 를 decorator 로 달면 로그인이 필요한페이지에서 로그인을안하면 로그인하라고 말해줌
    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)
    
    template_name = 'home.html'

