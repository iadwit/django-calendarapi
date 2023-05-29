from django.urls import path
from mycal.views import GoogleCalendarInitView, GoogleCalendarRedirectView
urlpatterns = [
    path('rest/v1/calendar/init/',
         GoogleCalendarInitView.as_view(), name='calendar_init'),
    path('rest/v1/calendar/redirect/',
         GoogleCalendarRedirectView.as_view(), name='calendar_redirect'),

]
