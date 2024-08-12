import rawpy
import imageio
import argparse
import sys
import os.path
import pathlib


# Get input and output directories as arguments
parser = argparse.ArgumentParser()
parser.add_argument('inputDir', type=str, nargs=1, help='Location of raw image files')
parser.add_argument('outputDir', type=str, nargs=1, help='Location to output files')
args = parser.parse_args()

# Get list of all files on camera
# Iterate through each, getting the thumbnail version and placing it in the output dir
for imageFile in pathlib.Path(args.inputDir[0]).glob('*.ARW'):

    imageFilePath = str(imageFile)
    filePrefix = pathlib.Path(imageFilePath).stem
    fileOutput = str(os.path.join(args.outputDir[0], filePrefix + '.jpeg'))
    print('Output : ' + fileOutput)

    with rawpy.imread(imageFilePath) as raw:
        thumb = raw.extract_thumb()
   
    if thumb.format == rawpy.ThumbFormat.JPEG:
        with open(fileOutput, 'wb') as f:
            f.write(thumb.data)
    elif thumb.format == rawpy.ThumbFormat.BITMAP:
        imageio.imsave(fileOutput, thumb.data)
