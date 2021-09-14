from django.urls import path
from django.contrib import admin

app_name = 'accounts'
urlpatterns = [
    path('admin', admin.site.urls),
        # path('', home_page, name='home_page'),
]