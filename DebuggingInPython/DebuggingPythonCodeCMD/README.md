# OVERVIEW
pdb is a command line debugger for Python applications

The Debugged application needs to add small amount of code

Commands:
* Display values of variables
* Control the execution of the debugged application
* Set and clear breakpoints
* Conditional breakpoints
* Enabling and disabling breakpoints

Evaluate python expressions in a pdb session

## Before debugging with the pdb debugger
* import the pdb module(included in the python standard library)
* call the set_trace() function in the pdb module
* the import and set_trace() call are ofthen placed on the same line
* Separate multiple python statements with a semicolon to put them on one line
* PEP-8 discourages this practice, but in this case it's often overlooked

## Using the pdb debugger
* Invoke the application using the Python Interpreter
* Execution will pause at the line after the set_trace() call
* the pdb command prompt will appear in the terminal

## pdb commands
* help(alias h) - get a list of available commands
* Pass the name of a command to _help_ to get instructions for that command
* p(short for print) - display the value of a variable
* pp(short for pretty print) - format and display complex values(ie. dictionaries)
* next(alias n) - execute until the following line of code(similar to 'step over')
* continue(alias c & cont) - resume execution until the next breakpoint or until the application exits
* quit(alias q) - quit the debugger and abort the application being debugged
* exit - same as quit

## Demo: Debugger our Application
Import pdb and add set_trace method
```python
def get_investment_info(investment):
    name = investment["name"]
    quantity = investment["quantity"]
    import pdb; pdb.set_trace()
    current_price = get_current_price(name)
    print(f"The current value of your {quantity} {name} is {current_price*quantity}")
```
run app in command line, it will be paused in the line in which the import and set_trace were called
```bash
$ python app.py 
> /workspaces/python_learning/DebuggingInPython/DebuggingPythonCodeCMD/app.py(16)get_investment_info()
-> current_price = get_current_price(name)
# type p command and variable name to print the variable value
(Pdb) p name
'Bitcoin'
(Pdb) p quantity
0.5
# if we print current_price variable for example, it is going to fail because it was not yet executed
(Pdb) p current_price
*** NameError: name 'current_price' is not defined
# To execute the next sentence type next
(Pdb) next
Getting current price for Bitcoin
> /workspaces/python_learning/DebuggingInPython/DebuggingPythonCodeCMD/app.py(17)get_investment_info()
-> print(f"The current value of your {quantity} {name} is {current_price*quantity}")
(Pdb) p current_price
10000
# type continue to go to the next execution, and check the variable values of next iteration
(Pdb) continue
The current value of your 0.5 Bitcoin is 5000.0
> /workspaces/python_learning/DebuggingInPython/DebuggingPythonCodeCMD/app.py(16)get_investment_info()
-> current_price = get_current_price(name)
(Pdb) p name
'Ethereum'
```
another way of include pdb is call to _breakpoint()_ method, this doesnt require importing pdb

## Commands for managing breakpoints
* break(alias b)
* if no argument is included list all breakpoints
* To set a breakpoint, provide a line number or function as the first argument
* The line number or function can be preceded with a filename
* The second argument is a conditional; the breakpoint is ignored if the expression evaluates to False.
* clear(alias cl) - remove one or more breakpoints
* if no arguments is included remove all breakpoints
* to remove a specific breakpoint, provide a line number or breakpoint number as the first argument
* The line number can be preceded with a file name

## Breakpoints in action
start the app and execute commands
```bash
$  python app.py 
> /workspaces/python_learning/DebuggingInPython/DebuggingPythonCodeCMD/app.py(17)get_investment_info()
-> current_price = get_current_price(name)
(Pdb) break
# The break output is empty since we didnt create breakpoints yet
# Set breakpoint in the line 2 and note the creation
(Pdb) break 2
Breakpoint 1 at /workspaces/python_learning/DebuggingInPython/DebuggingPythonCodeCMD/app.py:2
(Pdb) break
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at /workspaces/python_learning/DebuggingInPython/DebuggingPythonCodeCMD/app.py:2
# if we continue, the execution will be moved to the above method
(Pdb) c
> /workspaces/python_learning/DebuggingInPython/DebuggingPythonCodeCMD/app.py(2)get_current_price()
-> print(f"Getting current price for {coin}")
# and we can check the variables of this method
(Pdb) p coin
'Bitcoin'
```