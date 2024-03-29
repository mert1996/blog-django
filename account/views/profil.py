from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from account.models import CustomUserModel

class ProfilView(DetailView):
    template_name = "pages/profil.html"
    context_object_name = "profil"


    def get_object(self):
        return get_object_or_404(CustomUserModel, username=self.kwargs.get("username"))