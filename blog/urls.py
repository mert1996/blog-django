from django.urls import path
from blog.views import IletisimView, anasayfa, KategoriView, yazilarim, DetayView, YaziEkleView, YaziGuncelleView, YaziSilView, yorum_sil
from django.views.generic import TemplateView

urlpatterns = [
    path("iletisim/", IletisimView.as_view(), name="iletisim"),
    path("hakkimda", TemplateView.as_view(template_name="pages/hakkimda.html"), name="hakkimda"),
    path("", anasayfa, name="anasayfa"),
    path("kategori/<slug:kategoriSlug>", KategoriView.as_view(), name="kategori"),
    path("yazilarim", yazilarim, name="yazilarim"),
    path("detay/<slug:slug>", DetayView.as_view() , name="detay"),
    path("yazi-sil/<slug:slug>", YaziSilView.as_view() , name="yazi-sil"),
    path("yorum-sil/<int:id>", yorum_sil , name="yorum-sil"),
    path("yazi-ekle", YaziEkleView.as_view() , name="yazi-ekle"),
    path("yazi-guncelle/<slug:slug>", YaziGuncelleView.as_view() , name="yazi-guncelle"),
]