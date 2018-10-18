# combinePDF.py
# Author: Tiffany Tse
# Date: Oct 09,2018
# Updated: Oct 10, 2018
# Description: Combining pdf within sub-folders
# Dependencies: os, pyPDF2

import sys
import os
import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader


workingDirectory = os.path.dirname(os.path.realpath(__file__))
for root, dirs, files in os.walk(workingDirectory):
    merger = PdfFileMerger()
    for dirIndex in dirs:
        for filename in files:
            if filename.endswith(".pdf"):
                filepath = os.path.join(root, filename)
                merger.append(PdfFileReader(open(filepath, 'rb')))
                print dirIndex
            merger.write(os.path.join(workingDirectory, dirIndex + '.pdf'))
