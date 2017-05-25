from datetime import datetime
from io import StringIO
from xml.etree import cElementTree as ET
from xml.dom import minidom

NS = "http://www.topografix.com/GPX/1/1"

class GPXTrack(object):

    def __init__(self, *points):
        self.root = ET.Element('gpx',
                               creator="me2gpx",
                               version="1.1",
                               xmlns=NS)
        self.trk = ET.SubElement(self.root, 'trk')
        self.track_segment(points)

    def track_segment(self, points):
        if points:
            seg = ET.SubElement(self.trk, 'trkseg')
            for p in points:
                self.point(seg, p)

    def point(self, segment, pnt):
        pt = ET.SubElement(segment, 'trkpt',
                           lat=str(pnt.latitude),
                           lon=str(pnt.longitude))
        ele = ET.SubElement(pt, 'ele')
        ele.text = str(pnt.altitude)
        time = ET.SubElement(pt, 'time')
        dt = datetime.fromtimestamp(pnt.timestamp)
        time.text = dt.isoformat()
        return pt

    def write(self, filehandle, pretty=False):
        if pretty:
            filehandle.write(self.pretty())
        else:
            ET.ElementTree(self.root).write(filehandle, encoding='unicode')

    def pretty(self):
        rough_string = StringIO()
        self.write(rough_string)
        rough_string.seek(0) # Reset to start of string, so minidom can read it...
        reparsed = minidom.parse(rough_string)
        return reparsed.toprettyxml(indent="  ")
