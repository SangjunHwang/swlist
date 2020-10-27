from django.contrib import admin
from django.urls import path
from board import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list),
    path('write', views.write),
    path('insert', views.detail),
    path('detail', views.update),
    path('update', views.delete),
    path('delete', views.download),
    path('reply_insert', views.reply_insert),
]
