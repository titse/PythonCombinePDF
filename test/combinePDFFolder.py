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

# fileDir = os.path.dirname(os.path.realpath(__file__))
# for root, dirs, files in os.walk(fileDir):
#     merger = PdfFileMerger()
#     print root, dirs, files
#     # Loop through all the files
#     try:
#         if (file != '.git'):
#             for fileName in files:
#                 if fileName.endswith(".pdf"):
#                     print "file name is/are: " + fileName
#                     filePath = os.path.join(root, fileName)
#                     #open each pdf file and append it
#                     merger.append(open(fileName, 'rb'))
#             newPDFPath = os.path.join(fileDir, filePath + ".pdf")
#             merger.write(newPDFPath)
#
#     except:
#         print  'You have a git file or a .idea file '

#
fileDir = os.path.dirname(os.path.realpath(__file__))
file_list = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f))]
print file_list
print "Your file directory is: " + fileDir
for root, dirs, files in os.walk(fileDir, topdown=True):
    # current folder: root
    # list of filenames in that folder: files
    # list of subdirectories in that folder: dirs
    merger = PdfFileMerger()
    print "The files to merge are:"
    print files
    print root
    print "dirs: " + str(dirs)


    for directoryIndex in dirs:
        print "directory index: "
        print directoryIndex
        for filename in files:
            print "file name is: " + filename
            if filename.endswith(".pdf"):
                print "file names: " + filename
                filepath = os.path.join(root, filename)
                print "Your file path to append to is: " + filepath
                # with open(filepath)
                merger.append(PdfFileReader(open(filepath, 'rb')))
                print "merger is: "
                print merger
                #merger.write(str(filename))
                # write file path of the sub folder
                # test folder name is: pdf_to_merge
                print "what is dirs"
                print dirs
            else:
                print "Error we have a folder!"
        merger.write(os.path.join(fileDir, directoryIndex + '.pdf'))
