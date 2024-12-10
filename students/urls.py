from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# app_name='students'


urlpatterns = [
    path('newsletter/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('course-details/', views.course, name='course-details'),
    path('courses/', views.courses, name='courses'),
    path('events/', views.events, name='events'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('starter/', views.starter, name='starter'),
    path('trainers/', views.trainer, name='trainers'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



