import re
import os

def file_number(file):
	int_str = ""
	for c in file:
		if c.isdigit():
			int_str += c
	return int(int_str)


class HTMLManager:
	def __init__(self, chapters):
		self.chapters = chapters
		self.chapters_path = "./chapters/"
		self.chapters_names = []
		for chapter in chapters:
			text = self.read_file(self.chapters_path + chapter + "/theory.tex")
			text = text.split("\\theory{")[1]
			text = text.split("}")[0]
			self.chapters_names.append(text)


	def contents(self):
		contents_start = self.read_file("contents_start")
		contents_end = self.read_file("contents_end")
		output = contents_start
		chapter_number = 1
		for chapter_name in self.chapters_names:
			output += '<div>\n'
			output += '<a href = "./chapters_html/' +  self.chapters[chapter_number - 1] +'.html" class = "chapter_link">' + str(chapter_number) + '. ' + chapter_name + '</a>\n'
			output += '</div>\n'
			chapter_number += 1
		output += contents_end
		contents_file = open("contents.html", "w+")
		contents_file.write(output)
		contents_file.close()

	def generate_sort_number_from_filename(self, filename):
		numbers = filename.split('_')[1:]
		if len(numbers) == 1:
			return 100 * int(numbers[0].split('.')[0])
		else:
			return 100 * int(numbers[0]) + int(numbers[1].split('.')[0])

	def chapter(self, chapter):
		chapter_start = self.read_file("chapter_start")
		chapter_end = self.read_file("chapter_end")
		output = chapter_start

		files_in_folder = os.listdir("pictures/" + chapter)
		theory_files = []
		problems_files = []
		for file in files_in_folder:
			if file.startswith("theory"):
				theory_files.append(file)
			elif file.startswith("problem"):
				problems_files.append(file)
		# tu jest problem

		theory_files.sort(key=self.generate_sort_number_from_filename)
		problems_files.sort(key=self.generate_sort_number_from_filename)

		output += '<script> var chapter = "' + chapter + '" </script>'

		for file in theory_files:
			output += '<div class = "page_content">\n'
			output += '<img src="' + "../pictures/" + chapter + "/" + file + '" class = "page_image" ondblclick = "show_tex(\''+ chapter + "/" + file.replace("png", "tex") + '\')" >\n'
			output += '</div>\n\n'

		problem_number = 1
		for file in problems_files:
			output += '<div class = "problem_title">\n'
			output += 	'Zadanie ' + str(problem_number) + '\n'
			output += '</div>\n'
			output += '<div class = "problem_box">\n'
			output += '<img src="../pictures/' + chapter + '/problem_' + str(problem_number) + '.png" ondblclick = "show_tex(\''+ chapter + "/" + file.replace("png", "tex") + '\')" width="800px">'
			output += """<br><br>
			<input type="button" id="{0}_hint1" class = "problem_button" value = "Podpowiedź 1" onclick = "clicked('{0}', 'hint1')">
			<input type="button" id="{0}_hint2" class = "problem_button" value = "Podpowiedź 2" onclick = "clicked('{0}', 'hint2')">
			<input type="button" id="{0}_hint3" class = "problem_button" value = "Podpowiedź 3" onclick = "clicked('{0}', 'hint3')">
			<input type="button" id="{0}_solution" class = "problem_button" value = "Rozwiązanie" onclick = "clicked('{0}', 'solution')">
			</div>\n\n""".format(problem_number)

			output += '<div id = "below_problem_{0}" class = "below_problem">\n\n'.format(problem_number)
				
			output += '</div>\n\n'
			problem_number += 1
			


		output += chapter_end
		os.system("mkdir chapters_html")
		contents_file = open("chapters_html/" + chapter + ".html", "w+")
		contents_file.write(output)
		contents_file.close()

	def read_file(self, filename):
		file = open(filename)
		output = file.read()
		file.close()
		return output