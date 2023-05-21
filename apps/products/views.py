from django.shortcuts import render, redirect
from apps.products.models import Products,Contact
from apps.setting.models import Setting
# Create your views here.
def product_detail(request, id):
    setting = Setting.objects.latest('id')
    product = Products.objects.get(id = id)
    context = {
        'setting': setting,
        'product': product,
    }
    return render(request, 'course-detail.html', context)
def course(request):
    course = Products.objects.all()
    context = {
        'course' : course
    }    
    return render(request, 'course.html', context)
def contact(request):
    contact = Contact.objects.all()
    context = {
        "contact" : contact
    }
    return render(request,'contact.html',context)