


import PyPDF2
import os


if(os.path.isdir("temp") == False):
    os.mkdir("temp")
    
txtpath = ""
pdfpath = ""



pdfpath = input("Enter the name of your pdf file ")   
txtpath = input("Enter the name of your txt file ")   

BASEDIR = os.path.realpath("temp") 
print(BASEDIR)


if(len(txtpath) == 0):
    txtpath = os.path.join(BASEDIR,os.path.basename(os.path.normpath(pdfpath)).replace(".pdf", "")+".txt")
pdfobj = open(pdfpath, 'rb')

pdfread = PyPDF2.PdfFileReader(pdfobj)

x = pdfread.numPages


for i in range(x):
    pageObj = pdfread.getPage(i)
    with open(txtpath, 'w+',encoding="utf-8") as f: 
        f.write((pageObj.extractText()))
    print(pageObj.extractText()) 
                                    
    
    

pdfobj.close()  


