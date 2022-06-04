from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('email/', views.email),
    path('attachment/', views.attachment),
    path('template/', views.template),
    path('email-admins/', views.admin_email)
]
