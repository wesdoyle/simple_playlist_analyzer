import argparse
from matplotlib import pyplot as plt
import plistlib
import numpy as np


def plotYearHisto(fileName):
    """
    Plot year histogram using XML playlist from iTunes.
    """
    plist = plistlib.readPlist(fileName)
    tracks = plist['Tracks']
    years = []
    for trackId, track in tracks.items():
        try:
            years.append(track['Year'])
        except:
            pass

    if years == []:
        print("Playlist file does not contain valid track year data.")
        return

    x = np.array(years)
    f, ax = plt.subplots()
    ax.plot()
    ax.hist(x, bins=20, color='midnightblue')
    ax.set_title('Song Year Histogram for %s' % fileName)
    plt.show()


def main():
    descStr = """
    This program creates a histogram of track year from an XML playlist files
    exported from iTunes.
    """
    parser = argparse.ArgumentParser(description=descStr)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--years', dest='plFile', required=False)

    args = parser.parse_args()

    if args.plFile:
        plotYearHisto(args.plFile)
    else:
        print("Try again")

if __name__ == '__main__':
    main()
