from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from Home.models import Contact
from Blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Home.forms import ContactForm
import math
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.

def home(request):
    no_of_posts = 3
    page = request.GET.get('page')

    if page is None:
        page = 1
    else:
        page = int(page)

    allPosts = Post.objects.all()
    length = len(allPosts)
    allPosts = allPosts[(page-1)*no_of_posts: page*no_of_posts]

    if page>1:
        prev = page-1
    else:
        prev = None
    
    if page < math.ceil(length/no_of_posts):
        nxt = page+1
    else:
        nxt = None
    print(prev,nxt)
    context = {'allPosts':allPosts,'prev':prev,'nxt':nxt}
    # print(context)
    return render(request,'home/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'home/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'allPosts'
    ordering = ['-timeStamp']
    paginate_by = 3







# class UserPostListView(ListView):
#     model = Post
#     template_name = 'home/user_posts.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'allPosts'
#     paginate_by = 4

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Post.objects.filter(author=user).order_by('-timeStamp')









def about(request):
    return render(request,'home/about.html')

# def handlelogout(request):
#     logout(request)
#     messages.success(request,'You have been successfully Logged Out!')
#     return redirect('home')
#     return render(request,'users/logout.html')

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('uname')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('pass1')
#         pass2 = request.POST.get('pass2')


#         if not username.isalnum():
#             messages.error(request,"Username shoud be alphanumeric less than 10 character")
#             return redirect('singup')
#         if pass1 != pass2:
#             messages.error(request,"Password do no Match")
#             return redirect('singup')

#         myuser = User.objects.create_user(username,email,pass1)
#         myuser.save()
#         messages.success(request,f'Hello {username} your account has been successfully created!')
#         return redirect('login')
    
#     return render(request,'home/singup.html')

# def handlelogin(request):
#     if request.method == 'POST':
#         username = request.POST['uname']
#         password = request.POST['pass']

#         user = authenticate(username=username,password=password)

#         if user is not None:
#             login(request,user)
#             messages.success(request,f'Hello {username} you have been successfully Logged In!')
#             return redirect('home')
            
#         else:
#             messages.error(request,'Invalid Credential, Please try again!')
#             return redirect('login')
#     return render(request,'users/login.html')

def contact(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thank-You for contating with us, we will get back to you soon :)')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {
        'form': form,
    })



    # form = ContactForm()
    # if request.method == 'POST':
    #     form = ContactForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('contact')
    # else:
    #     form = ContactForm()
    # context = {'form': form}
    # return render(request,'home/contact.html')


# def contact(request):
    
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         msg = request.POST['msg']
#         # print(name,email,phone.msg)
    
#         if(len(name)<2 or len(email)<5 or len(phone)<10 or len(msg)<5):
#             messages.error(request,"Please fill your details correctly!")
#             return redirect('contact')
#         else:
#             contact = Contact(name=name,email=email,phone=phone,msg=msg)
#             contact.save()
#             params= name.capitalize()
#             messages.success(request,f'Hello {params} your form successfully submitted!')
#             return redirect('contact')

#     return render(request,'home/contact.html')