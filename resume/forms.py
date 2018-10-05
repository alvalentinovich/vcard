from django import forms
from .models import Post, Comment, Resume, Offer

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('title', 'text',)

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('author', 'text',)
