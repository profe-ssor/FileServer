from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Customer_page, name="home"),
    path('admin_page/', views.admin_page, name="admin"),
    path('register/', views.register_page, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path(
        'reset_password/',
        auth_views.PasswordResetView.as_view(template_name="authentication/passwords/password_reset.html"),
        name="reset_password"
    ),
    path(
        'reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="authentication/passwords/password_reset_sent.html"), 
        name="password_reset_done"
    ),
    path(
        'reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="authentication/passwords/password_reset_confirm.html"), 
        name="password_reset_confirm"
    ),
    path(
        'reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="authentication/passwords/password_reset_complete.html"), 
        name="password_reset_complete"
    ),

    

    path('feed_page/', views.feed_page, name="cards"),
    path('wedding_cards/', views.wedding_cards, name='wedding_cards'),
    path('admission_cards/', views.admission_cards, name='admission_cards'),
    path('engagement_cards/', views.engagement_cards, name='engagement_cards'),
    path('birthday_cards/', views.birthday_cards, name='birthday_cards'),
    path('file-feed/', views.feed_page, name='file_feed'),
    path('form_link/', views.form_link, name='form_link'),
    path('crud_page/', views.crud_page, name='check_page'),
    
    path('download/<str:file_type>/<int:file_id>/', views.download_file, name='download_file'),
    path('send_file/<str:file_type>/<int:file_id>/', views.send_file, name='send_file'),

    path('wedding_form/', views.wedding_form, name='wedding_form'),
    path('admission_form/', views.admission_form, name='admission_form'),
    path('engagement_form/', views.engagement_form, name='engagement_form'),
    path('birthday_form/', views.birthday_form, name='birthday_form'),

    path('update_wedding/<int:pk>/', views.update_wedding, name='update_wedding'),
    path('update_birthday/<int:pk>/', views.update_birthday, name='update_birthday'),
    path('update_admission/<int:pk>/', views.update_admission, name='update_admission'),
    path('update_engagement/<int:pk>/', views.update_engagement, name='update_engagement'),

    path('delete/<str:file_type>/<int:file_id>/', views.delete_file, name='delete_file'),
    path('view_file/<str:file_type>/<int:file_id>/', views.view_file, name='view_file'),
    ]


