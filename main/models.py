from django.db import models
from django.utils import timezone

class Slider(models.Model):
	image = models.ImageField(upload_to='images')
	title = models.CharField(max_length=100, default="none")
	description = models.TextField()

	def __str__(self):
		return self.title

class Setting(models.Model):

	STATUS = (
		('True', 'True'),
		('False', 'False'),
	)
	title = models.CharField(max_length=150)
	keywords = models.CharField(max_length=350)
	description = models.CharField(max_length=350)
	address = models.CharField(blank=True, max_length=150)
	company = models.CharField(blank=True, max_length=150)
	phone = models.CharField(blank=True, max_length=15)
	#fax = models.CharField(blank=True, max_length=20)
	email = models.CharField(blank=True, max_length=50)
	footer = models.TextField(blank=True, max_length=50)
	newsletter = models.CharField(blank=True, max_length=50)
	#smtppassword = models.CharField(blank=True, max_length=50)
	smtpport = models.CharField(blank=True, max_length=50)
	icon = models.ImageField(blank=True, upload_to='images')
	facebook = models.CharField(blank=True, max_length=50)
	instagram = models.CharField(blank=True, max_length=50)
	twitter = models.CharField(blank=True, max_length=50)
	aboutheader = models.TextField(blank=True, max_length=500)
	aboutus = models.TextField(blank=True, max_length=500)
	contact = models.TextField(blank=True, max_length=500)
	references = models.TextField(blank=True,  max_length=500)
	image = models.ImageField(upload_to='images')
	imagetwo = models.ImageField(upload_to='images')
	status = models.CharField(max_length=10, choices=STATUS)

	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class ContactModel(models.Model):
	"""docstring for ContactModel"""
	name = models.CharField(max_length=60, default="none")
	email = models.CharField(max_length=60, default="none")
	phone = models.CharField(max_length=60, default="none")
	message = models.CharField(max_length=60, default="none")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class Category(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title


class Product(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	description = models.TextField()
	price = models.CharField(max_length=60, default="none")
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title

class Comment(models.Model):
	image = models.ImageField(upload_to='images')
	comment = models.TextField()
	name = models.CharField(max_length=60, default="none")
	post = models.TextField()

	def __str__(self):
		return self.name
	



class Cataloque(models.Model):
	title = models.CharField(max_length=50, default="none")
	image = models.ImageField(upload_to='Images')
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


class CommentBanner(models.Model):
	title = models.CharField(max_length=50, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.title





