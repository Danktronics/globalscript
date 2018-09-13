# types:

## function (known to Java as a class and to plebs as a module or something):
```
Pirate(){
	//any code that's not in a nested function is like a constructor in Java
	inst arghMatey = 0 					//this is the syntax for making an instance variable
	intensify(arg){						//this is a nested function. usage below
		arghMatey+=arg
	}
	pirateLevel(){						//another nested function
		return arghMatey
	}
}

tSeries = Pirate()						//copies the function into a variable
tSeries.intensify(69)					//adds 69 to the instance variable, see the function
Console.println(tSeries.pirateLevel())	//should print 69
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
awkwardButValid = num 4.8
```
Whether a number is stored in the system as an integer or a floating-point number will be decided by the compiler.

*for those writing compilers:* As a general rule, if the number is an integer mathematically, it should be stored as such.


## builtins:
### print to console:
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

### if statement:
```
if(boolean){
	//stuff
}
```

### else statement (demo):
```
if(boolean){
	//stuff
}
else{
	//stuff
}
```

### else if statement (demo):
```
if(boolean){
	//stuff
}

elseif(boolean){	//alternatively use `elif` or `else if`
	//stuff
}
```
