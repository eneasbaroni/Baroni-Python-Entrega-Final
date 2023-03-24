from django import forms

class ObraForm(forms.Form):  
  choicess = ( (True, 'Si'), (False, 'No') )  # Opciones para poder armar booleano en el form
  name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre'})) 
  price = forms.IntegerField(label='Precio', widget=forms.NumberInput(attrs={'placeholder': 'Precio'}))
  area = forms.IntegerField(label='Area', widget=forms.NumberInput(attrs={'placeholder': 'Area'}))
  description = forms.CharField(label='Descripcion', max_length=2000, widget=forms.TextInput(attrs={'placeholder': 'Descripcion'}))
  credit = forms.ChoiceField(label='Apto Credito', choices=choicess, widget=forms.RadioSelect)
  image = forms.ImageField(label='Imagen', widget=forms.FileInput(attrs={'placeholder': 'Imagen'}))
  
  