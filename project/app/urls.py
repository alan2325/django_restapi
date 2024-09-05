from django.urls import path
from.import views
urlpatterns = [
    path('sdfs',views.dict),
    path('std',views.student),
    path('fun',views.fun1),
    path('fun2',views.fun2),
    path('fun3',views.fun3),
    path('fun4',views.fun4),
    path('fun5/<int:d>',views.fun5),
    path('fun6',views.fun6.as_view()),
    path('fun7/<int:d>',views.fun7.as_view()),
]

