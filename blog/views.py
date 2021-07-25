from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hrllo index ส่งงานสัปดาห์ที่4เเละ5')

def about(request):
    return HttpResponse('hello about')

def persons(request):
    return HttpResponse('hello persons')

def contact(request):
    return HttpResponse('hello contact')
