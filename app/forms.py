from django.forms import fields
from django.forms import widgets
from app.models import Customer, OrderPlaced,Services, contact_us
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm,PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User,Group
from django.utils.translation import gettext, gettext_lazy as _
from django.forms.widgets import PasswordInput, TextInput, Widget
from django.contrib.auth import password_validation
from django import forms
from django.core.exceptions import ValidationError
from PIL import Image
from django import forms
#from django.core.files.uploadedfile import SimpleUploadedFile


from django.core.validators import RegexValidator

rgname=RegexValidator(r'^[a-z|A-Z" "a-z|A-Z]*$', 'Only alphabets are allowed.')

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label=_("User Name*"),validators=[rgname], widget=forms.TextInput(attrs={'class': 'form-control',}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                             max_length=64, help_text='Enter a valid email address',label=_("Email*"),)

    password1 = forms.CharField(label=_("Password*"), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=_("Confirm Password(again)*"), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
                               

    class Meta(UserCreationForm):
        model = User
        exclude = ('groups',)
        # fields = ("username","email","password1","password2")
        widgets ={'groups' : forms.HiddenInput(),
        }
        fields = ("username", "email", "password1", "password2","groups")
        sequence = fields


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class MypasswordChangeform(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'autofocus': True, 'class': 'form-control'}),
                                    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'autofocus': True, 'class': 'form-control'}))


class Mypasswordrestform(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254,
                             widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'}))


class Mysetpasswordform(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'New Password', 'class': 'form-contorl'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'Repeat Password', 'class': 'form-contorl'}),
    )


state_choice =(('Punjab' ,'Punjab') ,('Sindh' ,'Sindh'),('Khyber Pakhtunkhwa','Khyber Pakhtunkhwa'),('Gilgit-Baltistan' ,'Gilgit-Baltistan') ,('Islamabad Capital Territory' ,'Islamabad Capital Territory'),('Balochistan','Balochistan'))

#FORM OF PROFILE
class CustomerForm(forms.ModelForm):
    customer_image1= forms.ImageField(label='Image')
    state= forms.ChoiceField(label='State',choices=state_choice)
   
    class Meta():
       model = Customer
 #fields = ("username","email","password1","password2"   "name",)
       fields = ("mobile","whatsapp_no" ,"phone_no","Address","city" ,"state","postelcode", "customer_image1")
       widgets ={
        'Address' : forms.TextInput(attrs={'class':'form-control'}),
       'city' : forms.TextInput(attrs={'class':'form-control'}),
       'postelcode' : forms.TextInput(attrs={'class':'form-control'}),
    #    'name' : forms.TextInput(attrs={'class':'form-control'}),
       'phone_no' : forms.TextInput(attrs={'class':'form-control'}),
       'mobile' : forms.TextInput(attrs={'class':'form-control'}),
       'whatsapp_no' : forms.TextInput(attrs={'class':'form-control'}),  
    }
       sequence = fields

  



status_choice = (('Accepted', 'Accepted'),('Service is Start', 'Service is Start'),
                 ('Service is Complete', 'Service is Complete'),
                 ('Cancel', 'Cancel')
                 )  
stat= (('paid', 'paid'), ('unpaid', 'unpaid'))
#orderfrom
class DateInput(forms.DateInput):
    input_type = 'date'
class Orderfrom(forms.ModelForm):
    status= forms.ChoiceField(label='Status',choices=status_choice)
    start_date =forms.DateField(widget=DateInput)
    end_date =forms.DateField(widget=DateInput)


    class Meta():
       model = OrderPlaced
 
       fields = ("status","start_date","end_date","Total_Bill","Advance_payment","Remaing_Bill","Bill_status")
       widgets ={
       'start_date' : forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }),
    #    'quantity' : forms.TextInput(attrs={'class':'form-control'}),
       'Total_Bill' : forms.TextInput(attrs={'class':'form-control'}),
       'Advance_payment' : forms.TextInput(attrs={'class':'form-control'}),
       'Remaing_Bill' : forms.TextInput(attrs={'class':'form-control'}),
    #    'message' : forms.Textarea(attrs={'class':'form-control'})
       
       }
       sequence = fields

status_choice= (('read', 'read'), ('later', 'later'))
class contact_usform(forms.ModelForm):

     status= forms.ChoiceField(label='Status',choices=status_choice)
     class Meta():
       exclude = ('phone',)
       model = contact_us
       fields = ("status","phone")
       widgets ={'phone' : forms.HiddenInput()}
       sequence = fields
     














cate = (('Punjab' ,'Punjab') ,('Sindh' ,'Sindh'),('Khyber Pakhtunkhwa','Khyber Pakhtunkhwa'),('Gilgit-Baltistan' ,'Gilgit-Baltistan') ,('Islamabad Capital Territory' ,'Islamabad Capital Territory'),('Balochistan','Balochistan'))


catagory_emp = (('Electrician' ,'Electrician'),('Plumber' ,'Plumber'),('Sweaper' ,'Sweaper'),('Carpenter' ,'Carpenter'),('Drain clean' ,'Drain clean'),('AC repair' ,'AC repair'),('Painting & Decorating' ,'Painting & Decorating'))


class Servicesform(forms.ModelForm):
   Service_image1= forms.ImageField(label='Image')
   Province= forms.ChoiceField(label='State',choices=cate)
   Employee= forms.ChoiceField(label='Catagory',choices=catagory_emp)
   class Meta:
      model = Services
 
      fields = ['name','phone_no','mobile_no','address','Province','Employee','Cnic','city','Shop_References','Service_image1']
      widgets ={
       'name' : forms.TextInput(attrs={'class':'form-control'}),
       'phone_no' : forms.TextInput(attrs={'class':'form-control'}),
       'mobile_no' : forms.TextInput(attrs={'class':'form-control'}),
       'address' : forms.Textarea(attrs={'class':'form-control'}),
       
       'city' : forms.TextInput(attrs={'class':'form-control'}),
       'Cnic' : forms.TextInput(attrs={'class':'form-control'}),
       'Shop_References':forms.Textarea(attrs={'class':'form-control'}),
       
    #    'description' : forms.Textarea(attrs={'class':'form-control'}),
       
      }
      sequence = fields




# rating
stcus=( ('Service is Completed', 'Service is Completed'),
                 ('Service is not  Completed', 'Service is not Completed'),)

nmbr= (('1','1'),('2', '2'), ('3', '3'),('4','4'),('5','5'))
class Orderfromrating(forms.ModelForm):
    ratting= forms.ChoiceField(label='Ratting',choices=nmbr)
    statuscus= forms.ChoiceField(label='Status',choices=stcus)
    

    class Meta():
        
       model = OrderPlaced
 
       fields = ("ratting","statuscus","message")
       widgets ={
    #   message= forms.TextInput(label='Comment')
    #    'quantity' : forms.TextInput(attrs={'class':'form-control'}),
       'ratting' : forms.TextInput(attrs={'class':'form-control'}),
       'statuscus' : forms.TextInput(attrs={'class':'form-control'}),
       'message' : forms.Textarea(attrs={'class':'form-control'}),
       
       }
       sequence = fields
