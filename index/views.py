from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse(u"hello world")
def list(request):
	alist = ['one', 'two', 'three']
	return render(request, 'list.htm', {'testlist': alist})
