
from django.urls import path
from . import views
from .views import update_selected_person

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login_user,name='login_user'),
    path('logout/',views.logout_user,name='logout_user'),
    path('register/',views.register_user,name='register_user'),
    path('record/<int:pk>',views.staff_record,name='record'),
    path('delete_staff_record/<int:pk>',views.delete_staff_record,name='delete_staff_record'),
    path('update_staff_record/<int:pk>',views.update_staff_record,name='update_staff_record'),
    path('add_staff_record/', views.add_staff_record, name='add_staff_record'),
    path('appointment_record/<int:pk>/', views.appointment_record, name='appointment_record'),
    path('bookapt/',views.bookapt,name='bookapt'),
    path('delete_appointment_record/<int:pk>',views.delete_appointment_record,name='delete_appointment_record'),
    path('update_appointment_record/<int:pk>',views.update_appointment_record,name='update_appointment_record'),
    path('appointment_register/', views.appointment_register, name='appointment_register'), 
    path('faq_chatbot/',views.faq_chatbot,name='faq_chatbot'),
    path('update_selected_person/<int:appointment_id>/', update_selected_person, name='update_selected_person'),
    path('compost_inquiry/',views.compost_inquiry,name='compost_inquiry'),
    path('compost_inquiry_record/<int:pk>/', views.compost_inquiry_record, name='compost_inquiry_record'),
    path('update_compost_inquiry_record/<int:pk>',views.update_compost_inquiry_record,name='update_compost_inquiry_record'),
    path('delete_compost_inquiry_record/<int:pk>',views.delete_compost_inquiry_record,name='delete_compost_inquiry_record'),
    path('blog_show/',views.blog_show,name='blog_show'),
    path('add_blog/',views.add_blog,name='add_blog'),
    path('update_blog/<int:pk>',views.update_blog,name='update_blog'),
    path('delete_blog/<int:pk>',views.delete_blog,name='delete_blog'),
    path('contact_us/',views.contact_us,name='contact_us'),
    
]
