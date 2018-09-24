def findNext(n, string):
	temp = 0
	while(not string[temp:temp+len(n)] == n):
		temp = temp + 1
	return temp

def hArray(input):
	horizontalArray(input)

def horizontalArray(input):
	inputCache = input
	output = []
	while(!inputCache.startswith("{") and inputCache != ""):
		inputCache = inputCache[1:]
	inputCache = inputCache[1:]
	
	while('}' in inputCache):
		output.append([])
		while(!inputCache.startswith('"') and inputCache != ""):
			inputCache = inputCache[1:]
		inputCache = inputCache[1:]
		findNext('"', inputCache)
		
	