from PyPDF2 import PdfFileMerger
#Create a list with the file paths
from os import listdir, path
from os.path import isfile, join
import img2pdf
from PIL import Image
import os
import io

abs_path = path.abspath(path.join(".","pdf_files"))
pdf_files = [path.join(abs_path, f) for f in listdir(abs_path) if isfile(join(abs_path, f))]

merger = PdfFileMerger(strict=False)

for pdf_file in pdf_files:
    if pdf_file.endswith(".jpg") or pdf_file.endswith(".jpg"):
        image = Image.open(pdf_file)
        pdf_bytes = img2pdf.convert(image.filename)
        file = open(join(abs_path, os.path.splitext(os.path.basename(pdf_file))[0]) + ".pdf", "wb")
        file.write(pdf_bytes)
        image.close()
        file.close()
        pdf_file = file.name
    merger.append(pdf_file)
merger.write("merged_file.pdf")
merger.close()
