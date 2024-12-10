from django.urls import path
from . import views


urlpatterns = [
 path('', views.home, name='home'),
 path('black-friday', views.black_friday, name='black_friday'),
 path('package/<int:id>/', views.package_detail, name='package_detail'),
]
