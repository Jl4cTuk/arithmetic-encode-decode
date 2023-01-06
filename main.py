import os
from collections import Counter

def compress(file):

	filein = open(file, 'r')
	s = filein.read()

	dict = {}
	for ch, freq in Counter(s).items():
		dict[ch] = freq

	print(dict)
	
	f = open("enc", 'w')
	f.write(s)
	f.close()

def decompress(file):

	filein = open(file, 'r')
	s = filein.read()
	
	f = open("dec", 'w')
	f.write(s)
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

if __name__ == "__main__":
	main()