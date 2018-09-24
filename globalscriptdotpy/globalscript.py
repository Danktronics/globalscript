import os
import sys
import math

def parseBuiltinConsole(parse):
	if(parse[8:].startswith("print(")):
		return(parse[8:len(parse)-1] + ", end='', flush=True)")
	elif(parse[8:].startswith("println(")):
		return("print(" + parse[16:])

isPython = True

if(len(sys.argv) == 1): #default if no args are passed, Python will autobrick
	filename = "index.gs"
	outputname = "index.py"
elif(len(sys.argv) == 2): #1 arg is passed
	if(sys.argv[1].endswith(".gs") and os.path.isfile(sys.argv[1])):
		filename = sys.argv[1]
		outputname = sys.argv[1][:3] + ".py"
	elif(os.path.isfile(sys.argv[1])):
		if(input("The specified file isn't a .gs file. Continue anyways? (y/anything else)").startswith("y")):
			filename = sys.argv[1]
			outputname = sys.argv[1][:3] + ".py"
		else:
			sys.exit()
	else:
		open(sys.argv[1], "r") #should throw exception and brick
		sys.exit()
elif(len(sys.argv) == 3): #2 args are passed
	if(sys.argv[1].endswith(".gs") and os.path.isfile(sys.argv[1])):
		filename = sys.argv[1]
	elif(os.path.isfile(sys.argv[1])):
		if(input("The specified input file isn't a .gs file. Continue anyways? (y/anything else)").startswith("y")):
			filename = sys.argv[1]
		else:
			sys.exit()
	else:
		open(sys.argv[1], "r") #should throw exception and brick
		sys.exit()
	
	if(sys.argv[2].endswith(".py") and os.path.isfile(sys.argv[2])):
		outputname = sys.argv[2]
	elif(os.path.isfile(sys.argv[2])):
		if(input("The specified output file isn't a .py file. Continue anyways? (y/anything else)").startswith("y")):
			outputname = sys.argv[2]
			isPython = False
		else:
			sys.exit()
	else:
		open(sys.argv[2], "r") #should throw exception and brick
		sys.exit()
rawText = open(filename, "r").read()
cache = str(rawText)
convertCache = ""

#start parsing
while(len(cache) > 0):
	#goes through newlines. needs to be first
	while(len(cache) > 0 and cache[0] == "\n"):
		cache = cache[1:]
		convertCache = convertCache + "\n"
	
	#parses Console
	if(cache.startswith("Console.")):
		cacheNum = 0
		while(len(cache)>0 and cache[cacheNum]!=")"):	#finds close parenthesis
			if(cache[cacheNum] = '"'):					#for multiline string
				cacheNum = cacheNum + 1
				while(cache[cacheNum] != '"'):
					cacheNum = cacheNum + 1
			
			if(cache[cacheNum] == "\n"):		#quits on newline
				exit()
				#exception about how the close paren is missing
			if(cache[cacheNum:cacheNum+1] == "//"):	#quits on comment
				exit()
				#similar exception to above
			cacheNum = cacheNum + 1
		cacheNum = cacheNum + 1
		killTheNewlines = cache[:cacheNum]
		while("\n" in killTheNewlines)					#also for multiline
			killTheNewlines = killTheNewlines.replace("\n", "\\n")
		convertCache = convertCache + parseBuiltinConsole(killTheNewlines)
		cache = cache[cacheNum:]
	
	#parses comments
	while(cache.startswith("//")):
		cacheNum = 0
		cache = cache[2:]
		convertCache = convertCache + "#"
		while(len(cache) > cacheNum and cache[cacheNum] != "\n"):
			cacheNum = cacheNum + 1
		convertCache = convertCache + cache[:cacheNum]
		cache = cache[cacheNum:]
	
	print(str(math.floor(((len(rawText)-len(cache))/len(rawText))*100)) + "% complete.")

print("done, saving...")
open("index.py","w+").write(convertCache)
print("saved to index.py")
if(isPython or input("Didn't run output file because it isn't a `.py` file. Try anyways? (y/anything else)").startswith("y")):
	print("running output file: \n")
	import index
