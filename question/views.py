from django.shortcuts import render

from .models import Anquan, Xianchang


def anquan(request):
    ti = Anquan.objects.all()
    return render(request,'question.html',{'ti':ti})

def xianchang(request):
    ti = Xianchang.objects.all()
    return render(request,'question.html', {'ti':ti})
