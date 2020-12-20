from django import forms
from .models import Order
from product.models import Product
from user.models import User


class RegisterForm(forms.Form):  

    def __init__(self, request, *args, **kwargs):  # 생성자 함수 __init__ 을 이용 현재 RegisterForm 에 request 를 전달할수있게 인터페이스 생성
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(     
        error_messages={
            'required' : '상품수량을 입력해주세요'
        }, label='상품수량'   
    )
    product = forms.IntegerField(     
        error_messages={
            'required' : '상품내용을 입력해주세요'
        },label='상품내용' , widget=forms.HiddenInput
    )
    
    def clean(self):
        cleaned_data = super().clean()    
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        user = self.request.session.get('user')

        if quantity and product and user:
            order = Order(
                quantity=quantity,
                product=Product.objects.get(pk=product),
                user=User.objects.get(email=user)
            )
            order.save()
        else:
            self.product = product
            self.add_error('quantity' , '값이 없습니다')
            self.add_error('product' , '값이 없습니다')