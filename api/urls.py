from django.urls import path
from . import views

urlpatterns=[
    path('doctors',views.getDoctor),
    path('doctors/<str:pk>/', views.doctorProfile),
    path('register/', views.doctorRegister, name='doctor_registration'),
]