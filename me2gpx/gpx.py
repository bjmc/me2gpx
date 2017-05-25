# Adapted from openxc-python http://python.openxcplatform.com
# Copyright (c) 2012-2014 Ford Motor Company

from xml.etree import ElementTree as ET

class GPXEncoder(object):
    def __init__(self, points):
        self.root = ET.Element("gpx")
        track = ET.SubElement(self.root, "trk")
        number = ET.SubElement(track, "number")
        number.text = "1"
        self.segment = ET.SubElement(track, "trkseg")
        for point in points:
            self.add_point(point)

    def output(self):
        root = ET.ElementTree(self.root).getroot()
        return ET.tostring(root, encoding="unicode")

    def add_point(self, point):
        xmlpoint = ET.SubElement(self.segment, "trkpt")
        xmlpoint.set('lat', str(point.latitude))
        xmlpoint.set('lon', str(point.longitude))
