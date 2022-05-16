# ТЕСТИРОВАНИЕ в PYTHON

def full_name(first, last, middle=''):
	""" Отдает полное имя и фамилию пользователя"""
	if middle:
		full = first + ' ' + last + ' ' + middle
	else:
		full = first + ' ' + last
	return full.title()

