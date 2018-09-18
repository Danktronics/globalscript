filename = "index.gs"
rawText = open(filename, "r").read()
cache = str(rawText)
convertCache = ""

def parseBuiltinConsole(parse):
	if(parse[8:].startswith("print(")):
		return(parse[8:len(parse)-1] + ", end='', flush=True)")
	elif(parse[8:].startswith("println(")):
		return("print(" + parse[16:])

while(len(cache) > 0):
	while(len(cache) > 0 and cache[0] == "\n"):
		cache = cache[1:]
		convertCache = convertCache + "\n"
	
	if(cache.startswith("Console.")):
		cacheNum = 0
		while(cache[cacheNum] != ")"):
			if(cache[cacheNum] == "\n"):
				break #custom exception about how the close paren is missing
			else: cacheNum = cacheNum + 1
		cacheNum = cacheNum + 1
		convertCache = convertCache + parseBuiltinConsole(cache[:cacheNum])
		cache = cache[cacheNum:]
	
	print(str(((len(rawText)-len(cache))/len(rawText))*100) + "% complete.")

print("done, saving...")
open("index.py","w+").write(convertCache)
print("saved to index.py")
print("running globalscript code: \n")
import index
