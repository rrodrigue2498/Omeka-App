from django.db import models
from ckeditor.fields import RichTextField 
from django.template.defaultfilters import slugify

# Create your models here.
class rsvp(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    note = RichTextField(blank=True)

    def __str__(self):
       return self.name

class Items(models.Model):
	title = models.CharField(max_length=30)
	slug = models.SlugField(max_length=30, null=True)
	description = RichTextField(blank=True, null=True)
	files = models.FileField(upload_to='media')
	attributes = models.TextField(blank=True)
	url = models.URLField(max_length=200, blank=True, null=True)
	date_created = models.DateField()
	
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Items, self).save(*args, **kwargs)
		
	def __str__(self):
		return self.title
		
class Creator(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	
	
