from django.shortcuts import render, redirect
from account.forms import ProfilGuncelleForm
from django.contrib import messages


def profil_guncelle(request):
    if request.method == 'POST':
        form = ProfilGuncelleForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profiliniz başarıyla güncellendi.')
    else:
        form = ProfilGuncelleForm(instance=request.user)

    context={"form":form}
    return render(request,"pages/profil-guncelle.html", context=context)