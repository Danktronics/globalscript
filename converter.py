filename = "index.gs"
rawText = open(filename, r)
cache = str(rawText)
convertCache = ""
progress = (len(rawText)-len(cache))/len(rawText) #progress should always be this equation

def parseBuiltinConsole(input):
	if(input[8:].startswith("print(")):
		return(input[8:])

print(str(progress*100) + "% complete.") #print every so often

while(len(cache) > 0):
	while(cache[1:] == "\n"):
		cache = cache[1:]
		convertCache = convertCache + "\n"
	
	if(cache.startswith("Console.")
		cacheNum = 0
		while(cache[cacheNum] != ")"):
			if(cache[cacheNum] == "\n"):
				break #custom exception about how the close paren is missing
		
			cacheNum++
		
		cache = cache + parseBuiltinConsole(cache[:cacheNum])
