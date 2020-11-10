from django import models

class Addresses(models.model):
    name = models.Charfield(max_length=10)
    phone_number = models.Charfield(max_length=13)
    address = models.Textfield
    created = models.DateTimeField(auto_now_add=True)  # 현재 시간을 기록하는 코드

    class Meta:
        ordering = ['created']