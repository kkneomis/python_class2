# Module excersices

### Challenge 1

1. Create a package main with an `__init__.py` file
2. Create a module person containing a Person class. 
3. Create a module car contain a Car class.
4. Create a file main.py outside of the package. Import both of your created classes from their respective modules and instantiate them.


### Challenge 2
1. Create a utils module with the following functions:
 *  square() (squares a number)
 *  cube() (cubes a number)
2. Create a main file
 * import the modules you util
 * print the square and cubes of every number from 1 to 100

 
 ## Challenge 3
 
Create a program that will randomly select two numbers from 1-6 (like rolling two dice). Show the dice rolls and end the program UNLESS the program rolls doubles. If the program rolls doubles, then it should roll again, show the new roll and stop UNLESS the program rolls doubles again and so on. But on the third time you roll doubles, you don't get to roll again, on the third time you roll doubles, you go to jail!

The program should print the sum of the rolls and indicate if the user should stop or roll again or go to Jail. See the example output below.

```
User rolls  2  &  6  
Move 8 Spaces and stop  
User rolls  3  &  3  
DOUBLES!  
Move 6 Spaces and roll again getting...  
User rolls 1 & 2
Move 3 Spaces and stop  
User rolls  2  &  2
DOUBLES!
Move 4 Spaces and roll again getting...
User rolls 1 & 1
DOUBLES
Move 2 Spaces and roll again getting...
User rolls 6 & 6
DOUBLES
GO TO JAIL --->
```

You die should be ints own class "Dice" and "dice" module
All you work should be done in the main class