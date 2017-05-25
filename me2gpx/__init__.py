import argparse

from medat import load_from_dat_file
from gpx import GPXTrack

def main():
    desc = 'Convert Maps.me gps_track.dat files to GPX format.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('input_file', metavar='IN', help='Input file (Maps.me .dat format)')
    parser.add_argument('output_file', metavar='OUT', help='Output file (GPX format)')
    parser.add_argument('-p', '--pretty-xml', action="store_true", help='Generate pretty XML with indentation')

    args = parser.parse_args()

    with open(args.input_file, 'rb') as inputfile:
        points = load_from_dat_file(inputfile)

    track = GPXTrack(*points)
    with open(args.output_file, 'w') as outputfile:
        track.write(outputfile, pretty=args.pretty_xml)

if __name__ == '__main__':
    main()
