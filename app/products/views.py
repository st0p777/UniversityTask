from django.shortcuts import render, HttpResponseRedirect
from products.models import ProductCategory, Product, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def index(request):
    context = {'title': 'Магазин', }
    return render(request, 'products/index.html', context)


def products(request, page=1, category_id=None):
    context = {
        'title': 'Магазин',
        'categories': ProductCategory.objects.all(),
    }
    product = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(product, 6).page(page)
    context.update({'products': paginator})
    context.update({'number': len(product)})
    return render(request, 'products/products.html', context)


@login_required
def bucket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product)
    else:
        basket = baskets.first()
        basket.count += 1
        basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def bucket_min(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, count=1)
    else:
        basket = baskets.first()
        if basket.count > 1:
            basket.count -= 1
            basket.save()
        else:
            bucket_del(request, product_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def bucket_del(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if baskets.exists():
        baskets.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




