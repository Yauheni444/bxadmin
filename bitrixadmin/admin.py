from django.contrib import admin
from .models import *


class b_iblock_typeAdmin(admin.ModelAdmin):
    list_display = ('id_name', 'sections', 'sort') #список выводимых полей в таблице
    #list_display_links = ('id') #ссылки
    #search_fields = ('sort') # по каким полям можем проводить поиск



admin.site.register(b_iblock_type, b_iblock_typeAdmin)
admin.site.register(b_iblock)
admin.site.register(b_iblock_element)
admin.site.register(b_iblock_section)
admin.site.register(b_iblock_property)
admin.site.register(b_iblock_element_property)
admin.site.register(b_iblock_section_property)