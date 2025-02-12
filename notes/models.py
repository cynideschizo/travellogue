from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from PIL import Image

class Note(models.Model):
	title = models.CharField(max_length=50)
	pov = models.CharField(max_length=20)
	ff = models.CharField(max_length=100)
	blog = models.TextField(max_length=15000)
	created = models.DateTimeField(auto_now_add=True)
	pic = models.ImageField(upload_to='images',default='IMG')
	author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
		)

	def save(self, *args, **kwargs):
		super().save()
		img = Image.open(self.pic.path)
		width, height = img.size  # Get dimensions

		if width > 300 and height > 300:
			# keep ratio but shrink down
			img.thumbnail((width, height))

		# check which one is smaller
		if height < width:
			# make square by cutting off equal amounts left and right
			left = (width - height) / 2
			right = (width + height) / 2
			top = 0
			bottom = height
			img = img.crop((left, top, right, bottom))

		elif width < height:
			# make square by cutting off bottom
			left = 0
			right = width
			top = 0
			bottom = width
			img = img.crop((left, top, right, bottom))

		if width > 300 and height > 300:
			img.thumbnail((300, 300))

		img.save(self.pic.path)

	def _str_(self):
		return self.text


	def get_absolute_url(self):
		return reverse('note_detail', args=[str(self.id)])
