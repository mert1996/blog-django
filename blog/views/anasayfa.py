from django.shortcuts import render


def anasayfa(request):
    context = {
        "isim":"someone who"
    }
    return render(request, "pages/anasayfa.html", context=context)