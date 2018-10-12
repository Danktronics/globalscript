globalscript is a programming language designed to be universal. C is to Python as Python is to globalscript. Hopefully. ;)

# types:

## function (known to plebs as a module or something):
```
pirateLevel = 0
function pirate(num arg){			//putting number forces any inputted variable to be a number the same way setting a default argument does (like in the type definition below) but also requires a number to be inputted. This is optional
	pirateLevel+=arg
	return("Success!")
}

pirate(69)						//adds 69 to the instance variable, see the function
Console.println(pirateLevel)	//should print 69
```

## custom types (classes):
```
class Pirate(boost=1){				//a class can take
	//any code that's not in a nested function is like a constructor in Java
	inst pirateLevel = 0 			//this is the syntax for making an instance variable. Instance variables can be accessed as an attribute of the class as well.
	intensify(number arg){			
		pirateLevel+=(boost*arg)
	}
}

tSeries = Pirate(boost=2)
tSeries.intensify(34.5)
Console.println(tSeries.pirateLevel)		//should print 69
```
Custom types allow variables to store almost anything.

## booleans:
	
### true:
```
true
!false
not false
identicalObject == identicalObject
object != differentObject
number+1 >= number	//ints and floats can be compared with each other
number >= number
number <= number
number <= number+1
```

### false:
```
false
!true
not true
```


## number:
```
number = 9
temp = 2.4
awkwardButValid = num(4.8)
```
Whether a number is stored in the system as an integer or a floating-point number will be decided by the compiler.

*for those writing compilers:* As a general rule, if the number is an integer mathematically, it should be stored as such.

## string:
```
string = "hello there"
multilineString = "hello there.
Java is irrelevant.
resistance is futile."
```
Strings can be multiline ;)
If you don't like this, you can use \n to signify a new line, similar to other languages.


# libraries:
These libraries should work as specified in any compiler.
*to compiler writers: 👀*

## JSON:

The JSON builtin should help because JSON is:

1. Widely used

2. that's about it actually

The builtin library only supports name/value pairs.

Assume the following for the entire JSON section:
```
example = '{"a": "1", "b": "2", "c": "3"}'
```


### `JSON.convertToJSON()`:
This will convert arrays to JSON.
```
example2 = JSON.convertToJSON(example)
//returns [["a", "1"], ["b", "2"], ["c", "3"]]
```

### `JSON.convertFromJSON()`:
This will convert JSON to arrays.
```
JSON.convertFromJSON(example2)
//returns '{"a": "1", "b": "2", "c": "3"}'
```

## builtins:

### `Builtins.platform`:
The constant variable platform in the builtins (`builtins.platform`) should give JSON info in a string in the following format:
```
{"codePlatform": "Python",
"os": "nt",
"dir": "/home/david/code/"}
```
Before you complain, there is a builtin JSON parser, so like, stop complaining. Zip it.
In Python, the name of the OS should be obtained from os.name.

## console:

### `Console.print()`:
```
Console.print(string)
```

### print to console and start new line and return carriage:
```
Console.println(string)
```

### clear console:
```
Console.clear()
```

## logic

### if statement:
```
boolean = true
if(boolean){
	//stuff runs
}
```

### else statement (demo):
```
boolean = false
if(boolean){
	//stuff doesn't run
}
else{
	//stuff runs
}
```

### else if statement (demo):
```
boolean = false
if(boolean){
	//stuff doesn't run
}

else if(not boolean){
	//stuff runs
}
```

### while loop:
```
boolean = true
while(boolean){
	//stuff runs until boolean == false
}
```
An infinite loop should be possible on all platforms. If the platform a compiler is running on doesn't like this (Dear Javascript: 👀) the compiler should implement a workaround that will allow a forever loop.
