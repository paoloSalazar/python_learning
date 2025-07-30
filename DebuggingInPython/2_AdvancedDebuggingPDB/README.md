# ADVANCED DEBUGGING WITH PDB AND FRIENDS
## Overview
Commands to navigate the source
* Step in
* Step out
* Moving through the stack trace
Read the stack trace

Additional tools to help debug Python code

## Commands for navigating the source
* Step(alias s) - Similar to "Step into" in other debuggers
* Up(alias u) - move up in the stack trace(similar to "step out")
* Down(alias d) - move down in the stack trace
* Both **up** and **down** default to 1 level


## Demo
```bash
python app.py 
> /workspaces/python_learning/DebuggingInPython/2_AdvancedDebuggingPDB/app.py(33)get_investment_info()
-> current_price = get_current_price(name)
# By typing step, this is going to move to the called function
(Pdb) step
--Call--
> /workspaces/python_learning/DebuggingInPython/2_AdvancedDebuggingPDB/app.py(13)get_current_price()
-> def get_current_price(coin):
# type next to move over the method
(Pdb) next
> /workspaces/python_learning/DebuggingInPython/2_AdvancedDebuggingPDB/app.py(14)get_current_price()
-> print(f"Getting current price for {coin}")
# here you can use the p(print) command to check function variable values
(Pdb) p coin
'Bitcoin'
# Add break point and continue
Pdb) break 16
Breakpoint 1 at /workspaces/python_learning/DebuggingInPython/2_AdvancedDebuggingPDB/app.py:16
(Pdb) continue
> /workspaces/python_learning/DebuggingInPython/2_AdvancedDebuggingPDB/app.py(16)get_current_price()
-> price = get_bitcoin_price()
# If you try to check values from executed method, they are not present since the stack trace is now in the get_bitcoin_price
(Pdb) p price
*** NameError: name 'price' is not defined

```

## Commands for Navigating the Stack trace
* bt/where (alias w) - print the current stack trace
* the frames are displayed vertically from oldest to newest
* angle bracket reference the current frame
* Thin arrow references the current line in each frame
* list(l) Display lines around the current line or range of lines
* long list(ll) Display the code for the current function or frame

Common pdb commands:

n (next): Execute the next line
s (step): Step into a function call
c (continue): Continue execution until next breakpoint
l (list): Show current location in code
p variable_name: Print variable value
h (help): Show command list
q (quit): Exit debugger

Up Command

Alias: u
Purpose: Moves up in the stack trace (towards older frames)
Default: Moves up 1 level
Usage: up [count]

Down Command

Alias: d
Purpose: Moves down in the stack trace (towards newer frames)
Default: Moves down 1 level
Usage: down [count]

When debugging:

Use bt or where to see the stack trace
Use up to move to the caller's frame
Use down to move back to the called frame
Use p locals() to inspect variables in the current frame
Remember: The stack trace displays frames from oldest (bottom) to newest (top), and the current frame is marked with angle brackets

## Tools to help you debug your code
* Pylint
* ipdb

## Demo:
pyling
```bash
# Install pylint using pip
$ pip install pyling
# run pyling with source file
$ pylint app.py
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:27:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 8.00/10 (previous run: 7.19/10, +0.81)
```

ipdb
```bash
# install ipdb and ipython
$ pip install ipdb ipython
# Run app
$ python app.py 
> /workspaces/python_learning/DebuggingInPython/2_AdvancedDebuggingPDB/app.py(32)get_investment_info()
     31     # breakpoint()
---> 32     current_price = get_current_price(name)
     33     print(f"The current value of your {quantity} {name} is {current_price*quantity}")
ipdb> where
  /workspaces/python_learning/DebuggingInPython/2_AdvancedDebuggingPDB/app.py(43)<module>()
     41 
     42     for investment in portfolio:
---> 43         get_investment_info(investment)
> /workspaces/python_learning/DebuggingInPython/2_AdvancedDebuggingPDB/app.py(32)get_investment_info()
     31     # breakpoint()
---> 32     current_price = get_current_price(name)
     33     print(f"The current value of your {quantity} {name} is {current_price*quantity}")
# Now run ipython
$ ipython
Python 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.4.0 -- An enhanced Interactive Python. Type '?' for help.
Tip: The `%timeit` magic has a `-o` flag, which returns the results, making it easy to plot. See `%timeit?`.

In [1]:

# set a breakpoint
In [1]: %debug --breakpoint app.py:19
Breakpoint 1 at /workspaces/python_learning/DebuggingInPython/2_AdvancedDebuggingPDB/app.py:19
NOTE: Enter 'c' at the ipdb>  prompt to continue execution.

#Run app
In [2]: %run app.py
> /workspaces/python_learning/DebuggingInPython/2_AdvancedDebuggingPDB/app.py(32)get_investment_info()
     31     # breakpoint()
---> 32     current_price = get_current_price(name)
     33     print(f"The current value of your {quantity} {name} is {current_price*quantity}")
ipdb> break
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at /workspaces/python_learning/DebuggingInPython/2_AdvancedDebuggingPDB/app.py:19
ipdb> continue
Getting current price for Bitcoin
Checking the blockchain...
The current value of your 1.3 Bitcoin is 13000.0
> /workspaces/python_learning/DebuggingInPython/2_AdvancedDebuggingPDB/app.py(32)get_investment_info()
     31     # breakpoint()
---> 32     current_price = get_current_price(name)
     33     print(f"The current value of your {quantity} {name} is {current_price*quantity}")
```