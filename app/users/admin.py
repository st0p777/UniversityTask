from django.contrib import admin
from users.models import Users
from products.admin import ProdAdminInline


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    inlines = (ProdAdminInline, )
