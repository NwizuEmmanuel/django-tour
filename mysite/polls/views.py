from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice


# Create your views here.
def index(request):
    latest_question = Question.objects.order_by("pub_date")[:5]
    context = {"latest_question": latest_question}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    responds = "You are looking at result of question %s."
    return HttpResponse(responds % question_id)


def vote(request, question_id):
    response = "You are voting on question %s."
    return HttpResponse(response % question_id)
