from django import forms
from models import Artical

class ArticleForm(forms.ModelForm):
	
	class Meta:
		model = Artical
		fields =  {'title','alt_title','body','pub_date','star_image','optional_image'}
		#fields = '__all__'
'''class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = {'name','body'}
'''