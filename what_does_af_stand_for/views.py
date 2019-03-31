"""Views"""

from django.shortcuts import render

from what_does_af_stand_for import models


def what_does_af_stand_for_view(request):
    """What does AF stand for?"""
    return render(
        request,
        "what_does_af_stand_for/what_does_af_stand_for.html",
        {
            "a_word": models.AWord.objects.get_one_at_random(),
            "f_word": models.FWord.objects.get_one_at_random(),
        },
    )
