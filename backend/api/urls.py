from django.urls import path

from api.views import FormAPIView

app_name = 'api'  # namespace

urlpatterns = [
    path('forms/', FormAPIView.as_view(), name='form-base'),
    path('forms/<int:id>/', FormAPIView.as_view(), name='form-detail'),
]
