from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
build_exe_options = {"includes":["chardet"]}

def convert(fname,pages=None):
    if not pages:
        pagenums=set()
    else:
        pagenums=set(pages)
    output=StringIO()
    manager=PDFResourceManager()
    converter=TextConverter(manager,output,laparams=LAParams())
    interpreter=PDFPageInterpreter(manager,converter)

    infile=open(fname,'rb')
    for page in PDFPage.get_pages(infile,pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text=output.getvalue()
    output.close
    return text


def convertMultiple(pdfDir,txtDir):
    for pdf in os.listdir(pdfDir):
        fileExtension=pdf.split(".")[-1]
        if fileExtension=="pdf":
            pdfFilename=pdfDir+pdf
            text=convert(pdfFilename)
            textFilename=txtDir+pdf.split(".")[0]+".txt"
            textFile=open(textFilename,"w")
            textFile.write(text)
pdfDir="C:/Users/NIKHIL/Downloads/pdf/"
txtDir="C:/Users/NIKHIL/Downloads/pdf/"
convertMultiple(pdfDir,txtDir)
