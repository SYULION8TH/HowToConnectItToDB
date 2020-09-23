from django.shortcuts import render,redirect
from .models import Post
from django.utils import timezone
def post_view(request):
    posts = Post.objects.all()
    return render(request, 'index.html',{"posts": posts})

def put_data(request):
    post_title = request.POST['post_title']
    post_content = request.POST.get('post_content','')
    created_at = timezone.datetime.now()
    post = Post(post_title = post_title, post_content= post_content, created_at= created_at)
    post.save()
    return redirect(post_view)