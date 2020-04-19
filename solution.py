Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
>>> from difflib import get_close_matches
>>> data = json.load(open(r"C:\Users\DELL-PC\Downloads\pydictproblem-master(1)\pydictproblem-master\data.json"))
>>> def translate(w):
	if w in data:
		return data[w]
	else:
		print("incorrect typed word,did you mean from the following:")
		print(get_close_matches(w,list(data)))
		## for the close matches of the input word
		choose = input("type the correct word from the list:")
		return data[choose.lower()]

	
>>> word = input("Enter word: ")
Enter word: BIRDO
>>> print(translate(word.lower()))
incorrect typed word,did you mean from the following:
['bird', 'bid', 'libido']
type the correct word from the list:bid
['Availability to sell goods or services for a certain price and under certain conditions.', 'To top the standing bid at an auction.', 'An offer or proposal for goods and/or services submitted in response to a government agency’s invitation.', 'To invoke upon (e.g. farewell, a nice evening, etc.).']
>>> 