#-HTB 
#-Reversing 
The given ZIP folder had a nested folder with a single executable
- Running strings behind_the_scenes gave some initial insight
	- The program outputs a formatted string with the flag
- Next, inspecting the executable in Ghidra revealed invalid UD2 opcodes 
	- These were manually replaced with NOP
		- NOP is the no-operation code, which does nothing
		- Replacing this allows Ghidra to deconstruct the code further
	- ![[Pasted image 20230819220543.png]]
	- With UD2 removed, we can now see the full code
		- It is comparing the input string with the flag
	- Now we can run the executable with the flag to get the correct output