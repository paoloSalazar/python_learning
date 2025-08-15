# Debugging Python Code with Visual Studio Code
## Setup VS Code for python debugging
Commands are out, UI is in
* Run and debug from inside of Visual Studio Code
* Manage breakpoints
* Inspect Variables
* Step through code
* Read the call stack
* Evaluate watch expressions
* Use the debug console

## Debugging in Visual Studio Code
* Python extension for Visual Studio Code
* Run and Debug Python code from inside of Visual Studio Code
* No additional code needed to start the debugger
### Commands are so pdb
* Run and debug panel
* Manage breakpoints and inspect variables
* View a lot of information at once that updates in real time
* Debug toolbar

## Demo
install the python extension for VSCode and then add a break point in the code
![Set Breakpoint](img/set_breakpoint.png)
Then choose debug option
![Select Debugger](img/select_debugger.png)
Check the left panel
![Variables Panel](img/variables_panel.png)

## Managing Breakpoints in Visual Studio Code
* Enabling, disabling and removing breakpoints
* Conditional breakpoints 
* Debugging exceptions

### Stepping through code
The step over, in and out functions are triggered with buttons in VSCode

### Inspecting Application State
* Continued use of the variables and call stack in the Run and Debug Panel
* Watch expressions
* Debug Console

## Demo
If you add a new breakpoint check the breakpoint left panel
![BreakPoint](img/breakpoints.png)

By pressing continue button the stack will skip to the next breakpoint
When we uncheck a breakpoint it is displayed as gray and disabled in the editor section

To Show breakpoints in the overview ruler open user preferences and check this option
![Overview Ruler](img/overview_ruler.png)

For conditional breakpoints edit the break points and add rule
![Conditional Breakpoints](img/conditional_breakpoints.png)

## Demo 2
Working in the __refactored__ folder.
Note you need to run debug from app.py file

Setup a breakpoint in __portfolio__ class in summarize method
![Setupbreakpoint](img/setupbreakpoint.png)

Once you reach the code for function call press Step Into (F10) button to jump to method definition
![alt text](img/stepintobutton.png)

To return to breakpoint location press StepOut Button (F11)

Let's check the watch section now.
this section is util because you can insert a python expression to check values.
it is useful when __variables__ section is populated too much
You can add a new expression by pressing plus button

![watchSection](img/watchsection.png)

Also you can use the __Debug Console__ to type variables or python expressions to check the values
Note you need to change to __<module>__ to access to more global variables
![DebugConsole](img/debugconsole.png)
