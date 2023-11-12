#-Forensics
#-HTB 

We are given a zipped folder.
Inside is two files that we can see.
	One is the bot, and the other is the config file.

![[Pasted image 20230901085920.png]]

In config I noticed there was a dictionary.
	In the dictionary, the token said it was "replaced" for security reasons.

![[Pasted image 20230901085827.png]]

Next, I checked the directory for ==*hidden files*== on the CLI with ==*ls- a*==.
There was a hidden .git directory present.
Inside the git directory there were many files.

![[Pasted image 20230901085740.png]]

The most important was the logs file.
In this file, we can ==*show commits*== made to the project with ==*git log*==
We can see a commit with the same message about the key.

![[Pasted image 20230901090030.png]]

To show this commit, I used the ==*git show -log id*== command.
Here we can see the security token that was replaced for security reasons.

![[Pasted image 20230901090143.png]]

Lastly, the flag was not accepted in the current form.
I tried decoding it with ==*echo flag | base64 -d*== and it was successful.
This was the current flag.

---

Key Takeaways:
Check for the .git directory in a project folder.
Look for log in information clues in config files and commit messages.
Use the information you currently have.
Simple decoding can be done from the CLI.
