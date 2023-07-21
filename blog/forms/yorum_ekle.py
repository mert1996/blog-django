from django import forms
from blog.models import YorumModel

class YorumEkleForm(forms.ModelForm):
    class Meta:
        model = YorumModel
        fields = ["yorum"]