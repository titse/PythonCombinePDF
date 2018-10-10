# combinePDF.py
# Author: Tiffany Tse
# Date: Oct 09,2018
# Updated: Oct 10, 2018
# Description: Combining pdf locally
# Dependencies: os, pyPDF2

import os
from PyPDF2 import PdfFileMerger

# Directory of the where script and py are located
fileDir = os.path.dirname(os.path.realpath(__file__))
print "This is fileDir: " + fileDir

#pdf get tall the pdfs to merge
pdfToMerge = [pdfIndex for pdfIndex in os.listdir(fileDir) if pdfIndex.endswith(".pdf")]
print "The files to merge are:"
print pdfToMerge
merger = PdfFileMerger()

for pdf in pdfToMerge:
    merger.append(open(pdf, 'rb'))

with open("result.pdf", "wb") as fout:
    merger.write(fout)
    merger.close()

print "Done!"