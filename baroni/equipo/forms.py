from django import forms
from phonenumber_field.formfields import PhoneNumberField

class MemberForm(forms.Form):    
  name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre'})) 
  last_name = forms.CharField(label='Apellido', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
  email = forms.EmailField(label='Email', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
  phone = PhoneNumberField(label='Telefono', widget=forms.TextInput(attrs={'placeholder': 'Telefono'})) #usa phonenumber_field para validar campos de telefono
  bio = forms.CharField(label='Biografia', max_length=2000, widget=forms.TextInput(attrs={'placeholder': 'Biografía'}))
  position = forms.CharField(label='Cargo', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Cargo'}))  
  image = forms.ImageField(label='Imagen', widget=forms.FileInput(attrs={'placeholder': 'Imagen'}), required=True)