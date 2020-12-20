from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic.edit import FormView




class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def form_invalid(self, form):  # 유효하지않을때 redirect 기능사용 
        return redirect('/product/' + str(form.product))

    def get_form_kwargs(self, **kwargs):  # form 을 생성할때 어떠한 인자값을 사용할것인가
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request' : self.request
        })
        return kw