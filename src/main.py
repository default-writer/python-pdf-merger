from PyPDF2 import PdfFileMerger

#Create an instance of PdfFileMerger() class
merger = PdfFileMerger()

#Create a list with the file paths
pdf_files = ['pdf_files/file1.pdf', 'pdf_files/file2.pdf']

#Iterate over the list of the file paths
for pdf_file in pdf_files:
    #Append PDF files
    merger.append(pdf_file)

#Write out the merged PDF file
merger.write("merged_file.pdf")
merger.close()