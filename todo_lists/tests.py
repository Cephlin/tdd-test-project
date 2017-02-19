# pylint: disable=C0111
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from todo_lists.views import homepage


class HomePageTest(TestCase):

    # pylint: disable=C0103
    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_homepage_returns_correct_html(self):
        request = HttpRequest()
        response = homepage(request)
        expected_html = render_to_string('base.html')
        self.assertEqual(response.content.decode(), expected_html)
