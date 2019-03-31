"""Models"""

from random import randint

from django.db import models


class WordModelManager(models.Manager):
    """Word model manager"""

    def get_one_at_random(self):
        """Choose a word at random"""
        num_instances = self.count()
        if not num_instances:
            raise self.model.DoesNotExist()

        return self.all()[randint(0, num_instances - 1)]


class WordModel(models.Model):
    """A word"""

    word = models.TextField()

    objects = WordModelManager()

    def __str__(self):
        return self.word

    class Meta:
        abstract = True


class AWord(WordModel):
    pass


class FWord(WordModel):
    pass


class Combination(models.Model):
    """A combination of an A- and an F-word."""

    a_word = models.ForeignKey(AWord, on_delete=models.CASCADE)
    f_word = models.ForeignKey(FWord, on_delete=models.CASCADE)
    thumbs_up = models.PositiveIntegerField(default=0)
    thumbs_down = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.a_word} {self.f_word} 👍 {self.thumbs_up} 👎 {self.thumbs_down}"

    class Meta:
        unique_together = ["a_word", "f_word"]
