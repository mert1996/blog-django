from django.shortcuts import get_object_or_404
from blog.models import KategoriModel
# from django.core.paginator import Paginator
from django.views.generic import ListView

class KategoriView(ListView):
    template_name = "pages/kategori.html"
    context_object_name = "yazilar"
    paginate_by = 2

    def get_queryset(self):
        kategori = get_object_or_404(KategoriModel, slug=self.kwargs["kategoriSlug"])
        return kategori.yazi.all().order_by("-id")

# def kategori(request, kategoriSlug):
#     kategori = get_object_or_404(KategoriModel, slug=kategoriSlug)
#     print(kategori)

#     yazilar = kategori.yazi.order_by("-id")

#     sayfa = request.GET.get('sayfa')
#     paginator = Paginator(yazilar,2)
    
#     context = {
#         "yazilar": paginator.get_page(sayfa),
#         "kategori_isim":kategori.isim
#     }
#     return render(request, "pages/kategori.html", context=context)