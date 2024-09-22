from django.db import models
class vic_payment(models.Model):

    amount=models.CharField(max_length=100,default='')
  
    payment_id=models.CharField(max_length=100,default='')
    paid=models.BooleanField(default=False)


