from django.db import models
from register.models import User
# Create your models here.

class Expense(models.Model):

    CATEGORY_OPTIONS=[
        ('ONLINE_SERVIES','ONLINE_SERVIES'),
        ('TRAVEL','TRAVEL'),
        ('FOOD','FOOD'),
        ('RENT','RENT'),
        ('OTHERS','OTHERS')
    ] 
    # 열쇠-값(key-value) 쌍의 튜플(tuple)을 포함하는 튜플을 정의해서 choices 인자에 전달합니다. 
    # 열쇠/값(key/value) 쌍에서 값(value)은 사용자가 선택할 수 있는 표시값인 반면, 열쇠(key)는 그 옵션이 선택되었을 때 실제로 저장되는 값입니다
    category = models.CharField(choices=CATEGORY_OPTIONS,max_length=255)
    amount = models.DecimalField(
        max_digits=10,decimal_places=2,max_length=255)
    # 10 진수 표현으로, python에서 Decimal 인스턴스로 나타냄
    # django.db.models.fields.DecimalField에 해당
    # DecimalField(max_digits, decimal_places, coerce_to_string=None, max_value=None, min_value=None)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)


    class Meta:
        ordering:['-date']

    def __str__(self):
        return str(self.owner) + 's income'