# types:

## function (known to Java as a class and to plebs as a module or something):
```
Pirate(){
	//any code that's not in a nested function is like a constructor in Java
	inst pirateLevel = 0 					//this is the syntax for making an instance variable. Instance variables can be accessed as an attribute of the function
	intensify(arg){						//this is a nested function. usage below
		pirateLevel+=arg
	}
}

tSeries = Pirate()						//copies the function into a variable (in Java this would be creating a new object of class Pirate)
tSeries.intensify(69)						//adds 69 to the instance variable, see the function
Console.println(tSeries.pirateLevel)	//should print 69
```
Yes. For real. None of that Java suffering. Functions and types are one thing. Obviously some functions won't do anything interesting when used as a type. If you want, you can follow Java convention and make your type names start with an uppercase letter and your function names start with a lowercase letter, but the compiler shouldn't care what you do, and should treat them as the same.


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
Assume the following for the entire JSON section:
```
example = '{"a": "1", "b": "2", "c": "3"}'
```

### `JSON.verticalArray()`:
*aliased as JSON.vArray(), they are one and the same*
This will return the JSON names (if they exist) in one array, and the values in another. If the JSON string is an object, it will return a set of values.
```
JSON.verticalArray(example)
/*returns:
[["a", "b", "c"], ["1", "2", "3"]]
*/
```

### `JSON.horizontalArray()`:
*aliased as JSON.hArray(), they are one and the same*
This will return the JSON names and values in an array for each ordered pair. If the JSON string is an object, it will return a set of values.
```
JSON.horizontalArray(example)
/*returns:
[["a", "1"], ["b", "2"], ["c", "3"]]
*/
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
