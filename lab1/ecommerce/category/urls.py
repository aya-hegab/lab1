from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.cat, name="catagory"),
    # path('products/', include('products.urls')),
]