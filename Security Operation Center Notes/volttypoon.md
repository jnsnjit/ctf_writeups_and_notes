## Volt Typhoon - TryHackMe Splunk Lab ##
if ever getting lost, look at mitre attack and other threat intelligence frameworks to get a better understanding of the adversary! 

Log Source Types Ingested:
- ADSS / ADSelfService+
- Powershell
- WMIC / Windows Management Instrumentation Command-line
roughly 2,500 totals events in capture <br>

### Initial Access ###
__Q1: At what time was the Dean's password changed and their account was compromised by the adversary?__
`sourcetype=adss username="dean-admin" action_name="Password Change"`
- 2024-03-24T11:10:22

__Q2: Shortly after the account was compromised, the attacker created a new administrator account, what is the name of the new account?__<br>
having the timestamp and ipaddress that made the action, we can narrow the timeframe to see what happenned after the compromise, and look for the administrator account action. <br>
`sourcetype=adss action_name=Enrollment `(after time of last question)
- voltyp-admin

### Execution ###
now that they have their now admin account "voltyp-admin", lets now track malicious activity they will attempt to do... <br>

__WMIC / Windows Management Instrumentation Command-line:__ older, legacy first of a pseudo powershell. <br>

Volt Typoon APT is known to use WMIC for gathering information, dumping databases, and infilrating and exploiting networks
_Q1: In an information gathering attempt, what command does the attacker run to find information about local drives on server01 & server02?_<br>
knowing they are using WMIC on the dean-admin profile, quickly did some searches with keyword "logicaldisk", the command in WMIC to extract this info
- `wmic /node:server01, server02 logicaldisk get caption, filesystem, freespace, size, volumename`

_Q2: The attacker uses ntdutil to create a copy of the AD database. After moving the file to a web server, the attacker compresses the database. What password does the attacker set on the archive?_<br>
- look for commands from dean-admin with 'ntdutil'
- then, look at location its moved to, and when the archive occured
- `d5ag0nm@5t3r`

### Persistence ###
the APT group employs web sheels to maintain a foothold in the network, hiding them as legitimate files

_Q1: to establish persistence on the compromised server, the attacker created a web shell using Base64 encoded text. in what directory was the shell placed in?_<br>
- C:\Windows\Temp\
- Look for activity related to ntdutil and temp.dit

### Defense Evasion ###
_Q1: in an attempt to begin covering their tracks, the attackers remove evidence of the compromise. First they wipe RDP records. What Powershell cmdlet does the attacker use to remove the "Most Recently Used record / MRU"?_<br>
- `Remove-ItemProperty`
- do research on how to remove powershell records, this cmdlet cam up, searched in splunk and found related activity for log clearing

_Q2: The apt continues to cover their tracks by renaming and changing the extension of the previous archive. what is the file name now called?_<br>
- after doing research on wmic commands to rename files --> look for ren command
- `cl64.gif`

_Q3: Under what regedit path does the attacker check for evidence of a virtualized enviroment?_<br>
- `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control`