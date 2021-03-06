from django import forms
from django.forms import fields
from .models import Pizza, Topping, Comment

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["name", "image"]
        labels = {"name": ""}
class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ["name"]
        labels = {"name": ""}
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name"]
        labels = {"name": ""}
