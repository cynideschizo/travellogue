from django import forms
from django.forms import ModelForm, Textarea
from .models import Note

class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['title','pov','ff','blog','pic']
		widgets = {
			'text': Textarea(attrs={'cols': 50, 'rows': 6})
                    
		}
		labels = {
            'blog': '',
            'pov' : 'Place Of Visit',
            'ff' : 'Famous Food ',
            'title' : 'Subject of Blog '

        }
