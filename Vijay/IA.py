from PIL import Image
import pytesseract

def process_image(iamge_name, lang_code):
	return pytesseract.image_to_string(Image.open(iamge_name), lang=lang_code)

def print_data(data):
	print(data)

def output_file(filename, data):
	file = open(filename, "a")
	file.write(data)
	file.close()

def main():
    l = ["D:/IA/page0.jpg","D:/IA/page1.jpg"]
    for x in l:
        data_eng = process_image(x, "eng")
        print_data(data_eng)
        output_file("eng2.txt", data_eng)

if  __name__ == '__main__':
	main()   