from django.urls import path
from blog.views import iletisim, anasayfa


urlpatterns = [
    path("iletisim/", iletisim),
    path("", anasayfa)
]