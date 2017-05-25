# Adapted from https://gist.github.com/lambdaupb/21bfa917292d45c9b4fef4964799b3d4

from collections import namedtuple
import struct
from enum import Enum

# Global values, might change if maps.me modifies their format.
POINT_PATTERN = '<ddddddddB'
POINT_PACK_SIZE = struct.calcsize(POINT_PATTERN)
HEADER_SIZE = 4

class PointSource(Enum):
	EAppleNative=0
	EWindowsNative=1
	EAndroidNative=2
	EGoogle=3
	ETizen=4
	EPredictor=5

Point = namedtuple("Point", ('timestamp',
							 'latitude',
							 'longitude',
							 'altitude',
							 'speed',
							 'bearing',
							 'horizontalAccuracy',
							 'verticalAccuracy',
							 'source')

		)

def make_point(raw_point):
	return Point(*raw_point[:-1], source=PointSource(raw_point[-1]))


def load_from_dat_file(filehandle):
	data_input = filehandle.read()
	data_len = len(data_input) - HEADER_SIZE
	start = HEADER_SIZE
	end = HEADER_SIZE + (POINT_PACK_SIZE *data_len) // POINT_PACK_SIZE
	raw_points = data_input[start:end]
	return map(make_point, struct.iter_unpack(POINT_PATTERN, raw_points))
		


