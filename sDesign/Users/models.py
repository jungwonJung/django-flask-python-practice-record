from django.db import models

# Create your models here.
class Sdesign_Users(models.Model):
    username = models.CharField(max_length=64)
    userpw = models.CharField(max_length=64)
    useremail = models.EmailField(max_length=64)
    createtime=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='sdesign_users'