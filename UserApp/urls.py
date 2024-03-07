from django.urls import path
from . import views

app_name = 'UserApp'

urlpatterns = [
    path('user_profile/<str:username>/', views.user_profile, name='user_profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
    #settings page
    path('settings/', views.settings, name='settings'),
    # path('update_account_info/', views.update_account_info, name='update_account_info'),

]

