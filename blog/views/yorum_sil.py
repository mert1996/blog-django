from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from blog.models import YorumModel

@login_required(login_url="/")
def yorum_sil(request, id):
    yorum = get_object_or_404(YorumModel, id=id)

    if request.user == yorum.yazan or request.user == yorum.yazan:
        yorum.delete()
        return redirect("detay", slug=yorum.yazi.slug )
    return redirect("anasayfa")