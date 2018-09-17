filename = "index.gs"
rawText = open(filename, r)
cache = str(rawText)
convertCache = ""
progress = (len(rawText)-len(cache))/len(rawText) #progress should always be this equation

print(str(progress*100) + "% complete.") #print every so often

while(len(cache) > 0):
	pass
