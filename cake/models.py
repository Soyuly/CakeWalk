from secrets import choice
from sys import maxsize
from tkinter import CASCADE
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    telRex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    tel = models.CharField(validators=[telRex], max_length=16, unique=True)
    open_time = models.DateTimeField(input_formats=['%H : %M'])
    close_time = models.DateTimeField(input_formats=['%H : %M'])
    businessNumRex = RegexValidator(regex=r"([0-9]{3})-?([0-9]{2})-?([0-9]{5})")
    business_num = models.CharField(validators=[businessNumRex], max_length=12, unique=True)
    description = models.TextField()
    instagrame = models.URLField()
    notice = models.TextField()

class Store_Review(models.Model):
    store_review_id = models.IntegerField(primary_key=True)
    store_id = models.ForeignKey('Store', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    comment = models.TextField()
    pub_date = models.DateField()

class Store_Cake(models.Model):
    store_cake_id = models.IntegerField(primary_key=True)
    store_id = models.ForeignKey('Store', on_delete=CASCADE)
    image = models.ImageField(upload_to="appname", null=True)
    likes = models.IntegerField()

class Favorites_store(models.Model):
    user_id = models.ForeignKey('User', on_delete=CASCADE)
    store_id = models.ForeignKey('Store', on_delete=CASCADE)

class Recent_Cake(models.Model):
    user_id = models.ForeignKey('User', on_delete=CASCADE)
    store_cake_id = models.ForeignKey('Store_Cake', on_delete=CASCADE)

class Like_Cake(models.Model):
    user_id = models.ForeignKey('User', on_delete=CASCADE)
    store_cake_id = models.ForeignKey('Store_Cake', on_delete=CASCADE)

class Store_Order(models.Model):

    store_order_id = models.IntegerField()    
    user_id = models.ForeignKey('User', on_delete=CASCADE)
    store_cake_id = models.ForeignKey('Store_Cake', on_delete=CASCADE)
    order_date = models.DateTimeField()
    OPTION_CHOICES = ['1호', '2호', '3호', '기타']
    option_size = models.TextChoices(maxsize=2, choice=OPTION_CHOICES)
    OPTION_FLAVOR = ['바닐라']


