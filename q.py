from sikuli import *
import os

def findPattern(filename):
	filename =  filename + ".png"
	print "access:", os.access(filename,os.R_OK) 
	if os.access(filename ,os.R_OK) == False:
		f = capture("Please outline the pattern you wish to search for")
		os.rename(f,filename )
	m = find(filename )
	print m


findPattern("cows")
		

