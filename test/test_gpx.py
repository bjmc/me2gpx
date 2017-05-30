from csv import DictReader, QUOTE_NONNUMERIC
from io import StringIO
from os import path
from unittest import TestCase
from unittest.mock import Mock
from xml.etree import cElementTree as ET

from me2gpx.gpx import GPXTrack, NS

HERE = path.dirname(path.abspath(__file__))

class TestGPX(TestCase):

    def setUp(self):
        with open(path.join(HERE, 'points.csv')) as f:
            fields = ('latitude', 'longitude', 'altitude', 'timestamp')
            reader = DictReader(f, fields, quoting=QUOTE_NONNUMERIC)
            self.points = [Mock(**pt) for pt in reader]

    def test_create_gpx_file(self):
        fakefile = StringIO()
        track = GPXTrack(*self.points)
        track.write(fakefile)
        fakefile.seek(0)
        result = ET.parse(fakefile).getroot()
        self.assertEqual(len(result[0][0]), 35)
        







