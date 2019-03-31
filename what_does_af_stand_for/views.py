"""Views"""

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from what_does_af_stand_for import forms, models


class FrontPageView(TemplateView):
    """Front page view."""

    template_name = "what_does_af_stand_for/front_page.html"

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super().get_context_data(**kwargs)
        a_word = models.AWord.objects.get_one_at_random()
        f_word = models.FWord.objects.get_one_at_random()
        context.update(
            {
                "a_word": a_word,
                "f_word": f_word,
                "thumbs_up_form": forms.ReactionForm(
                    {"reaction": "thumbs_up", "a_word": a_word.id, "f_word": f_word.id}
                ),
                "thumbs_down_form": forms.ReactionForm(
                    {
                        "reaction": "thumbs_down",
                        "a_word": a_word.id,
                        "f_word": f_word.id,
                    }
                ),
            }
        )
        return context

    def post(self, request, *args, **kwargs):
        """Handle a post request."""
        form = forms.ReactionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("front_page"))

        raise RuntimeError("Invalid form posted.")
