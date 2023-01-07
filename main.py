import os
from collections import Counter

def compress(file):

	filein = open(file, 'r')
	s = filein.read()
	
	dict = {}
	p = []
	list = ""
	for ch, freq in Counter(s).items():
		dict[ch] = freq
		p.append(dict[ch]/len(s))
		list+=ch

	top = 1
	bottom = 0
	for ch in s:
		a = top - bottom
		new_top = list.find(ch)
		for i in range(new_top): 
			bottom = bottom + a*p[i]
		top = bottom + a*p[new_top]

	
	#запись
	f = open("enc", 'wb')
	f.write(len(dict).to_bytes(2,'big'))
	for ch in dict:
		f.write(ch.encode())
		f.write(dict[ch].to_bytes(2, 'big'))
	print(len(dict), dict)
	f.close()

def decompress(file):

	filein = open(file, 'rb')

	dictlen = int.from_bytes(filein.read(2), 'big')
	dict = {}
	for i in range(dictlen):
		a = str(filein.read(1).decode())
		b = int.from_bytes(filein.read(2), 'big')
		dict[a] = b
	print(dictlen, dict)
	
	#запись
	f = open("dec", 'wb')
	f.close()

def take_file():
	file = input("input file:\n")
	if os.path.exists(file):
		return file
	else:
		exit("file not found")

def main_menu():
	option = input("choose option: [c]ompress/[d]ecompress\n")
	if option == 'c':
		file = take_file()
		compress(file)
	elif option == 'd':
		file = take_file()
		decompress(file)
	else:
		exit("wrong option")

def main():
	#main_menu()
	compress("txt")
	decompress("enc")

if __name__ == "__main__":
	main()