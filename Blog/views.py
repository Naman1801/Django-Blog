from django.shortcuts import render,HttpResponse,redirect
from Blog.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Blog.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView



# Create your views here.
@login_required
def blogHome(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Blog  has been successfully Posted :)')
            return redirect('home')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request,'blog/blogHome.html',context)

# def blogHome(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         stitle = request.POST['stitle']
#         author = request.POST['author']
#         slug = request.POST['slug']
#         content = request.POST['content']
#         img = request.POST['image']

#         blog = Post(title=title,subtitle=stitle,author=author,slug=slug,content=content,img=img)
#         blog.save()
#         messages.success(request,f'Hello {author} Your Blog successfully Posted !')
#         return redirect('blogHome')
        
#     return render(request,'blog/blogHome.html')

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request,'blog/blogPost.html',context)

class PostUpdateView( UpdateView):
    model = Post
    fields = ['title', 'subtitle','author','slug','content','img']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False