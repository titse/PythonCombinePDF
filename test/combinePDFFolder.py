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
        pdfToMerge = [pdfIndex for pdfIndex in os.listdir(dirIndex) if pdfIndex.endswith(".pdf")]
        for pdfFiles in pdfToMerge:
            filepath = os.path.join(workingDirectory, dirIndex)
            mergedFile = os.path.join(filepath, pdfFiles)
            merger.append(PdfFileReader(open(mergedFile, 'rb')))

        with open(os.path.join(workingDirectory, dirIndex + '.pdf'), "wb") as fout:
            merger.write(fout)

        merger.close()
