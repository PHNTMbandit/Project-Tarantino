from django.urls import reverse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import Http404, HttpResponseRedirect

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Walk for at least 60 minutes every day!",
    "april": "Walk for at least 60 minutes every day!",
    "may": "Walk for at least 60 minutes every day!",
    "june": "Walk for at least 60 minutes every day!",
    "july": "Walk for at least 60 minutes every day!",
    "august": "Walk for at least 60 minutes every day!",
    "september": "Walk for at least 60 minutes every day!",
    "october": "Walk for at least 60 minutes every day!",
    "november": "Walk for at least 60 minutes every day!",
    "december": None,
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"month": month, "text": challenge_text},
        )
    except:
        raise Http404()


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        raise Http404()
    else:
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
