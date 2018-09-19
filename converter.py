filename = "index.gs"
rawText = open(filename, "r").read()
cache = str(rawText)
convertCache = ""
import sys

def parseBuiltinConsole(parse):
	if(parse[8:].startswith("print(")):
		return(parse[8:len(parse)-1] + ", end='', flush=True)")
	elif(parse[8:].startswith("println(")):
		return("print(" + parse[16:])

#start parsing
while(len(cache) > 0):
	while(len(cache) > 0 and cache[0] == "\n"):			#goes through newlines
		cache = cache[1:]
		convertCache = convertCache + "\n"
	
	if(cache.startswith("Console.")):					#parses Console
		cacheNum = 0
		while(len(cache)>0 and cache[cacheNum]!=")"):	#finds close parenthesis
			if(cache[cacheNum] == "\n"):				#quits on newline
				exit() #exception about how the close paren is missing
			if(cache[cacheNum:cacheNum+1] == "//"):		#quits on comment
				exit() #similar exception to above
			cacheNum = cacheNum + 1
		cacheNum = cacheNum + 1
		convertCache = convertCache + parseBuiltinConsole(cache[:cacheNum])
		cache = cache[cacheNum:]
	
	while(cache.startswith("//")):
		cacheNum = 0
		cache = cache[2:]
		convertCache = convertCache + "#"
		while(len(cache) > 0 and cache[cacheNum] != "\n"):
			cacheNum = cacheNum + 1
		convertCache = convertCache + cache[:cacheNum]
		cache = cache[cacheNum:]
	
	print(str(((len(rawText)-len(cache))/len(rawText))*100) + "% complete.")

print("done, saving...")
open("index.py","w+").write(convertCache)
print("saved to index.py")
print("running globalscript code: \n")
import index
