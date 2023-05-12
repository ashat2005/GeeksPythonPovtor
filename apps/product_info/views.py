from django.shortcuts import render

from apps.products.models import Products
# Create your views here.
def info(request, id):
    product = Products.objects.get(id = id)
    context = {
        'product': product,
    }
    return render(request, 'course-detail.html', context)
