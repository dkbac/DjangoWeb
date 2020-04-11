from django.shortcuts import render
from .models import Post

# Create your views here.
def PostFetch(request):
    Data = {'Posts' : Post.objects.all()}
    return render(request, 'blog/post.html', Data)

def PostFetchById(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'blog/postdetail.html', {'post':post})