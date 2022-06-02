from django.urls import path
from .views import UploadImage, IndexView, DeleteImage

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('upload', UploadImage.as_view(), name='upload'),
    path('delete/<int:pk>', DeleteImage.as_view(), name='delete'),
]
