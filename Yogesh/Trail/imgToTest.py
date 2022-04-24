from PIL import Image
import pytesseract


def process_image(image_name, lang_code):
    return pytesseract.image_to_string(Image.open(image_name), lang=lang_code)


def print_data(data):
    print(data)


def output_file(filename, data):
    file = open(filename, "a")
    file.write(data)
    file.close()


# def main():
#     l = ["D:/IA/page0.jpg", "D:/IA/page1.jpg"]
#     for x in l:
#         data_eng = process_image(x, "eng")
#         print_data(data_eng)
#         output_file("eng2.txt", data_eng)


import pypdfium2 as pdfium

pdffile = 'MailAttachments/QUOTATION 6680 [ KOTHARI SUGAR & CHEMICAL 19B ]511.pdf'


def main():
    # render multiple pages concurrently (in this case: all)
    try:
        for image, suffix in pdfium.render_pdf_topil(pdffile):
            image.save('output_%s.jpg' % suffix)
    except Exception as e:
        print(e)

main()
# if __name__ == '__main__':
#     main()