from PyPDF2 import PdfFileReader, PdfFileWriter
import PyPDF2
from PyQt5.QtWidgets import QFileDialog
import os

def getNameFile(path):
    return os.path.basename(path)

def combinePDFs(paths):
    '''Given a list of pdf's combine and save them to a new file'''
    pdf_writer = PdfFileWriter()

    for path in paths:
        print(path)
        #Create PDF Reader object
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            #Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    #Get name of save file
    outputName = path[:-4] + ' pdfs-combined.pdf'

    #Write out the merged pdf
    with open(outputName, 'wb') as out:
        pdf_writer.write(out)




def removePass(paths,password):
    '''Remove pass for the given pdfs'''
    for path in paths:
        pdf_reader = PdfFileReader(path)
        restult = pdf_reader.decrypt(password)
        if restult == 0:
            print('Password incorrect!')
            #pop up waring message
        else:
            #Create pdf writer obj
            pdf_writer = PdfFileWriter()
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))
            
            outName = path[:-4] + ' decrypted.pdf'
            
            #write out pdf
            with open(outName, 'wb') as out:
                pdf_writer.write(out)
    



def encrypyPDF(paths, password):
    '''Add password to pdfs'''
    for path in paths:
        pdf_reader = PdfFileReader(path)
        pdf_writer = PdfFileWriter()

        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        pdf_writer.encrypt(user_pwd=password, owner_pwd=None, 
                       use_128bit=True)
        
        outName = path[:-4] + ' encrypted.pdf'

        with open(outName, 'wb') as out:
            pdf_writer.write(out)
        


def addWatermark(paths,watermark):
    '''Add watermark to given pdfs'''
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    for path in paths:
        pdf_reader = PdfFileReader(path)
        pdf_writer = PdfFileWriter()

        for page in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page)
            page.mergePage(watermark_page)
            pdf_writer.addPage(page)

        outName = path[:-4] + ' watermarked.pdf'
        
        with open(outName, 'wb') as out:
            pdf_writer.write(out)





def getTxt(file):
    '''Get txt from given pdf to docx'''
    pageObj = PyPDF2.pdf.PageObject(file)
    text  = pageObj.extractText()

    outName = file[:-4] + '.txt'

    with open(outName, 'wb') as out:
        out.write(text)




def rotatepdf(paths,option):
    '''rotate entire pdf cw or ccw'''
    if option == 'cw':
        for path in paths:
            pdf_reader = PdfFileReader(path)
            pdf_writer = PdfFileWriter()

            for page in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page)
                page.rotateClockwise(90)
                pdf_writer.addPage(page)

            outName = path[:-4] + ' cw.pdf'
            
            with open(outName, 'wb') as out:
                pdf_writer.write(out)

    elif option == 'ccw':
        for path in paths:
            pdf_reader = PdfFileReader(path)
            pdf_writer = PdfFileWriter()

            for page in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page)
                page.rotateCounterClockwise(90)
                pdf_writer.addPage(page)

            outName = path[:-4] + ' ccw.pdf'
            
            with open(outName, 'wb') as out:
                pdf_writer.write(out)

    #process complete popup



def splitpdf(path):
    '''Split by page pdf'''
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        name_of_split = path[:-4]
        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
    
    #process complete popup



def removeWhitePages(file):
    '''remove white pages in an pdf'''
    pass


