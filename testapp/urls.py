from django.urls import path
from django.conf.urls import url
from . import views

app_name = "testapp"
urlpatterns =[url('signup/', views.signup, name = 'signup'),
        path('', views.index, name = 'index'),
        path('<int:article_id>/', views.detail, name = 'detail')
    ]
