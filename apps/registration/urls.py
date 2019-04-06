from django.conf.urls import  url
from apps.registration.views import RegisterUser, WelcomeUser
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, \
    PasswordResetDoneView, PasswordResetCompleteView
from django.urls import reverse_lazy

urlpatterns = [
    url(r'register', RegisterUser.as_view(), name="register"),
    url(r'welcome', WelcomeUser.as_view(), name="welcome"),
    url(r'login', LoginView.as_view(template_name='user/login.html'), name="login"),
    url(r'logout', LoginView.as_view(template_name='user/logout.html'), name="logout"),
    url(r'password/reset/$',
        PasswordResetView.as_view(success_url=reverse_lazy('registration:password_reset_done')),
        name="password_reset"),
    url(r'password/reset/done',
        PasswordResetDoneView.as_view(),
        name="password_reset_done"),
    url(r'password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(success_url=reverse_lazy('registration:password_reset_completeS')),
        name="password_reset_confirm"),
    url(r'password/reset/complete',
        PasswordResetCompleteView.as_view(),
        name="password_reset_completeS"),

]