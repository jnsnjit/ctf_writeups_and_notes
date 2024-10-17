## investigating windows: tryhackme ##
remoting in to a comprimised windows machine with *RDP*
- think of tools like remote in

cool that tryhackme has this all integrated into there website for free!
ok machine is booted up...
lots of initial questions such as
1. year and version of machine <br>
ok using search functionality, opened about section in windows, some info on the machine:
- windows server 2016 database
- version 1607
- os build: 14393.2791
- part of an organizational workgroup, *WORKGROUP*
- pcname: EC2AMAZ-I8UHO76

*man this computer is messed up* 💀 *cmd keeps popping up with text i cant read*
2. last logged in user <br>
*its us, which is administrator user*
**checked by opening control panel>user accounts>user accounts>manage accounts**

3. when did john last log in: <br>
better place to look then step two, just open event view>windows logs>security--> check audits 
sike i lied, use cmd instead, no gui requirement
net user (name:John)         gives base info about user obj, including last logon date
**03/02/2019 5:48:32 PM** 

4. what IP does sys connect to when first starting (domain?) <br>
**ok less certain where to go now, brainstorm time:**

recall windows server database 2016, think it is part of some domain (AD)
probable address is the domain controller.
not netstat sigh 🤧
damn this one silly i am coming back to this question later

5. what two accounts have administrator priv: <br>
WOAH, found this issue right here, guest acc (domain guest), has admin priv, defo not right
**Jenny, Guest**

6. name of scheluded task that is malicous? <br>
ok, going to check task scheluder
    **clean file system**

7. what file is the process trying to start? <br>
**nc.ps**
one quick lookup is all it took to see a nasty github repo
aptsimulator/toolset/nc.ps1
provide data to be sent as soon as connection is established 💀

ok well its interesting to see the administrator denied the request last time it tried to run, which was not when I was on the machine...

8. what port did this file listen to? <br>
**port 1348**
did a quick sanity check with netstat -a to see if it was a currently running process. NO

9. when did jenny last logon <br>
**never?**     interesting thats the answer.
bc why then is there a password set and change?
answer to number 10
10. when did the comprimise happen? <br>
**03/02/2019**

GOING TO LEAVE OFF HERE FOR TONIGHT, WILL CONTINUE TMR! 💯💯
ill add some images next time too..

ok coming back to the challenge now, first thing i thought to check today was not one of the question but the local policies set on the computer:

answer to that: nothing. even though in the past it was 