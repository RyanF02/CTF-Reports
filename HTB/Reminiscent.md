#-HTB
#-Forensics 

We are given an email, a system info document, and a memory dump.

We can run strings memory_dump to get all of the plaintext in the file.

We can see there is a resume.pdf.lnk file that was opened on the computer.

Using a tool called 'volatility' we can scan the memory for information.

Running a file scan reveals resume.pdf.lnk file.

Running strings on the resume.pdf.lnk.dat file shows there is obfuscated power shell code.

Running base64 -d on the encoded string reveals more power shell code.

We can decode the decoded string, for two layers of encryption, to see more plaintext.

In this text we can see a variable $flag=HTB{} and we have solved the challenge.