#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `modtest` package."""


import unittest

from modtest import modtest


class TestModtest(unittest.TestCase):
    """Tests for `modtest` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.message = "Hello"

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test1(self):
        """Test something."""
        output = modtest.hello()
        assert(output == self.message)
