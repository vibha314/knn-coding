Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
>>> data = json.load(open(r"C:\Users\DELL-PC\Downloads\pydictproblem-master\pydictproblem-master\data.json"))
>>> def translate (w):
	if w in data :
		return data[w]

	
>>> word = input("Enter word: ")
Enter word: bird
>>> print(translate(word))
['Any of the bipedal, warm-blooded vertebrates that lay eggs having wings which, for most species, enables them to fly.', 'A powered heavier-than-air aircraft with fixed wings that obtains lift by the Bernoulli effect and is used for transportation.', 'Badminton equipment consisting of a ball of cork or rubber with a crown of feathers.']
>>> 