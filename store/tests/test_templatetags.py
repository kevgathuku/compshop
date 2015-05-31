from django.template import Context, Template
from django.test import SimpleTestCase


class MakeRangeTest(SimpleTestCase):
    def test_make_range_filter(self):
        out = Template(
            "{% load store_extras %}"
            "{{4|make_range}}"
        ).render(Context())
        self.assertEqual(out, "range(0, 4)")

    def test_make_range_filter_output(self):
        out = Template(
            "{% load store_extras %}"
            "{% for star in 3|make_range %}"
            "Hello"
            "{% endfor %}"
        ).render(Context())
        self.assertMultiLineEqual(
            out,
            'HelloHelloHello')

    def test_make_range_filter_raises_error_on_invalid_input(self):
        render = lambda t: Template(t).render(Context())
        self.assertRaises(TypeError, render,
                          "{% load store_extras %}{{'Error'|make_range}}")
