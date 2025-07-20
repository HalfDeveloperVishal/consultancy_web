from django.urls import path
from . import views

urlpatterns=[
    path("",views.home, name="home"),
    path('about/',views.about, name="about"),
    path("contact/",views.contact,name="contact"),
    path('service/',views.service,name="service"),
    path('ukcolleges/',views.ukcollege,name="ukcollege"),
    path('cancolleges/',views.cancollege,name="cancollege"),
    path('uscolleges/',views.uscollege,name="uscollege"),
    path('auscolleges/',views.auscollege,name="auscollege"),
    path('colleges/harvard/', views.uk_harvard_unversity_detail_view, name='uk_harvard_university_detail'),
    path('colleges/stanford/', views.uk_stanford_unversity_detail_view, name='uk_stanford_unversity_detail'),
    path('colleges/stanford/', views.uk_mit_unversity_detail_view, name='uk_mit_unversity_detail'),
]