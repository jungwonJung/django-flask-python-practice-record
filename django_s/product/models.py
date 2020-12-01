from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')  # 숫자를 적을수있게 IntegerField 사용
    description = models.TextField(verbose_name='상품내용')  # 상품내용을 길게 적을수있게 TextField 사용 제한이없다
    stuck = models.IntegerField(verbose_name='재고')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    
    def __str__(self):    # 각 모델을 문자열로 변환했을때 표시해주기위함
        return self.name


    class Meta:
        db_table = 'jung_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'   # 복수형이름도 지정해주기로한다

"""
일반적으로 상품의 정보를 표시할때는 상품명 상품가격 상품의내용 그리고 재고수량과 상품이 등록된날짜가 필요하다
상품명은 Charfield 로 표시가능하고 가격은 숫자만 입력할것이기때문에 Integerfield 로 생성한다
상품의내용은 길게적을수도있게 textfield 로 설정해준뒤 재고도 숫자만입력할것이기때문에 가격과 동일
상품의 등록날짜는 user.models.py 에서 설정한 register_date 와 동일하게 사용할것이다
"""