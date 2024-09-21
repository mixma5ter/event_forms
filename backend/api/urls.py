from django.urls import path

from api.views import FormList

app_name = 'api'  # namespace

urlpatterns = [
    path('forms/', FormList.as_view(), name='forms'),
]
