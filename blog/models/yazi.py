from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel

class YazilarModel(DateAbstractModel):
    resim = models.ImageField(upload_to="yazi_resimler")
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from="baslik", unique=True)
    kategoriler = models.ManyToManyField(KategoriModel, related_name = "yazi")
    yazar = models.ForeignKey("account.CustomUserModel", related_name="yazilar", on_delete=models.CASCADE)

    class Meta:
        db_table = "Yazilar"
        verbose_name='Yazı'
        verbose_name_plural = "Yazilar"

    def __str__(self):
        return self.baslik