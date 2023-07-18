from django.forms import ModelForm
from blog.models import IletisimModel

class IletisimForm(ModelForm):
    class Meta:
        model = IletisimModel
        fields = ["isim_soyisim","email","mesaj"]
