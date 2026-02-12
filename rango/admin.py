from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
admin.site.register(Category)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)

        self.list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)