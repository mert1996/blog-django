from django import forms
from blog.models import YazilarModel

class YaziEkleForm(forms.ModelForm):
    class Meta:
        model = YazilarModel
        exclude = ["slug","yazar"]