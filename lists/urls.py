from django.urls import path

from lists.views import home


urlpatterns = [
    path('', home)
]