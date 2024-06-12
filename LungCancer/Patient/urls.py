from django.urls import path
from .import views

urlpatterns=[
    # path('',views.home,name='homepage'),
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('doctor',views.doctor,name='doctor'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('treatment',views.treatment,name='treatment'),
    path('login',views.login,name="login"),
    path('logout',views.logout,name='logout'),
    path('LungPrediction',views.LungPrediction,name='LungPrediction')
]