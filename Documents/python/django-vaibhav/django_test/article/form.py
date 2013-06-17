from django import forms
from models import Article,Comment

class ArticleForm(forms.ModelForm):
	
	class Meta:
		model = Article
		fields = ('title','body','pub_date','thumbnail')#include the name of the fields in the models.py to display in the meta function
		
class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ('name','body')
