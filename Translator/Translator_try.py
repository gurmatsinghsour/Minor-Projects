from translate import Translator

try:
	with open('translate.txt',mode='r') as text:
		new_text = text.read()
		print("This is the text before translation\n")
		print(new_text)
except FileNotFoundError as err:
	print("Text file not found")
	raise err
except IOError as err:
	print("IO error")
	raise err

print('''
	1. English
	2. Japan
	3. Korean
	4. PT
	5. Zh
	6. Zh-TW
	7. Exit\n''')

loop = True

while loop == True:	
	
	lang = int(input("Select the language that you want to input from the selected options: "))

	if lang == 1:
		translator = Translator(to_lang="en")
		translated = translator.translate(new_text)
		print(translated)
		print("*\n"*8)
		with open("translated.txt",mode = 'w') as translatedtext:
			mynewtranslatedtext = translatedtext.write(translated)

		


	elif lang == 2:
		translator = Translator(to_lang="ja")
		translated = translator.translate(new_text)
		print(translated)
		print("*\n"*8)		
		with open("translated.txt",mode = 'w') as translatedtext:
			mynewtranslatedtext = translatedtext.write(translated)

        

	elif lang == 3:
		translator = Translator(to_lang="ko")
		translated = translator.translate(new_text)
		print(translated)
		print("*\n"*8)
		with open("translated.txt",mode = 'w') as translatedtext:
			mynewtranslatedtext = translatedtext.write(translated)
		
		
	

	elif lang == 4:
		translator = Translator(to_lang="pt")
		translated = translator.translate(new_text)
		print(translated)
		print("*\n"*8)
		with open("translated.txt",mode = 'w') as translatedtext:
			mynewtranslatedtext = translatedtext.write(translated)	
       	
       	


	elif lang == 5:
		translator = Translator(to_lang="zh")
		translated = translator.translate(new_text)
		print(translated)
		print("\n************************\n"*8)
		with open("translated.txt",mode = 'w') as translatedtext:
			mynewtranslatedtext = translatedtext.write(translated)
       	


	elif lang == 6:
		translator = Translator(to_lang="zh")
		translated = translator.translate(new_text)
		print(translated)
		print("*\n"*8)
		with open("translated.txt",mode = 'w') as translatedtext:
			mynewtranslatedtext = translatedtext.write(translated)
		


	elif lang == 0:
		print("Hey, Don't type 0 DUMBO")

	elif lang == 7:
		loop = False
		









