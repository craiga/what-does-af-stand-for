"""Command to import AF phrases."""

import argparse
import logging

from django.core.management.base import BaseCommand

import what_does_af_stand_for
from what_does_af_stand_for import models

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Import AF phrases."""

    help = __doc__

    def add_arguments(self, parser):
        parser.add_argument("af_file", type=argparse.FileType("r"))

    def handle(self, *args, **options):
        """Handle a call to the command."""
        # Set logging level.
        # 0 = minimal output, 1 = normal output, 2 = verbose output, and
        # 3 = very verbose output.
        verbosity = options["verbosity"]
        log_levels = (logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG)
        logger.setLevel(log_levels[verbosity])
        logger.debug("Logger configured.")

        af_file = options["af_file"]
        for af_phrase in af_file:
            af_phrase = af_phrase.strip()
            logger.debug('Importing "%s".', af_phrase)
            try:
                a_word, f_word = what_does_af_stand_for.parse_phrase(af_phrase)
                logger.debug('Got "%s" and "%s".', a_word, f_word)
                models.AWord.objects.create(word=a_word)
                models.FWord.objects.create(word=f_word)
            except what_does_af_stand_for.CouldNotParsePhraseError:
                logger.warning('Could not parse "%s".', af_phrase)
