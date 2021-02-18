from django.urls import path
from my_auth.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegisterView


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', RegisterView.as_view(), name='auth_register'),
]
