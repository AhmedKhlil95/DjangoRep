from django.urls import path
from .views import SignUpView
from accounts import views
urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    path("signup/", views.register , name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    
]