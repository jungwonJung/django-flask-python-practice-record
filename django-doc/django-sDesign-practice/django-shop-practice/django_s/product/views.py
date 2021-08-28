from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
from django.utils.decorators import method_decorator
from user.decorators import admin_required
from order.forms import RegisterForm as OrderForm
from rest_framework import generics
from rest_framework import mixins
from .serializers import ProductSerializer
# Create your views here.


class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin ):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin ): # RetrieveModelMixin 상세보기를 위한 mixin
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'  # templates 에서 사용할 변수명 지정

@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            description=form.data.get('description'),
            stuck=form.data.get('stuck')
        )
        product.save()
        return super().form_valid(form)

class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs): # 원하는데이터를 넣을수있는 함수사용 get_context_data
        context = super().get_context_data(**kwargs) # 1. 먼저생성된 context에
        context['form'] = OrderForm(self.request)  # 2. form 이라는 변수로 하나의 데이터를 추가
        return context   # 3. 그걸반환


