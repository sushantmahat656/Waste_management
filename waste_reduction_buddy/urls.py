
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
    path('delete_appointment_record/<int:pk>',views.delete_appointment_record,name='delete_appointment_record'),
    path('update_appointment_record/<int:pk>',views.update_appointment_record,name='update_appointment_record'),
    path('appointment_register/', views.appointment_register, name='appointment_register'), 
    path('faq_chatbot/',views.faq_chatbot,name='faq_chatbot'),
    path('update_selected_person/<int:appointment_id>/', update_selected_person, name='update_selected_person'),
    
     
]
