from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

from .models import BlogPost
from .forms import ContactForm

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html')

def blog_home(request):
	posts = BlogPost.objects.all().order_by('published_date')
	return render(request, 'blog_list.html', {'posts': posts})

def contact(request):
	form_class = ContactForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			form_content = request.POST.get('content', '')

			# email the profile with the contact information
			template = get_template('contact_template.html')
			context = Context({
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content,
				})
			content = template.render(context)
			email = EmailMessage(
				"Contact Form submission",
				content,
				"your website" + '',
				['higgottluke@gmail.com'],
				headers = {'Reply-To': contact_email}
				)
			email.send()
			return redirect('contact')


	return render(request, 'contact.html', {
		'form': form_class,
		})
