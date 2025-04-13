## event-viewing picoctf challenge ##
**Category**: forensics (logging, analysis, alerts, events)
**Difficulty**: medium
**Tools**: windows event viewer, notepad ... 
**Date**: 4/11/25
**Attachments**: ...

step1: first look <br>
total events captured... over 8,000. <br>
prior information: One of the employees at your company has their computer infected by malware! Turns out every time they try to switch on the computer, it shuts down right after they log in. The story given by the employee is as follows:
- They installed software using an installer they downloaded online
- They ran the installed software but it seemed to do nothing
- Now every time they bootup and login to their computer, a black command prompt screen quickly opens and closes and their computer shuts down instantly.

things of note. its a company computer, be aware of potentials events for AD and other SMB controlling protocols. additionally, initial payload comes from an installer downloaded online. <br>

first goal, find installed program.<br>
event ID's to look for: 11707, 4697    <br>

boom part one --> first event ID for 11707 is an install for "Totally Legit Software", and after looking at some of the events around this point, there is...<br>
[filename](picoeventchall1.png)

in the xml data of the event, there is this oddly sus info in the data segment, looks like base64 encoded, type to pull out the good ole cyberchef<br>
yup! ---> picoCTF{Ev3nt_vi3wv3r_ <br>

step 2: find out what the installed program is doing... <br>
for this step, I cant say that I can immediately start by sorting by event ID's, not sure what this program wants to do, but it definitly creates some type of persistence on the windows machine, so maybe looking for registry changes might be a good start, but not sure if events are created for that (probably).<br>

registry events DO exist --> ID = 4658 <br>
lets try looking for modified registry keys for a potential service connected to totally legit software...  (just found executable attached to it, Totally_Legit_Software.exe)

okay silly idiot update, event ID i really needed to look was 4657 (registry modification), and BAM, we have found the next part of the flag!<br>
p2 --> 1s_a_pr3tty_us3ful_<br>
[filename](picoeventchall2.png)

okay so at this point, persistent for this program is now established on startup, time figure out what commands are happening that are causing the computer to shutdown...
new value in reg that it was assigned is this new executable... custom_shutdown.exe, yeah TOTALLY legit. lets see where this takes up. <br>

simple idea, look for machine shutdown event!   eventid=1074 <br>

and with that --> last part of the flag, t00l_81ba3fe9} <br>
[filename](picoeventchall3.png)


#### lessons learned! ####
- event ID's are powerful tools, this capture had almost 9000 events, and most of them are created by the SAM and AD so have filters to sort 
- context is a even MORE powerful tool. Knowing information like it was an installed program from the internet, not through lets say a link, or that it was persistant on start was crucial pieces of info that helped to filter through all of the bloat events.