# Password Generator V1.0
# Made By Kryzsec

from random import randint
_MIN_ = 8
_MAX_ = 32

charset = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plength = randint(_MIN_,_MAX_)
password = ""
for i in range(0,plength):
	password = password + charset[randint(0,len(charset)-1)]

print password
