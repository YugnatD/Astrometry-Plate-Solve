################################################################################
# Author : Tanguy Dietrich
# Date : 17/09/2021
# Description : Plate solver based on astrometry.net to generate sky-plot
#               image without internet using index files
################################################################################
import lib.PlateSolve as PlateSolve
import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, required=True)
    parser.add_argument('--focale', type=int, required=True)
    parser.add_argument('--photosite', type=float, required=True)
    parser.add_argument('--percent', nargs='?', const=20, type=int, default=20)
    parser.add_argument('--fov', nargs='?', const=5, type=int, default=5)
    parser.add_argument('--star-size', nargs='?', const=9, type=int, default=9)
    parser.add_argument('--downscale', nargs='?', const=2, type=int, default=2)
    args = parser.parse_args()
    toSolve = PlateSolve.PlateSolve(focale=args.focale, photosyte=args.photosite)
    toSolve.solve(args.image)
