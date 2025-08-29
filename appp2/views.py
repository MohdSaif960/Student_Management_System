from django.shortcuts import render

from .models import Teacher


# Create your views here.
def teacher_detail(request):
    teacher=Teacher.objects.all()
    return render(request,'appp2/teacher_detail.html',{'teacher':teacher})