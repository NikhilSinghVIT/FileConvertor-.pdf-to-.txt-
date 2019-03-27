from tkinter import *
from tkinter import filedialog
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
build_exe_options = {"includes":["chardet"]}

class convertor(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.get_widgets()


    def get_widgets(self):
        self.instruction1=Label(self,text="CHOOSE ANY PDF FILE")
        self.instruction1.grid(row=0,column=0,columnspan=2,sticky=W)

        self.button=Button(self,text="CHOOSE THE FILE",command=self.getfile)
        self.button.grid(row=1,column=0,sticky=W)

        self.button2=Button(self,text="CHOOSE THE DESTINATION",command=self.savefile)
        self.button2.grid(row=3,column=0,sticky=W)

        self.button3=Button(self,text="CONVERT TO TEXT",command=self.translate)
        self.button3.grid(row=5,column=0,sticky=W)

    def getfile(self):
        self.filename=filedialog.askopenfilename(initialdir="/",title="select a file",filetype=(("pdf files","*.pdf"),("all files","*.*")))
        self.display=Label(self,text=self.filename)
        self.display.grid(row=2,column=0,sticky=W)
        
    def savefile(self):
        self.savedir=filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
        self.display2=Label(self,text=self.savedir)
        self.display2.grid(row=4,column=0,sticky=W)

        
    def translate(self):
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


        def convertx(pdfDir,txtDir):
            
            fileExtension=pdfDir.split(".")[-1]
            if fileExtension=="pdf":
                pdfFilename=pdfDir
                text=convert(pdfFilename)
                textFilename=txtDir+".txt"
                textFile=open(textFilename,"w")
                textFile.write(text)

        pdfDir=self.filename
        txtDir=self.savedir
        print('/'.join(pdfDir.split('/')[:-1])+'/')
        print(txtDir)
        convertx(pdfDir,txtDir)

        

root=Tk()
root.title("FILE CONVERTOR")
root.geometry("300x300")
app=convertor(root)
root.mainloop()
                                                 

