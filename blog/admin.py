from django.contrib import admin
from blog.models import KategoriModel, YazilarModel, YorumModel, IletisimModel

class YazilarAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'yazar','olusturulma_tarihi')
    search_fields = ("baslik", "yazar")

class YorumAdmin(admin.ModelAdmin):
    list_display = ("yazan", "olusturulma_tarihi","guncellenme_tarihi")
    search_fields = ("yazan__username",)

class IletisimAdmin(admin.ModelAdmin):
    list_display = ("email","olusturulma_tarihi")
    search_fields = ("email",)



admin.site.register(KategoriModel)
admin.site.register(YazilarModel,YazilarAdmin)
admin.site.register(YorumModel, YorumAdmin)
admin.site.register(IletisimModel)