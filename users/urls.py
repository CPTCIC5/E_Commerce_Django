from django.urls import path
from . import views
from django.contrib.auth import views as v_views

app_name='users'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',v_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('order_history/',views.order_history,name='order_history'),
    path('logout/',v_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('password_reset/',v_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),

    path('password_reset_done/',v_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',v_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete',v_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete')

]