from django.contrib import admin

from .models import Category, Page, LastName, Data


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PageAdmin(admin.ModelAdmin):
    list_display = ('sub_name', 'category')


class LastNameAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'page')


class DataAdmin(admin.ModelAdmin):
    list_display = ('strain', 'min_range', 'max_range', 'size', 'dr_up_down', 'insertion_site', 'integrase')


admin.site.register(Category, CategoryAdmin)

admin.site.register(Page, PageAdmin)

admin.site.register(LastName, LastNameAdmin)

admin.site.register(Data, DataAdmin)


