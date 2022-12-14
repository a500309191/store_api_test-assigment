from django.contrib import admin
from api.models import Product, Image


class ImageInline(admin.StackedInline):
    model = Image
    verbose_name = 'Product image'
    extra = 5
    max_num = 5
    field = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    list_display = ('name', 'article', 'price' , 'status')
    field = '__all__'