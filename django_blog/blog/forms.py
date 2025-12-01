from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
       
        widgets = {
            "username": forms.TextInput(attrs={"class": "input_field"}),
            "first_name": forms.TextInput(attrs={"class": "input_field"}),
            "last_name": forms.TextInput(attrs={"class": "input_field"}),
            "email": forms.EmailInput(attrs={"class": "input_field"}),
        }

class PostForm(forms.ModelForm):
    tags_input = forms.CharField(
        required=False,
        label='Tags (comma separated)',
        widget=forms.TextInput(attrs={'placeholder': 'tag1, tag2, tag3'})
    )
    class Meta:
        model = Post
        fields = ['title', 'content', "tags"]  

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if self.instance.pk:
                current_tags = ', '.join([t.name for t in self.instance.tags.all()])
                self.fields['tags_input'].initial = current_tags

        def save(self, commit=True):
            post = super().save(commit=False)
            if commit:
                post.save()
            tags_str = self.cleaned_data.get('tags_input', '')
            tag_names = [t.strip() for t in tags_str.split(',') if t.strip()]
            new_tags = []
            for name in tag_names:
                tag_obj, _ = Tag.objects.get_or_create(name=name)
                new_tags.append(tag_obj)
            if commit:
                post.tags.set(new_tags)
            else:
                setattr(post, '_pending_tags', new_tags)
            return post
            
        widgets = {
            'tags': TagWidget(),  
        }





class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows':4, 'placeholder':'Write your comment...'})
        }  