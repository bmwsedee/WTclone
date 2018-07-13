from django.shortcuts import render
from django.shortcuts import render
from .models import Post
from .models import timezone


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'rtblog/post_list.html', {'posts': posts})