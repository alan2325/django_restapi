from django.urls import path
from.import views
urlpatterns = [
    path('sdfs',views.dict),
    path('std',views.student),
    path('fun',views.fun1),
    path('fun2',views.fun2),
]

