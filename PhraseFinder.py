startPoint = input("Starting point:\n")
startPoint = startPoint.split(":")
ID = startPoint[0]
FileName = startPoint[1]
phraseLength = int(startPoint[2])
word = ""
newPhrase = ""
file = open(FileName,'r')

for i in range(phraseLength):
	for line in file:
		line = line.split(":")
		if line[0] == ID:
			word = line[1]
			FileName = line[2]
			if "\n" in line[3]:
				ID = line[3][:-1]
			else:
				ID = line[3]
			file.close()
			file = open(FileName,'r')
			newPhrase += word + " "
			break

print(newPhrase )
