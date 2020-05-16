from django.contrib import admin
from django.urls import path, include

from todo.views import todo_list

urlpatterns = [
    path('admin/', admin.site.urls),
    #separate app urls and call them with an include
    path('', include('todo.urls', namespace='todos')),
]
