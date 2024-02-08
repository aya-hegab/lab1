from django.shortcuts import render
from django.http import HttpResponse

products=[{'id':1, 'name':'iphone', 'src':'1.jpeg'},{'id':2, 'name':'redmi', 'src':'2.jpeg'}, {'id':3, 'name':'samsung', 'src':'3.jpeg'}]
# Create your views here.
def helloworld(request):
  context = {}
  context['products'] = products
  return render(request, 'products/index.html', context)
def helloworld2(request, pid):
  myItem = list(filter(lambda t:t['id']==pid, products))  
  if myItem:
    return HttpResponse(f"hello world from products of {myItem}")
  else:
    return HttpResponse(f"item not found")