## Windows Hardening 101 - TryHackMe Premium Room ##
Objectives of this room:
- Learn key attack vectors used by hackers, and how to mitigate them with different hardening techniques
- Understand IAM, network management, windows updating, and config cheat sheets

### General Window Machine Concepts ###
__Services:__
--> create and manage critical windows functions, like network connectivity, storage, memory, sound, user credentials ... <br>
--> many applications will also use and run services as well. <br>
__Registry:__
--> unified container database to store configurational settings. 
__Event Viewer:__
--> app that shows detailing logging of events occuring on your machine.
__Telemetry:__
--> data collection system used by microsoft to enhance user experience by preemptively finding security and functional issues. 

_Q1: What is the startup type of the App Readiness service?_
- Manual
_Q2: Open Registry Editor and find the key "tryhackme", what is the default value?_
- {THM_REG_FLAG}
_Q3: Open the diagnosis folder and go through the various log files. What is the flag?_
- {THM_1000710}
_Q4: Open Event Viewer, what error type has the maximun number of logs?_
- Information

### Identity and Access Management / IAM ###
Remember Ideas of Least Privilege! Only authenticated and authorized user should be able to access only the bare minimun of what they need. 
Two Base Accounts:
- Standard
- Admin (Best practice restricts it usage for software installation, accessing registry editor, services ...)

__UAC / User Account Control:__ feature that enforces access control for all services and applications executed in non-administrator accounts. <br>
__Password Policy__ <br>
__Lockout Policy__ <br>

_Q5: what is the name of the administrator account on the machine?_ Harden <br>
_Q6: what is the current set level of UAC in the machine?_ Always Notify <br>
_Q7: how many standard accounts are created on the machine?_ 0 <br>

### Network Management ###
Things that require hardening / oversight:
1. Windows Defender Firewall: make sure it is configure to allow allow the minimum amount of traffic that the computers needs for its necessary functions
2. Device Manager: Have oversight of your drivers and what devices are connected to the machine, and disable any unused devices (least priv)
3. SMB File sharing: if you are NOT using at file sharing in your enviroment, PLEASE disable it, a big vector that attackers like to compromise in order to take an attack to a network level incident. 
4. Local DNS Cache: there is a local hosts file on that machine that can overwrite the caching of DNS translations over a browser, and adversary love to spoof this file in order to maintain persistence steathly on a machine.
5. ARP Attacks: arp caches can also be modified in order to spoof a machine, which adversary like do, in which the cache can be cleared by entering a terminal: `arp -d`
6. Remote Access: RDP == lovely way to compromise a machine if it is publically facing, disable if its not needed, and if it is, create a whitelist of devices that can use that service.

_Q8: In the Windows Firewall Panel, which of the following profiles is active?_ Private <br>
_Q9: Find the IP address resolved for the tryhack.me website in the virtual machine local host file:_ 192.168.1.140 <br>
_Q10: Open the command prompt and find the physical address for the IP address of 255.255.255.255 (broadcast addr):_ ff-ff-ff-ff-ff-ff <br>

### Application Management ###
Microsoft Store offers range of programs that are vetted (although not very well imo)
- Can toggle the machine to only allow installation of products that are only from the microsoft app store

Microsoft Office is a very important vector to harden in most enterprise enviroments due to its HIGH usage by like everyone. <br>
__AppLocker:__ feature that can be used ot block specific executables, scripts, and installers from execution. <br>
__MS Edge__

_Q11: In defender AV, it is configuredto exclude a particular extension from scanning, what is it?_ .ps <br>
_Q12: Is it best practice to immediately open a word document from the external web?_ nay <br>
_Q13: What is the flag for executing the office hardening batch script?_ THM_1101110 <br>

### Storage Management ###
Having file protection is something that is not immediately thought about, but without, a ransomware attack can completely destroy the availiblity of a machine. <br>

Bitlocker == w mitigation <br>
__Secure Boot:__ protects boot order for tampering and malicious boot-order malware. <br>

_Q14: What is the last sixdigits of the bitlocker recovery key stored on the same drive?_ 377564 <br>
_Q15: How many characters does the recovery key have?_ 48 <br>
_Q16: a backup file is stored on the desktop of the machine, what is the extension of the file?_ .bkf <br>