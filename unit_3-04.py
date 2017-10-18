#created by Matthew Walsh
#created on october2017
#created for ICS3U
#this program will check if a year is a leap year

import ui

def check_year_button(sender):
	#input
	year = int(view['year_textfield'].text)
	#process
	if((year % 100) == 0):
		if((year % 400) == 0):
			view['answer_label'].text = str(year) + " is a leap year"
		else:
			view['answer_label'].text = str(year) + " is not a leap year"
	elif((year % 4) == 0):
		view['answer_label'].text = str(year) + " is a leap year"
	else:
		view['answer_label'].text = str(year) + " is not a leap year"

view = ui.load_view()
view.present('full_sheet')
