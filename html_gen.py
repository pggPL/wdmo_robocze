import os
import re
import wand.image
from pdf2image import convert_from_path
from wand.color import Color
from PIL import Image

def generate_html_theory(tex):
	file_prefix = """
		<!DOCTYPE html>
	<html>
	<head>
		<meta charset="UTF-8">
		<title> Wstęp do matematyki olimpijskiej </title>
		<link rel="style/css" href="style.css">
	</head>
	<body> """

	text_to_be_processed = """
\\input{preamble}
\\begin{document}""" + tex + """
\\end{document}"""


	temporary_tex_processing_file = open("temporary_tex_processing_file.tex", "w+")
	temporary_tex_processing_file.write(text_to_be_processed)
	temporary_tex_processing_file.close

	os.system("pdflatex temporary_tex_processing_file.tex")

	
	with wand.image.Image(filename='temporary_tex_processing_file.pdf', resolution=300) as img:
		img.save(filename='temp.png')

	i = 0
	files_to_convert = []
	for file in os.listdir():
		if file.endswith(".png") and len(re.findall("temp-[0-9]*.png", str(file))) > 0:
			files_to_convert.append(str(file))

	files_to_convert.sort()

	for file in files_to_convert:
		print(i)
		im = Image.open(file)
		im.size  # (364, 471)
		im.getbbox()  # (64, 89, 278, 267)
		im2 = im.crop(im.getbbox())
		im2.size  # (214, 178)
		im2.save("out" + str(i) + ".png")
		i += 1
				    
	

	middle = tex
		
	file_suffix = """</body>
	</html>"""


	os.system("rm temporary_tex_processing_file.aux")
	os.system("rm temporary_tex_processing_file.log")
	os.system("rm temporary_tex_processing_file.out")

	return file_prefix + middle + file_suffix
