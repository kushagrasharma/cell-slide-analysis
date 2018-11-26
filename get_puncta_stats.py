#@String filename
from ij import IJ
from ij.plugin import Duplicator
from loci.plugins import BF

def get_image_paths():
    images = []
    with open(filename, 'r') as f:
        [images.append(file.strip()) for file in f]
    return images

def run_analysis(path):
    img = BF.openImagePlus(path)[0]
    imgDup = img.duplicate()
    #imgDup = img.Duplicator()
    IJ.setAutoThreshold(imgDup, "Default dark no-reset")
    #IJ.run(imgDup, "Threshold...", "")
    #IJ.run(imgDup, "Convert to Mask", "method=Default background=Dark calculate black")    

if __name__ in ['__builtin__','__main__']:
    imagePaths = get_image_paths()
    for path in imagePaths:
        run_analysis(path)
        break
        #img = IJ.openImage(path)
        #imgDup = img.duplicate()

        #IJ.setAutoThreshold(imgDup, "Default dark no-reset")
        #IJ.run(imgDup, "Threshold...")
        #IJ.run(imgDup, "Convert to Mask", "method=Default background=Dark calculate black")

