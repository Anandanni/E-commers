from django.urls import path
from.import views

urlpatterns = [
    path("",views.index,name="Blog home"),
    path("blogpost/<int:id>",views.blogpost,name="BlogPost")
    
] 
