from PyPDF2 import PdfFileMerger
#Create a list with the file paths
from os import listdir, path
from os.path import isfile, join


abs_path = path.abspath(path.join(".","pdf_files"))
pdf_files = [path.join(abs_path, f) for f in listdir(abs_path) if isfile(join(abs_path, f))]

#Create an instance of PdfFileMerger() class
merger = PdfFileMerger(strict=False)

#Iterate over the list of the file paths
for pdf_file in pdf_files:
    #Append PDF files
    merger.append(pdf_file)

#Write out the merged PDF file
merger.write("merged_file.pdf")
merger.close()
