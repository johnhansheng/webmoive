from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    GENDER_CHOICE=(
        ('M','男'),
        ('F','女'),
    )
    nickname=models.CharField(blank=True,null=True,max_length=20)
    avatar=models.FileField(upload_to='avatar/')
    mobile=models.CharField(blank=True,null=True,max_length=13)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICE,blank=True,null=True)  #性别字段，
    subscribe=models.BooleanField(default=False)

    class Meta:
        db_table="v_user"



# Create your models here.
