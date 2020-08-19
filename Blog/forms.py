# forms.py 
from django.forms import ModelForm
from django import forms
from Blog.models import Post

class PostForm(forms.ModelForm): 

	class Meta: 
		model = Post 
		fields = ['title', 'subtitle','author','slug','img','content'] 
		widgets = {
        'title': forms.TextInput(attrs={'placeholder': 'Enter Blog Title'}),
        'subtitle': forms.TextInput(attrs={'placeholder': 'Enter Subtitle'}),
        'author': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
        'slug': forms.TextInput(attrs={'placeholder': '(This will show in your blog url.Do not write more than 30 words)'})
    }


		
