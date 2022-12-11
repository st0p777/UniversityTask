from django.contrib import admin
from products.models import ProductCategory, Product, Basket, Exchanges


admin.site.register(ProductCategory)
admin.site.register(Basket)
admin.site.register(Exchanges)


@admin.register(Product)
class AdminProducts(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'quantity')
    fields = (('name', 'image'), ('description', 's_description'), ('price', 'quantity'), 'category')
    ordering = ('name', )
    search_fields = ('name', )


class ProdAdminInline(admin.TabularInline):
    model = Basket
    fields = ('product', 'count', 'created_timestamp', 'status')
    readonly_fields = ('created_timestamp', )
