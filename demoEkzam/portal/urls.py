# portal/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('reports/', views.reports, name='reports'),
    path('admin/', views.admin_panel, name='admin_panel'),
    path('update_status/<int:report_id>/<str:status>/', views.update_status, name='update_status'),
]
