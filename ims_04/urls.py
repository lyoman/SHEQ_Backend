from django.urls import path
from django.contrib import admin

app_name = 'newstock'
urlpatterns = [
    path('', admin.site.urls),
        # path('', home_page, name='home_page'),
]