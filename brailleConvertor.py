def textToBraille(fileName):
	# ASCII
	asciicodes = [' ','!','"','#','$','%','&','(',')','*','+',',','-','.','/',
			  '0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
			  'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
			  'r','s','t','u','v','w','x','y','z','[','\\',']','^','_']

	# Braille symbols
	brailles = [' ','⠮','⠐','⠼','⠫','⠩','⠯','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
			'⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
			'⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠪','⠳','⠻','⠘','⠸']
	
	# transtab = str.maketrans(''.join(asciicodes), ''.join(brailles)," ")
	translateDict = {}
	for index,chr  in enumerate(asciicodes):
		print(chr,len(chr))
		translateDict[chr] =  brailles[index]
	transtab = str.maketrans(translateDict)
	file = open(fileName,'r')
	file2 = open('braille.txt','w', encoding='utf-16')
	for line in file:
		line = line.lower()
		file2.write(line.translate(transtab))
	file2.close()
		
inputFile = input("enter the file to convert")
textToBraille(inputFile)