from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text',]
        widgets = {
            'comment_text': forms.Textarea(attrs={'cols': 120, 'rows': 2}),
        }

