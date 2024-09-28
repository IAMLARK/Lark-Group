from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('tech_dashboard', views.tech_dashboard, name="tech_dashboard"),
    path('finance_dashboard', views.finance_dashboard, name="finance_dashboard"),
    path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
    path('', views.login_user, name="login"),
    path('logout/', views.logout_user, name='logout'),
]
