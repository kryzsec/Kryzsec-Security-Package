# Password Generator V1.0
# ToDo
# >Add statements to allow us of symbols
# >Add dictionary for word based passwords
# >Add security options for password generation
# >Add ability to set min and max as command line arguments
# >Add a graphical interface
#	This is free to use and to modify and release, just please give credit where credit is due...

from random import randint
import sys
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_min_ = 8
_max_ = 32
version = "V1.0.1"

def _main_(dmin, dmax):
	_Min_ = dmin
	_Max_ = dmax
	arg = []
	if len(sys.argv)==1:
		password = generate_password(_Min_, _Max_, alphabet)
	else:
		for i in range(1,len(sys.argv)):
			arg.append(sys.argv[i])
		if "-h" in arg:
			help(sys.argv[0])
			return 0;
		if "-min" in arg:
			_Min_ = int(arg[arg.index("-min")+1])
		if "-max" in arg:
			_Max_ = int(arg[arg.index("-max")+1])
		if "--v" in arg:
			print version
		if "-v" in arg:
			print version
			print "Verbose Mode [Enabled]"
			generate_password_verbose(_Min_,_Max_, alphabet)
			return 0;
		password = generate_password(_Min_, _Max_, alphabet)
	return;

def generate_password(minl, maxl, charset):
	password = ""
	length = randint(minl, maxl)
	for i in range(0,length):
		password = password + charset[randint(0,len(charset)-1)]
	print password
	return password;

def help(nme):
	print "Usage: " + nme + " <options>"
	print "Leave options blank for default password generation\n"
	print "-min	Set Minimum password length (default 8)"
	print "-max	Set Maximum password length (defult 32)"
	print "-h	Displays Help"
	print "-v	Enables Verbose Mode (implies --v)"
	print "--v	Displays Version"
	return 0;

def generate_password_verbose(minl, maxl, charset):
	password = ""
	print "Minimum length: " + str(minl)
	print "Maximum length: " + str(maxl)
	print "Generating password length"
	length = randint(minl, maxl)
	print "Password length [" + str(length) + "]"
	print "Generating each password character!"
	for i in range(0,length):
		nextchar = charset[randint(0,len(charset)-1)]
		print "Password character " + str(i+1) + " is " + nextchar
		password = password + nextchar
	print "Printing Password: " + password
	print "Finished."
	return password;

_main_(_min_, _max_)
