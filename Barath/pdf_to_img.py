# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
images = convert_from_path('D:/IA/q.pdf',500)

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')

	
# new method - currently using
import pypdfium2 as pdfium

pdffile = 'MailAttachments/QUOTATION 6680 [ KOTHARI SUGAR & CHEMICAL 19B ]511.pdf'


def main():

    # render multiple pages concurrently (in this case: all)
    for image, suffix in pdfium.render_pdf_topil(pdffile):
        image.save('output_%s.jpg' % suffix)

    # render a single page (in this case: the first one)
    with pdfium.PdfContext(pdffile) as pdf:
        image = pdfium.render_page_topil(pdf, 0)
        image.save('output.jpg')
    
