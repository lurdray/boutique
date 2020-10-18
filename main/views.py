from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import *
from django.contrib import messages

# Create your views here.

def index(request):
	settings = Setting.objects.all()
	categorys = Category.objects.all()
	sliders = Slider.objects.all()
	products = Product.objects.all().order_by('-pub_date')[:6]
	cataloques = Cataloque.objects.all().order_by('-pub_date')
	commentbanners = CommentBanner.objects.all().order_by('?')[:1]
	comments = Comment.objects.all()
	context = {'settings':settings,
				'sliders':sliders,
				'products': products,
				'cataloques':cataloques,
				'commentbanners':commentbanners,
				'comments':comments,
				'categorys':categorys,
				}
	#messages.success(request, "Your message has been delivered thank you")
	return render(request, "main/index.html", context)

def about(request):
	settings = Setting.objects.all()
	sliders = Slider.objects.all().order_by('?')[:1]
	context = {"settings":settings,
				"sliders":sliders,
				}
	return render(request, "main/about.html", context)



def product(request):
	settings = Setting.objects.all()
	products = Product.objects.all().order_by('-pub_date')
	sliders = Slider.objects.all().order_by('?')[:1]
	context = {"settings":settings,
				"sliders":sliders,
				"products":products,

			}
	return render(request,"main/product.html", context)

def contact(request):
	settings = Setting.objects.all()
	sliders = Slider.objects.all().order_by('?')[:1]

	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')


		contact_model = ContactModel.objects.create(name=name, email=email, phone=phone, message=message)
		contact_model.save()
		messages.success(request, "Your message has been delivered")
		return HttpResponseRedirect('/contact')


	context = {"sliders":sliders, "settings":settings}
	return render(request, "main/contact.html", context)

