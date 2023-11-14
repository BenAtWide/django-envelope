# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
Signals sent by the application.
"""

from django.dispatch import Signal

# Providing args has been removed, but they were message and form
# for both these signals.
before_send = Signal()
after_send = Signal()
