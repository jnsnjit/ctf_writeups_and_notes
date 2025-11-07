# Exploitation and Post-Exploitation #
Hacker Trends:
- using mal payloads == more popular
- social enginnering and phishing is most common attack vector
- if you can use a feature over a bug, that is a lot more preferred, because features will not get fixed!

Common Payloads:
- Macros in Documents
- DDE in MS Office (dynamic data exchange)
- ISO files (digital disk, too big to be scanned)


### MS Office Macros ###
__Allows for the automation of work with scripting!__<br>
--> can be very easy misused in malicious ways! <br>

### DDE - Dynamic Data Exchange ###
__Alternate to macros, can run arbitary commands in Excel and Office__<br>

### Container Files ###
ISO --> 7zip --> Tar --> Gzip --> malware.exe (hopefully the layers of the payload with obfuscate the malicious payload from being viewed by AV solution)<br>

### LNK Files ###
files that point to existing process (shortcut!) <br>
think LotL (living of the lands), where it can lead to a shell to install a payloader