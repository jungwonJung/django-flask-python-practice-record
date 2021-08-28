from django.db import models

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='사용자' )     # user app 내의 models. User 라는 클래스를 ForeginKey (외래키)로 사용하겠다
                                                                                            # on_delete=models.CASCADE user라는 데이터값이 삭제될때 같이 삭제시키겠음
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='주문시간')

    def __str__(self):
        return str(self.user) + '' + str(self.product)

    class Meta:
        db_table = 'jung_order'  # 데이터베이스 테이블명 지정
        verbose_name = '주문'    # django-admin에서 보는이름지정
        verbose_name_plural = '주문'   #  django-admin에서 보는 복수형이름도 지정해주기로한다

"""
ForeignKey (외래키)를 사용하여 user app 폴더내의 models.py 내의 User 클래스에서 외래키를 가져오겠다
on_delete=models.CASCADE 는 만일 user,product 데이터값이 삭제될때 지금 Order의 설정한 models Order클래스내의 있는데이터값도 같이 지우겠다는설정
"""