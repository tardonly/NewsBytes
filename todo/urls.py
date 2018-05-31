from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall'),
    url(r'^logout/$', auth_views.logout,{'next_page': '/'}, name='logout'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'$', views.index,name='index' ),
]
