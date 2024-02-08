from django.shortcuts import render
from django.http import HttpResponse

products=[{'id':1, 'name':'iphone', 'category':'smart phone'},{'id':2, 'name':'redmi', 'category':'smart phone'}, {'id':3, 'name':'samsung', 'category':'smart phone'}]
# Create your views here.
def cat(request):
  context = {}
  context['products'] = products
  return render(request, 'category/index.html', context)
