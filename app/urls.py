from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),

    path('about',views.about,name='about'),

    path('faq',views.faq,name='faq'),

    path('blog-details',views.blog,name='blog'),

    path('gallery',views.gallery,name='gallery'),

    path('services/<int:pk>',views.services,name='services')


] 