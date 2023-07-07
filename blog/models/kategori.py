from django.db import models
from autoslug import AutoSlugField

class KategoriModel(models.Model):
    isim = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from="isim", unique=True)

    class Meta:
        db_table = "kategori"
        verbose_name ="Kategori"
        verbose_name_plural = "Kategoriler"

    def __str__(self):
        return self.isim   # tabloda isimler gözükecek