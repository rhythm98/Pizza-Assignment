from django.urls import path,include
from .views import PizzaAPI,Pizza_ListAPI,sizeAPI


urlpatterns = [
        path("",PizzaAPI.as_view()),
        path("getPizza/",Pizza_ListAPI.as_view()),
        path("addSize/",sizeAPI.as_view())
]