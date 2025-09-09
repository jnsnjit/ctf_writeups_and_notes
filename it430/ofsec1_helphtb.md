# Hack The Box Lab - Help #
in this class I want to really improve my offensive security skills, so I want to up the difficulty of the labs I do!

## Step 1 - IP Enumernation and Fingerprinting ##
```ping 10.10.10.121``` <br>
```nmap 10.10.10.121 -sV -sC``` (get version info and check all ports) <br>

three ports open: <br>
- 22, 80, 3000

__Port 80:__
```curl 10.10.10.121``` <br>
--> says that the website is moved to http://help.htb <br>

try opening in browser, no go ... bc i dont know the domain <br>
* in /etc/hosts, add the address and domain name so the browser knows where to navigate to

Leds to an apache server default page, at this point there is a lot more to do now... 
1. tried directory busting with dirbuster:
``` gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 100 -u http://help.htb ```
after enumerating --> /support and /javascript<br>
1. /javascript can not be accessed, need authentication
2. /support leads to helpdeskz support ticket system, this looks vulr imo

_NEW_ --> try using exploitdb tool searchsploit to find out more about vulnerabilities with a application <br>

``` searchsploit helpdeskz ```
--> version 1.0.2 is vulnerability to RCE ... just need to verify the version the server is running now

