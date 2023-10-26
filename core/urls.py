from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('job-list/', views.job_list, name='job_list'),
    path('job-detail/<int:pk>/', views.job_detail, name='job_detail'),
    path('job-post/', views.job_post, name='job_post'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('about/', views.about, name='about'),




]
