

from django.urls import path
from accounts import views as accounts_views

urlpatterns = [
    path('say-hi/',accounts_views.say_hi)

]