from csv import DictReader, QUOTE_NONNUMERIC
from datetime import datetime
from io import StringIO
from os import path
from unittest import TestCase
from unittest.mock import Mock
from lxml import etree


from me2gpx.gpx import GPXTrack, NS

HERE = path.dirname(path.abspath(__file__))

class TestGPX(TestCase):

    def parser_and_points(self):
        with open(path.join(HERE, 'gpx1.1.xsd')) as f:
            schema_root = etree.parse(f)
        schema = etree.XMLSchema(schema_root)
        # This parser will validate that the XML satisfies the GPX schema
        self.xmlparser = etree.XMLParser(schema=schema)

        with open(path.join(HERE, 'points.csv')) as f:
            fields = ('latitude', 'longitude', 'altitude', 'timestamp')
            reader = DictReader(f, fields, quoting=QUOTE_NONNUMERIC)
            self.points = [Mock(**pt) for pt in reader]

    def assert_matches(self, csv_points, xml_points):
        for csv_pt, xml_pt in zip(csv_points, xml_points):
            self.assertEqual(str(csv_pt.latitude), xml_pt.get('lat'))
            self.assertEqual(str(csv_pt.longitude), xml_pt.get('lon'))
            self.assertEqual(str(csv_pt.altitude), xml_pt[0].text)
            xml_dt = datetime.strptime(xml_pt[1].text, "%Y-%m-%dT%H:%M:%S")
            csv_dt = datetime.fromtimestamp(csv_pt.timestamp)
            self.assertEqual(xml_dt, csv_dt)

    def test_create_gpx_file(self):
        self.parser_and_points()
        fakefile = StringIO()
        track = GPXTrack(*self.points)
        track.write(fakefile)
        fakefile.seek(0)
        result = etree.parse(fakefile, self.xmlparser).getroot()
        self.assertEqual(len(result[0][0]), 35)
        self.assert_matches(self.points, result[0][0])


    def test_create_pretty_gpx_file(self):
        self.parser_and_points()
        fakefile = StringIO()
        track = GPXTrack(*self.points)
        track.write(fakefile, pretty=True)
        fakefile.seek(0)
        result = etree.parse(fakefile, self.xmlparser).getroot()
        self.assertEqual(len(result[0][0]), 35)
        self.assert_matches(self.points, result[0][0])
        fakefile.seek(0)
        for lineno, line in enumerate(fakefile):
            if 1 < lineno < 146:
                self.assertTrue(line.startswith(' '))




