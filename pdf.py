from pyPdf import PdfFileWriter, PdfFileReader


output = PdfFileWriter()
input1 = PdfFileReader(file("document1.pdf", "rb"))

print ("title = %s" % (input1.getDocumentInfo().title))