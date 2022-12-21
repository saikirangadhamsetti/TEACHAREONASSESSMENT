from django.urls import path
from .views import Productlist,particularproduct
urlpatterns=[
path("products/",Productlist.as_view()),
path("product/<int:id>",particularproduct.as_view())
]