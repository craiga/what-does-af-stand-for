"""Forms"""

from django import forms

from what_does_af_stand_for import models


class ReactionForm(forms.Form):
    """Reaction form"""

    a_word = forms.ModelChoiceField(
        queryset=models.AWord.objects.all(), widget=forms.HiddenInput()
    )
    f_word = forms.ModelChoiceField(
        queryset=models.FWord.objects.all(), widget=forms.HiddenInput()
    )
    reaction = forms.ChoiceField(
        choices=[("thumbs_up", "👍"), ("thumbs_down", "👎")], widget=forms.HiddenInput()
    )

    def save(self):
        """Save a reaction."""
        combination, _ = models.Combination.objects.get_or_create(
            a_word=self.cleaned_data["a_word"], f_word=self.cleaned_data["f_word"]
        )
        reaction = self.cleaned_data["reaction"]
        setattr(combination, reaction, getattr(combination, reaction) + 1)
        combination.save()
