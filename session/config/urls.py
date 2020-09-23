from django.contrib import admin
from django.urls import path
from mydb import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_view),
    path('put_data/',views.put_data,name="put_data"),
]
