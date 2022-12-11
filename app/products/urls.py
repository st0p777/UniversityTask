from django.urls import path
from products.views import products, bucket_add, bucket_min, bucket_del

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('<int:category_id>/', products, name='category'),
    path('page/<int:page>/', products, name='page'),
    path('basket-add/<int:product_id>/', bucket_add, name='bucket_add'),
    path('basket-min/<int:product_id>/', bucket_min, name='bucket_min'),
    path('basket-del/<int:product_id>/', bucket_del, name='bucket_del'),
]
