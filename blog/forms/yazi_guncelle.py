from django import forms
from blog.models import YazilarModel

class YaziGuncelleForm(forms.ModelForm):
    class Meta:
        model = YazilarModel
        exclude = ["slug","yazar"]