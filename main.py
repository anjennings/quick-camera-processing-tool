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

print(args.inputDir[0])
print(args.outputDir[0])

'''
if not os.path.isdir(args.inputDir[0]):
    print('Invalid input dir')
    sys.exit()
   
# Create dir instead?
if not os.path.isdir(args.outputDir[0]):
    print('Invalid input dir')
    sys.exit()'''

# Get list of all files on camera
# Iterate through each, getting the thumbnail version and placing it in the output dir
for imageFile in pathlib.Path(args.inputDir[0]).glob('*.ARW'):

    imageFilePath = str(imageFile)
    filePrefix = pathlib.Path(imageFilePath).stem
    fileOutput = str(os.path.join(args.outputDir[0], filePrefix + '.jpeg'))
    print('Input : ' + imageFilePath)
    print('Output : ' + fileOutput)

    with rawpy.imread(imageFilePath) as raw:
        thumb = raw.extract_thumb()
   
    if thumb.format == rawpy.ThumbFormat.JPEG:
        # thumb.data is already in JPEG format, save as-is
        with open(fileOutput, 'wb') as f:
            f.write(thumb.data)
    elif thumb.format == rawpy.ThumbFormat.BITMAP:
        # thumb.data is an RGB numpy array, convert with imageio
        imageio.imsave(fileOutput, thumb.data)


'''
path = 'testpic.ARW'
with rawpy.imread(path) as raw:
    thumb = raw.extract_thumb()
   
if thumb.format == rawpy.ThumbFormat.JPEG:
    # thumb.data is already in JPEG format, save as-is
    with open('thumb.jpeg', 'wb') as f:
        f.write(thumb.data)
elif thumb.format == rawpy.ThumbFormat.BITMAP:
    # thumb.data is an RGB numpy array, convert with imageio
    imageio.imsave('thumb.png', thumb.data)
    '''