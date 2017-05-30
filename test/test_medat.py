from os import path
from unittest import TestCase

from me2gpx.medat import load_from_dat_file, make_point, PointSource

HERE = path.dirname(path.abspath(__file__))


class TestMedat(TestCase):

    def test_load_from_dat_file(self):
        with open(path.join(HERE, 'gps_track.dat'), 'rb') as f:
            points = list(load_from_dat_file(f))
        self.assertEqual(len(points), 8064)
        self.assertEqual(points[0].timestamp, 1493487365)
        self.assertEqual(points[0].latitude, 51.2514605)
        self.assertEqual(points[0].longitude, 0.0660154)

    def test_make_point(self):
        dummy = tuple(range(9, 0, -1))
        point = make_point(dummy)
        self.assertEqual(dummy[:8], point[:8])
        self.assertEqual(point.source, PointSource.EWindowsNative)



