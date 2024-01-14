
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.core.validators import MinValueValidator ,MinLengthValidator




# validar

from django.core.validators import RegexValidator

pnumber = RegexValidator(r'^((0)(3)[0-9]{9})$', 'Only a whole number are allowed.')
rgname=RegexValidator(r'^[a-zA-Z" "a-zA-Z]*$', 'Only alphabets are allowed.')
rgcnic=RegexValidator(r'^[0-9]{13}$', 'Only 13 number are allowed.')
rgpost=RegexValidator(r'^[0-9]{5}$', 'Only 5 nuber are allowed.')
# end  valider


# Create your models here.
state_choice =(('Punjab' ,'Punjab') ,('Sindh' ,'Sindh'),('Khyber Pakhtunkhwa','Khyber Pakhtunkhwa'),('Gilgit-Baltistan' ,'Gilgit-Baltistan') ,('Islamabad Capital Territory' ,'Islamabad Capital Territory'),('Balochistan','Balochistan'))


class Customer(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=11 ,null=True, blank=True,validators=[pnumber])
    whatsapp_no =models.CharField(max_length=11,null=True, blank=True ,validators=[pnumber])
    phone_no = models.CharField(max_length=11,null=True, blank=True,validators=[pnumber])
    Address = models.CharField(max_length=200)
    Cnic=models.CharField(max_length=13, null=True, blank=True,validators=[rgcnic])
    postelcode = models.CharField(max_length=5,null=True, blank=True, validators=[rgpost])
    city = models.CharField(max_length=70,null=True, blank=True, validators=[rgname])
    state = models.CharField(choices=state_choice, max_length=200)
    email = models.EmailField(max_length=200)
    customer_image1 = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


category_choices = (('Punjab' ,'Punjab') ,('Sindh' ,'Sindh'),('Khyber Pakhtunkhwa','Khyber Pakhtunkhwa'),('Gilgit-Baltistan' ,'Gilgit-Baltistan') ,('Islamabad Capital Territory' ,'Islamabad Capital Territory'),('Balochistan','Balochistan'))
catagory_emp= (('Electrician' ,'Electrician'),('Plumber' ,'Plumber'),('Sweaper' ,'Sweaper'),('Carpenter' ,'Carpenter'),('Drain clean' ,'Drain clean'),('AC repair' ,'AC repair'),('Painting & Decorating' ,'Painting & Decorating'))


class Services(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name =  models.CharField(max_length=50,null=True, blank=True,validators=[rgname])
    phone_no = models.CharField(max_length=11 ,null=True, blank=True,validators=[pnumber])
    mobile_no = models.CharField(max_length=11 ,null=True, blank=True,validators=[pnumber])
    address = models.CharField(max_length=200,default='abc')
    city =  models.CharField(max_length=70 ,null=True, blank=True,validators=[rgname])
    Province = models.CharField(choices=category_choices,default='Punjab', max_length=56)
    Employee = models.CharField(choices=catagory_emp,default='Plumber', max_length=100)
    Cnic= models.CharField(max_length=13 ,null=True, blank=True,validators=[rgcnic])
    Shop_References = models.TextField(default='shop no address etc')
    Service_image1 = models.ImageField(upload_to='productimg')
  

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


    @property
    def total_cost(self):
       return self.quantity * self.service.discounted_price

stcus=( ('Service is Completed', 'Service is Completed'),
                 ('Service is not  Completed', 'Service is not Completed'),)

status_choice = (('Accepted', 'Accepted'), ('Service is Start', 'Service is Start'),
               ('Service is Complete', 'Service is Complete'),
                 ('Cancel', 'Cancel'))

stat= (('paid', 'paid'), ('unpaid', 'unpaid'))

nmbr= (('1','1'),('2', '2'), ('3', '3'),('4','4'),('5','5'))
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=status_choice, default='Pending')
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    message = models.TextField(null=True, default='none')
    Total_Bill = models.IntegerField(default=0)
    Advance_payment=models.IntegerField(default=0)
    Remaing_Bill=models.IntegerField(default=0)
    Bill_status= models.CharField(max_length=100, choices=stat, default='unpaid')
    ratting= models.CharField(max_length=100, choices=nmbr, default='pending')
    statuscus=models.CharField(max_length=100, choices=stcus, default='In progress')

    def __str__(self):
        return str(self.id)




####


# ##

    
    @property
    def total_price(self):
       return self.quantity * self.service.discounted_price    

# done


# class expence(models.Model):
    
#     title = models.CharField(max_length=100)
#     excost = models.FloatField(default=0.0)
#     description = models.TextField()

#     def __str__(self):
#         return str(self.id)


# class profit(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     service = models.ForeignKey(Services, on_delete=models.CASCADE)
#     expencess = models.ForeignKey(expence, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     total_costs = models.FloatField()
#     total_pad = models.FloatField(default=0.0)
#     remaing_amount = models.FloatField(default=0.0)
#     total_profit = models.FloatField(default=0.0)

#     def __str__(self):
#         return str(self.id)


class About_us(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    description = models.TextField()
    about_image1 = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
status_choice= (('read', 'read'), ('later', 'later'))

class contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Subject = models.CharField(max_length=200)
    phone = models.IntegerField()
    description = models.TextField()
    status=models.CharField(max_length=100, choices=status_choice, default='unread')
    msg_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


rate_choices = (('30', '30'), ('50', '50'), ('40', '40'),
                ('50', '50'), ('60', '60'), ('70', '70'), ('90', '90'),
                ('99', '99'), ('100', '100'))


class feed_back(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    name_of_serves = models.CharField(max_length=100)
    description = models.TextField()
    rate_us = models.CharField(choices=rate_choices, max_length=4)

    def __str__(self):
        return str(self.id)


class blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subject = models.EmailField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.id)



   ###customer
