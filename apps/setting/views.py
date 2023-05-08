from django.shortcuts import render

# Create your views here.
from apps.setting.models import Setting
# Create your views here.
def index(request):
    setting = Setting.objects.all()
    context = {
        'setting': setting,
    }
    return render(request,'index.html', context)