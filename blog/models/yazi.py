from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class YazilarModel(models.Model):
    resim = models.ImageField(upload_to="yazi_resimler")
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from="baslik", unique=True)
    kategoriler = models.ManyToManyField(KategoriModel, related_name = "yazi")
    yazar = models.ForeignKey(User, related_name="yazilar", on_delete=models.CASCADE)

    class Meta:
        db_table = "Yazilar"
        verbose_name='Yazı'
        verbose_name_plural = "Yazilar"

    def __str__(self):
        return self.baslik