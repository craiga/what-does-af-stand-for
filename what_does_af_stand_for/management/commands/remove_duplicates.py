"""Command to remove duplicate words."""

import logging

from django.core.management.base import BaseCommand

from what_does_af_stand_for import models

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Remove duplicate words."""

    help = __doc__

    def handle(self, *args, **options):
        """Handle a call to the command."""
        # Set logging level.
        # 0 = minimal output, 1 = normal output, 2 = verbose output, and
        # 3 = very verbose output.
        verbosity = options["verbosity"]
        log_levels = (logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG)
        logger.setLevel(log_levels[verbosity])

        logger.info("Removing duplicate A words.")
        remove_duplicates(models.AWord)
        logger.info("Removing duplicate F words.")
        remove_duplicates(models.FWord)


def remove_duplicates(model_class):
    """Remove duplicate words."""
    words = model_class.objects.values_list("word", flat=True)
    words = set(word.lower() for word in words)
    for word in words:
        logger.debug('Looking for duplicates of "%s".', word)
        count = model_class.objects.filter(word__iexact=word).count()
        logger.debug("Found %d word(s).", count)
        if count > 2:
            first = model_class.objects.filter(word__iexact=word).first()
            model_class.objects.exclude(id=first.id).filter(word__iexact=word).delete()
