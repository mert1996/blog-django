from django.urls import path
from blog.views import iletisim, anasayfa, kategori, yazilarim


urlpatterns = [
    path("iletisim/", iletisim, name="iletisim"),
    path("", anasayfa, name="anasayfa"),
    path("kategori/<slug:kategoriSlug>", kategori, name="kategori"),
    path("yazilarim", yazilarim, name="yazilarim")
]