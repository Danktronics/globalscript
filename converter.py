filename = "index.gs"
rawText = open(filename, "r").read()
cache = str(rawText)
convertCache = ""

def parseBuiltinConsole(input):
	if(input[8:].startswith("print(")):
		return(input[8:])

while(len(cache) > 0):
	print(str(((len(rawText)-len(cache))/len(rawText))*100) + "% complete.") #print every so often
	while(cache[1:] == "\n"):
		cache = cache[1:]
		convertCache = convertCache + "\n"
	
	if(cache.startswith("Console.")):
		cacheNum = 0
		while(cache[cacheNum] != ")"):
			if(cache[cacheNum] == "\n"):
				break #custom exception about how the close paren is missing
		
			cacheNum = cacheNum + 1
		
		cache = cache + parseBuiltinConsole(cache[:cacheNum])

open("index.py","w+").write(convertCache)
