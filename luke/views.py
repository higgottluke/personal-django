from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages
from django.http import Http404
from .forms import ContactForm

from .models import BlogPost, Project
from .forms import ContactForm

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html')

def blog_home(request, tag=''):
	if tag != '':
		tag = tag.replace('-',' ')
		posts = BlogPost.objects.filter(tags__contains=tag).order_by('published_date')
		if len(posts)!= 0:
			messagestring = "Showing {} blog post(s) with tags matching: '{}'.".format(len(posts), tag)
			messages.add_message(request, messages.INFO, messagestring)
			return render(request, 'blog_list.html', {'posts': posts})
		else:
			messagestring = "I have no posts with a tag matching: '{}'".format(tag)
			messages.add_message(request, messages.ERROR, messagestring)

	posts = BlogPost.objects.all().order_by('published_date')
	return render(request, 'blog_list.html', {'posts': posts}) #show all posts

def blog_post(request, name):
	undashed_name = name.replace("-", " ")
	try:
		post = BlogPost.objects.get(title=undashed_name)
	except BlogPost.DoesNotExist:
		messages.add_message(request, messages.ERROR, "I don't have any posts with that name. Sorry!")
		raise Http404()
	return render(request, 'blog_post.html', {'post': post})

def projects_home(request, tag=''):
	if tag != '':
		tag = tag.replace('-',' ')
		projects = Project.objects.filter(tags__contains=tag).order_by('created_date')
		if len(projects)!= 0:
			messagestring = "Showing {} project(s) with tags matching: '{}'.".format(len(projects), tag)
			messages.add_message(request, messages.INFO, messagestring)
			return render(request, 'projects_list.html', {'projects': projects})
		else:
			messagestring = "I have no projects with a tag matching: '{}'".format(tag)
			messages.add_message(request, messages.ERROR, messagestring)

	projects = Project.objects.all().order_by('created_date')
	return render(request, 'projects_list.html', {'projects': projects}) #show all posts

def project(request, name):
	undashed_name = name.replace("-", " ")
	try:
		project = Project.objects.get(title=undashed_name)
	except Project.DoesNotExist:
		messages.add_message(request, messages.ERROR, "I don't have any projects with that name. Sorry!")
		raise Http404()
	return render(request, 'project.html', {'project': project})

def contact(request):
	form_class = ContactForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			form_content = request.POST.get('content', '')

			template = get_template('contact_template.html')
			context = Context({
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content,
				})
			content = template.render(context)

			email_to_luke = EmailMessage(
				"New Contact Form Submission",
				content,
				'luke@higgott.com',
				['luke@higgott.com',],
				reply_to=[contact_email]
				)
			email_to_luke.content_subtype = "html"
			email_to_luke.send()
			email_to_them = EmailMessage(
				"Thanks for the message!",
				"<p>This is what you sent me:</p>" + content + "<p>I'll answer as soon as I can.</p>",
				'luke@higgott.com',
				[contact_email],
				reply_to=['luke@higgott.com']
				)
			email_to_them.content_subtype = "html"
			email_to_them.send()

			messages.add_message(request, messages.SUCCESS, "Your message was sent successfully! I'll answer as soon as I can. You should receive a copy of your message at your email address soon.")
			return redirect('contact')
		else:
			messages.add_message(request, messages.WARNING, "Something went wrong. Try filling the form out again.")
			return redirect('contact')

	return render(request, 'contact.html', {
		'form': form_class,
		})
