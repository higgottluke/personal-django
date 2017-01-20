from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages

from .models import BlogPost, Project
from .forms import ContactForm

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html')

def blog_home(request):
	posts = BlogPost.objects.all().order_by('published_date')
	return render(request, 'blog_list.html', {'posts': posts})

def blog_post(request, name):
	undashed_name = name.replace("-", " ")
	post = BlogPost.objects.get(title=undashed_name)
	return render(request, 'blog_post.html', {'post': post})

def projects_home(request):
	projects = Project.objects.all().order_by('created_date')
	return render(request, 'projects_list.html', {'projects': projects})

def project(request, name):
	undashed_name = name.replace("-", " ")
	project = Project.objects.get(title=undashed_name)
	return render(request, 'project.html', {'project': project})

def contact(request):
	form_class = ContactForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			form_content = request.POST.get('content', '')

			# send the info
			send_mail(
				'New Contact Form from {}'.format(contact_name),
				form_content,
				contact_email,
				['higgottluke@gmail.com'],
				fail_silently=False,
				)
				
			messages.add_message(request, messages.SUCCESS, "Your message was sent successfully! I'll answer as soon as I can.")
			return redirect('contact')
		else:
			messages.add_message(request, messages.WARNING, "Something went wrong. Try filling the form out again.")
			return redirect('contact')


	return render(request, 'contact.html', {
		'form': form_class,
		})
