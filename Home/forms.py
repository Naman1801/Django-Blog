from django.forms import ModelForm
from django import forms
from Home.models import Contact

class ContactForm(forms.ModelForm): 

	class Meta: 
		model = Contact
		fields = ['name','email','phone','msg']
		widgets = {
        'name': forms.TextInput(attrs={'placeholder': 'Enter Name'}),
        'email': forms.TextInput(attrs={'placeholder': 'Enter Email'}),
        'phone': forms.TextInput(attrs={'placeholder': 'Enter Phone Number'}),
        'msg': forms.TextInput(attrs={'placeholder': 'Write your message'})
    }
		