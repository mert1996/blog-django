from django.contrib import admin
from blog.models import KategoriModel, YazilarModel

class YazilarAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'yazar','olusturulma_tarihi')
    search_fields = ("baslik", "yazar")


admin.site.register(KategoriModel)
admin.site.register(YazilarModel,YazilarAdmin)