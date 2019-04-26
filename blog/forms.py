from django import forms
from .models import Post



class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {'title': forms.TextInput(attrs={'size': 60}), 'body': forms.Textarea(attrs={'rows':4, 'cols':70}),}
        labels = {'title': 'Название поста', 'body': 'Текст поста', }
 

