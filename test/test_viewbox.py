from __future__ import print_function

import unittest

from svgelements import *


class TestElementViewbox(unittest.TestCase):

    def test_viewbox_incomplete_transform(self):
        v = Viewbox({'viewBox': None, 'height': None, 'width': None})
        self.assertEqual(v.transform(), '')
        v = Viewbox({'viewBox': None, 'height': 200, 'width': None})
        self.assertEqual(v.transform(), '')
        v = Viewbox({'viewBox': None, 'height': None, 'width': 200})
        self.assertEqual(v.transform(), '')
        v = Viewbox({'viewBox': None, 'height': 200, 'width': 200})
        self.assertEqual(v.transform(), '')
        v = Viewbox({'viewBox': '0 0 100 100', 'height': None, 'width': None})
        self.assertEqual(v.transform(), '')
        v = Viewbox({'viewBox': '0 0 100 100', 'height': 100, 'width': None})
        self.assertEqual(v.transform(), '')

    def test_viewbox_incomplete(self):
        v = Viewbox({'viewBox': None, 'height': None, 'width': None})
        self.assertEqual(v.element_width, None)
        self.assertEqual(v.element_height, None)
        self.assertEqual(v.viewbox_width, None)
        self.assertEqual(v.viewbox_height, None)
        v = Viewbox({'viewBox': None, 'height': 200, 'width': None})
        self.assertEqual(v.element_width, None)
        self.assertEqual(v.element_height, 200)
        self.assertEqual(v.viewbox_width, None)
        self.assertEqual(v.viewbox_height, 200)
        v = Viewbox({'viewBox': None, 'height': None, 'width': 200})
        self.assertEqual(v.element_width, 200)
        self.assertEqual(v.element_height, None)
        self.assertEqual(v.viewbox_width, 200)
        self.assertEqual(v.viewbox_height, None)
        v = Viewbox({'viewBox': None, 'height': 200, 'width': 200})
        self.assertEqual(v.element_width, 200)
        self.assertEqual(v.element_height, 200)
        self.assertEqual(v.viewbox_width, 200)
        self.assertEqual(v.viewbox_height, 200)
        v = Viewbox({'viewBox': '0 0 100 100', 'height': None, 'width': None})
        self.assertEqual(v.element_width, None)
        self.assertEqual(v.element_height, None)
        self.assertEqual(v.viewbox_width, 100)
        self.assertEqual(v.viewbox_height, 100)
        v = Viewbox({'viewBox': '0 0 100 100', 'height': 100, 'width': None})
        self.assertEqual(v.element_width, None)
        self.assertEqual(v.element_height, 100)
        self.assertEqual(v.viewbox_width, 100)
        self.assertEqual(v.viewbox_height, 100)

        v = Viewbox({'viewBox': None, 'height': '200in', 'width': '200in'})
        self.assertEqual(v.element_width, '200in')
        self.assertEqual(v.element_height, '200in')
        self.assertEqual(v.viewbox_width, '200in')
        self.assertEqual(v.viewbox_height, '200in')
        v.render(ppi=1)
        self.assertEqual(v.element_width, 200)
        self.assertEqual(v.element_height, 200)
        self.assertEqual(v.viewbox_width, 200)
        self.assertEqual(v.viewbox_height, 200)

        v = Viewbox({'viewBox': '0 0 100 100', 'height': '200in', 'width': '200in'})
        self.assertEqual(v.element_width, '200in')
        self.assertEqual(v.element_height, '200in')
        self.assertEqual(v.viewbox_width, 100)
        self.assertEqual(v.viewbox_height, 100)
        v.render()
        self.assertEqual(v.element_width, '200in')
        self.assertEqual(v.element_height, '200in')
        self.assertEqual(v.viewbox_width, 100)
        self.assertEqual(v.viewbox_height, 100)
        self.assertRaises(ValueError, v.transform)
        v.render(ppi=1.0)
        self.assertEqual(v.transform(), 'scale(2, 2)')

    def test_viewbox_simple(self):
        v = Viewbox({'viewBox': '0 0 100 100', 'height': 100, 'width': 100})
        self.assertEqual(v.transform(), '')

    def test_viewbox_scale(self):
        v = Viewbox({'viewBox': '0 0 100 100', 'height': 200, 'width': 200})
        self.assertEqual(v.transform(), 'scale(2, 2)')

    def test_viewbox_translate(self):
        v = Viewbox({'viewBox': '-50 -50 100 100', 'height': 100, 'width': 100})
        self.assertEqual(v.transform(), 'translate(50, 50)')
