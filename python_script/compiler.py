import os
import html_gen
from chapter_manager import ChapterManager
from html_manager import HTMLManager

chapters = os.listdir("chapters")
chapters.remove(".DS_Store")
chapters.sort()

html_manager = HTMLManager(chapters)
html_manager.contents()

print(chapters)

which_chapter = input("Czy chcesz skompilować konretny rozdział? Jeśli tak, wpisz jego numer, jeśli nie wpisz 'X'. Zwróć uwagę na format '01', a nie '1'. \n")
if which_chapter == 'X':
	for chapter in chapters:
		chapter_manager = ChapterManager(chapter)
		chapter_manager.generate_pictures()
		html_manager.chapter(chapter)
else:
	chapter_manager = ChapterManager(str(which_chapter))
	chapter_manager.generate_pictures()
	html_manager.chapter(str(which_chapter))


