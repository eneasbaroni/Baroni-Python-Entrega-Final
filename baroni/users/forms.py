from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    #Lo siguiente solo es para agregarle label y placeholder a los campos del formulario. sino solo sería email = forms.EmailField(required=True)
    email = forms.EmailField(required=True, label='email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(max_length=30, required=True, label='Username', widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    first_name = forms.CharField(max_length=30, required=True, label='Nombre', widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(max_length=30, required=True, label='Apellido', widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    profile_pic = forms.ImageField(required=False, label='Imagen de perfil', widget=forms.FileInput(attrs={'placeholder': 'Imagen de perfil'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'profile_pic')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.profile_pic = self.cleaned_data["profile_pic"]
        if commit:
            user.save()
        return user  
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=254, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de Usuario'}))   
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_pic')

