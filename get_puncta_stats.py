#@String directory
from ij import IJ, WindowManager
from ij.plugin import Duplicator, Thresholder
from loci.plugins import BF
import os

def get_image_paths():
    files = os.listdir(directory)
    files = [f.strip() for f in files]
    files = [f for f in files if f[-4:]=='.oib']
    return files

def run_analysis(img_name):
    path = directory + img_name
    results_dir = directory + "Results/"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    img = BF.openImagePlus(path)[0]
    imgDup = img.duplicate()
    #imgDup = img.Duplicator()
    imgDup.show()
    IJ.setAutoThreshold(imgDup, "Default dark no-reset")
    # IJ.run(imgDup, "Threshold...", "")
    # IJ.run(imgDup, "Convert to Mask", "method=Default background=Dark calculate black")    
    # IJ.run(imgDup, run("Close-", "stack"))
    IJ.run(imgDup, "Set Measurements...", "area mean min display  decimal=3")
    IJ.run("Analyze Particles...", "size=2-Infinity circularity=0.15-1.00 display clear stack")
    IJ.saveAs("Results", results_dir + img_name + "_results.csv")
    IJ.selectWindow("Results")
    IJ.run("Close")
    img.close()
    imgDup.close()

if __name__ in ['__builtin__','__main__']:
    if directory[-1] != '/':
        directory += '/'
    imagePaths = get_image_paths()
    for path in imagePaths:
        run_analysis(path)
        
    IJ.run("Quit")

