from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    balance = models.FloatField(null=True)
    stockvalue = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name

class Coin(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    #STATUS = (
    #    ('Pending', 'Pending'),
    #    ('Finished', 'Finished'),
    #) 
    coin = models.ForeignKey(Coin, null=True, on_delete= models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    amount = models.FloatField(null=True)
    class Meta:
        pendingPrice = 0

class Stock(models.Model):
    coin = models.ForeignKey(Coin, null=True, on_delete= models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    amount = models.FloatField(null=True)

@receiver(post_save, sender=Order)
def afterPurchase(sender, instance, created, **kwargs):
    if created:
        cost = instance.amount*instance.price
        if cost > 10:
            mystock = Stock.objects.filter(customer=instance.customer, coin=instance.coin)
            if mystock is None:
                stock = Stock()
                stock.coin = instance.coin
                stock.customer = instance.customer
                stock.amount = instance.amount
                stock.save()
            else:
                mystock.amount += instance.amount
            instance.delete()
        else:
            Order.pendingPrice += cost
            if Order.pendingPrice > 10:
                for i in Order.objects.all():
                    mystock = Stock.objects.filter(customer=i.customer, coin=i.coin)
                    if mystock is None:
                        stock = Stock()
                        stock.coin = i.coin
                        stock.customer = i.customer
                        stock.amount = i.amount
                        stock.save()
                    else:
                        mystock.amount += i.amount
                    i.delete()
                Order.pendingPrice = 0    
            else:
                return True
    return True