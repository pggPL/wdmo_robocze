import os
import re
import wand.image
from pdf2image import convert_from_path
from wand.color import Color
from PIL import Image

class ChapterManager:
	def __init__(self, chapter_number):
		self.chapter_number = chapter_number
		self.chapter_path = "../wdmo/chapters/" + chapter_number
		self.pictures_path = "../pictures/" + chapter_number
		self.tex_files_path = "../wtex_files/" + self.chapter_number

		os.system("mkdir ../pictures")
		os.system("mkdir " + self.pictures_path)

		self.theory = self.read_file("theory")
		self.problems = self.read_file("problems")
		self.hint1 = self.read_file("hint1")
		self.hint2 = self.read_file("hint2")
		self.hint3 = self.read_file("hint3")
		self.solutions = self.read_file("solutions")

		os.system("mkdir ../tex_files")
		os.system("mkdir " + self.tex_files_path)



		tex_file = open("../text_templates/tex_start.tex")
		self.tex_start = tex_file.read()
		tex_file.close()


		tex_file = open("../text_templates/tex_end.tex")
		self.tex_end = tex_file.read()
		tex_file.close()	

	def read_file(self, filename):
		file = open(self.chapter_path + "/" + filename + ".tex")
		output = file.read()
		file.close()
		return output

	def write_file(self, filename, text):
		file = open(filename, "w+")
		file.write(text)
		file.close()

	def generate_pictures(self):
		self.generate_pictures_problems()
		self.generate_pictures_theory()
		self.generate_pictures_hint(1)
		self.generate_pictures_hint(2)
		self.generate_pictures_hint(3)
		self.generate_pictures_solutions()


	def generate_pictures_theory(self):
		# podzielić teorię na fragmenty
		parts = self.theory.split("\\heading{")
		self.gen_picture(parts[0], "theory_0")
		i = 1
		parts = parts[1:]
		for part in parts:
			part = "\\heading{" + part
			part =  part 
			self.gen_picture(part, "theory_" + str(i))
			i += 1
		
	def generate_pictures_problems(self):
		parts = self.problems.split("\\begin{problem}")
		parts = parts[1:]
		i = 1
		for part in parts:
			part = part[(part.find("}") + 1):]
			part = part.split("\\end{problem}")[0]
			part =  "\\noindent" + part 
			self.gen_picture(part, "problem_" + str(i))
			i += 1

	def gen_picture(self, tex_code, name):
		regular_expression = "\\\heading\{.*\}"
		to_replace = re.findall(regular_expression, "\\\heading\{abc\}")
		text_code_to_save = tex_code
		if len(to_replace) == 1:
			text_code_to_save = tex_code.replace(to_replace[0], "")

		text_code_to_save = tex_code.replace("\n", "<br>\n")
		text_code_to_save = tex_code.replace("\t", "&nbsp;&nbsp;")
		self.write_file(self.tex_files_path + "/" + name, text_code_to_save)


		tex_code = self.tex_start + tex_code + self.tex_end
		temporary_tex_processing_file = open("temporary_tex_processing_file.tex", "w+")
		temporary_tex_processing_file.write(tex_code)
		temporary_tex_processing_file.close()

		os.system("pdflatex temporary_tex_processing_file.tex >syf")
		os.system("rm temporary_tex_processing_file.log")
		os.system("rm temporary_tex_processing_file.aux")
		os.system("rm temporary_tex_processing_file.out")

		print(name + " generated ")

		
		with wand.image.Image(filename='temporary_tex_processing_file.pdf', resolution=300) as img:
			img.save(filename='temp.png')

		i = 0
		files_to_convert = []
		for file in os.listdir():
			if file.endswith(".png") and len(re.findall("temp", str(file))) > 0:
				files_to_convert.append(str(file))

		files_to_convert.sort()

		if len(files_to_convert) == 1:
			file = files_to_convert[0]
			im = Image.open(file)
			im2 = im.crop((150, 150, im.size[1] - 900, im.getbbox()[3]))
			im2.save(self.pictures_path +  "/" + name + ".png")
			i += 1
			os.system("rm " + file)
		else:
			pic_id = 0
			for file in files_to_convert:
				im = Image.open(file)
				im2 = im.crop((150, 150, im.size[1] - 900, im.getbbox()[3]))
				im2.save(self.pictures_path +  "/" + name + "_" + str(pic_id) + ".png")
				i += 1
				pic_id += 1
				os.system("rm " + file)



	def generate_pictures_hint(self, num):
		if num == 1:
			parts = self.hint1.split("\\item")
		if num == 2:
			parts = self.hint2.split("\\item")
		if num == 3:
			parts = self.hint3.split("\\item")

		parts[-1] = parts[-1].split("\\end{hints_list}")[0]
		
		i = 1
		parts = parts[1:]
		for part in parts:
			part =  "\\noindent \n" + part 
			self.gen_picture(part, "hint" + str(num) + "_" + str(i))
			i += 1

	def generate_pictures_solutions(self):
		parts = self.solutions.split("\\begin{problem}")
		i = 1
		parts = parts[1:]
		for part in parts:
			part = part.split("\\end{problem}")[1]
			part = part 
			self.gen_picture(part, "solution_" + str(i))
			i += 1



