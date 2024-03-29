from django.shortcuts import render, redirect
from blog.forms import IletisimForm
from blog.models import IletisimModel
from django.views.generic import FormView

class IletisimView(FormView):
    template_name = "pages/iletisim.html"
    form_class = IletisimForm
    success_url ="/email-gonderildi"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



# def iletisim(request):
#     form = IletisimForm()

#     if request.method == "POST":
#         form = IletisimForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect("anasayfa")


#     context = {
#         "form": form
#     }
#     return render(request, "pages/iletisim.html", context=context)