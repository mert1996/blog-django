from django.contrib import admin
from blog.models import KategoriModel, YazilarModel, YorumModel, IletisimModel

@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'yazar','olusturulma_tarihi')
    search_fields = ("baslik", "yazar")

@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    list_display = ("yazan", "olusturulma_tarihi","duzenlenme_tarihi")
    search_fields = ("yazan__username",)

@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    list_display = ("email","olusturulma_tarihi")
    search_fields = ("email",)

admin.site.register(KategoriModel)
