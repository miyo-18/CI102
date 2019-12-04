from django.conf.urls import url
from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

app_name = 'accounts'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name="login"),
    path('post/', views.post, name='post')

    #url('^$', views.home),
]
