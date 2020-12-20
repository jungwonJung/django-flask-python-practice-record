from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm
# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'  # templates 에서 사용할 변수명 지정

class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs): # 원하는데이터를 넣을수있는 함수사용 get_context_data
        context = super().get_context_data(**kwargs) # 1. 먼저생성된 context에
        context['form'] = OrderForm(self.request)  # 2. form 이라는 변수로 하나의 데이터를 추가
        return context   # 3. 그걸반환
