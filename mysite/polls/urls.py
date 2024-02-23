from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # ex. /polls/
    path("", views.index, name="index"),
    # ex. /4/detail/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex. /2/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex. /9/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
