from django.db import models
class customer(models.Model):
    full_name=models.CharField(max_length=150)
    contact=models.CharField(max_length=150)
    email_address=models.CharField(max_length=150)
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    confirm_password=models.CharField(max_length=150)
class food(models.Model):
    foodtype=models.CharField(max_length=150)
    price=models.CharField(max_length=150)
    image=models.CharField(max_length=150)
    foodname=models.CharField(max_length=150)
    starttime=models.CharField(max_length=150)
class order(models.Model):
    total_amount=models.CharField(max_length=150)
    menu_id=models.CharField(max_length=150)
    customer_id=models.CharField(max_length=150)
    order_status=models.CharField(max_length=150)
    quantity=models.CharField(max_length=150)