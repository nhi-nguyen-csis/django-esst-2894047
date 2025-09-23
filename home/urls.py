# from django.urls import path
# from home.views import home, authorized

# urlpatterns = [
#     path('home/', home),
#     path('authorized/', authorized)
# ]

from django.urls import path
from home.views import HomeView, Authorized

urlpatterns = [
    path('home/', HomeView.as_view()),
    path('authorized/', Authorized.as_view())
]