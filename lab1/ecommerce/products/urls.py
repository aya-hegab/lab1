from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.helloworld, name="products"),
    # path('category/', include('category.urls')),
    path('<int:pid>', views.helloworld2),
]
