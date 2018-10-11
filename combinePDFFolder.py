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

fileDir = os.path.dirname(os.path.realpath(__file__))
for root, dirs, files in os.walk(fileDir):
    merger = PdfFileMerger()
    print root, dirs, files
    # Loop through all the files
    try:
        if (file != '.git'):
            for fileName in files:
                if fileName.endswith(".pdf"):
                    print "file name is/are: " + fileName
                    filePath = os.path.join(root, fileName)
                    #open each pdf file and append it
                    merger.append(open(fileName, 'rb'))
            newPDFPath = os.path.join(fileDir, filePath + ".pdf")
            merger.write(newPDFPath)

    except:
        print  'You have a git file or a .idea file '


