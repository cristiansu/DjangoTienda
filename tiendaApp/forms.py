from django import forms
from django.forms import fields, widgets
from .models import Category,Products,Contact


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Products
        fields='__all__'

        widgets={

            'fecha_fabricacion':forms.SelectDateWidget()
        }


class ContactoForm(forms.ModelForm):

    class Meta:
        model=Contact
        #fields=['nombre','correo','tipo_consulta','mensaje','avisos'] otro camino es con __all__
        fields='__all__'