from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

#request is an object
#view to list the posts
def post_list(request):
    #retrieve all posts with "published" status with the custom publish manager
    posts = Post.published.all()

    #render list of postswith template name lists.html
    return render(request, 'blog/post/list.html', {'posts': posts})
    #returns an HttpResponse object

#detailed view for the post
def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug = post,
        status = 'published',
        publish__year = year,
        publish__month = month,
        publish__day = day)
    return render(request, 'blog/post/detail.html', {'post': post})
