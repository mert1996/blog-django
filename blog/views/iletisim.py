from django.shortcuts import render

def iletisim(request):
    context = {
        "isim":"iletişim sayfasi"
    }
    return render(request, "pages/iletisim.html", context=context)