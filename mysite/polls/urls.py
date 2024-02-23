from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # ex. /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex. /4/detail/
    path("<int:question_id>/", views.DetailView.as_view(), name="detail"),
    # ex. /2/results/
    path("<int:question_id>/results/", views.ResultView.as_view(), name="results"),
    # ex. /9/vote/
    path("<int:question_id>/vote/", views.VoreView.as_view(), name="vote"),
]
