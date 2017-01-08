from django.shortcuts import render
from django.utils import timezone
from .models import BlogPost

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html')

def blog_home(request):
	posts = BlogPost.objects.all().order_by('published_date')
	return render(request, 'blog_list.html', {'posts': posts})