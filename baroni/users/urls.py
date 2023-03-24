from django.urls import path
from .views import register, UserView, CustomLogoutView, CustomLoginView, login_status, logout_exit, UserUpdateView, CustomPasswordChangeView, password_status

urlpatterns = [
    path('signup/', register, name='register'),   
    path('profile/', UserView.as_view(), name='profile'), #as_view() es un metodo de clase que devuelve una vista 
    path('logout/', CustomLogoutView.as_view(), name='logout'), #as_view() es un metodo de clase que devuelve una vista
    path('logout_exit/', logout_exit, name='logout_exit'),    
    path('login/', CustomLoginView.as_view(), name='login'), #as_view() es un metodo de clase que devuelve una vista
    path('login_status/', login_status, name='login_status'),
    path('update/', UserUpdateView.as_view(), name='update_user'),
    path('password/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_status/', password_status, name='password_status'),
]