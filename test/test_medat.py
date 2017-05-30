from os import path
from unittest import TestCase

import environ

from me2gpx.medat import load_from_dat_file, make_point, PointSource

HERE = path.dirname(path.abspath(__file__))

class TestMedat(TestCase):

    def test_load_from_dat_file(self):
        with open(path.join(HERE, 'gps_track.dat'), 'rb') as f:
            points = list(load_from_dat_file(f))
        self.assertEqual(len(points), 20)
        self.assertEqual(points[0].timestamp, 0)
        self.assertEqual(points[0].latitude, 0)
        self.assertEqual(points[0].longitude, 0)

    def test_make_point(self):
        dummy = tuple(range(9, 0, -1))
        point = make_point(dummy)
        self.assertEqual(dummy[:8], point)
        self.assertEqual(dummy[8], PointSource.EWindowsNative)



