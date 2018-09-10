types:
boolean:
	true:
		true
		!false
		not false
		identicalObject == identicalObject
		object != differentObject
		number+1 >= number									//ints and floats can be compared with each other
		number >= number
		number <= number
		number <= number+1
	false:
		false
		!true
		not true

number:
	


builtins:
print to console:
	Console.print(string)

print to console and start new line and return carriage:
	Console.println(string)

clear console:
	Console.clear()

if statement:
	if(boolean){
		//stuff
	}
else statement (demo):
	if(boolean){
		//stuff
	}
	else{
		//stuff
	}
else if statement (demo):
	if(boolean){
		//stuff
	}
	elseif(boolean){	//alternatively use `elif` or `else if`
		//stuff
	}
