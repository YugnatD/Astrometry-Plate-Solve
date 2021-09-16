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
    args = parser.parse_args()
    toSolve = PlateSolve.PlateSolve(focale=args.focale, photosyte=args.photosite)
    toSolve.solve(args.image)
