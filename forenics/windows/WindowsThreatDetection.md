## Windows Threat Detection 1 - TryHackMe Room Series (1-3) ##
This room covers:
- Initial Access and Discovery Techniques
- How Threat Actors access and breach Windows Systems
- Practice detecing techniques discussed using Windows Event Logs

### Introduction to Initial Access ### 
No matter the goal of any adversary, the initial/first goal is to find a point to get past your "first door". This meaning moving from the external internet into your protected internal internet. <br>

Two Groups of Initial Access:
1. Exposed Public Service
Anything that is exposed to the internet by default NEEDS to be considered with security in mind, as within minutes, people on the internet will begin to automatically probe and scout for misconfigured or insecure services to attack. 
2. Human Interaction
This includes social enginnner, physical access attacks, external/removeable media... <br>

### Initial Access via RDP ###
having RDP facing publically == CARDINAL sin of bad security!!! <br>

so how can we detect an RDP breach?
1. Attacker will scan the network and detect and detect an exposed RDP port. 
2. RDP Brute Force: attackers will start to attempt loginng with common credentials. detecting this was covered in WindowsSIEM room!
3. Initial Access via RDP: successful logon, can be spotted by looking for a successful login associated with the source of the RDP brute forcing attempts. 
4. Further Malicious Actions Begin: at this point, they now have initial access to your endpoint, to track, keep a note of the login ID that is stored to follow the malicious activity.

__Q: Which user seems to be most activey brute-forced by botnets?__
- Adminstrator
__Q: Which IP managed to breach the host via RDP (Logon Type 10)__
- 203.205.34.107
__Q: Can you get the Workstation name of the threat actor?__
- DESKTOP-QNBC4UU

### Initial Access via Phishing ###
__Binary Attachments:__
--> in windows there is a lot of executable extensions (exe, bat, com, scr, cpl ...), which can make it hard for users to be aware of.<br>
--> Windows also hides known file extensions by default, which makes it even harder to detect malicious attachments and media. <br>

__LNK Attachments:__
In order to attempt to avoid Anti Virus detection, adversaries can try attaching scripts over binaries through LNK shortcuts. :3

As seen in WindowsSOC, sysmon is great for tracking malicious process downloads! <br>

### Initial Access via USB ###
USB flash drive attacks, although much less common then other attack vectors, is still something that needs to be considered from a blue-team perspective <br>

__Detecting an Infected USB:__
1. Easy: files within USB are malicious, user will self-execute them
2. USB runs malware as soon as the flash drive is plugged in

## Windows Threat Detection 2 - TryHackMe Room Series (1-3) ##
After breaching a host, the adversary has many options:
- establish a backdoor for long-term access
- take immediate action on their objectives

This Room Covers:
- Discovery and Collection
- Trace attack origin by follow/reconstructing process tree
- Find out what data threat actrs look for, and how it gets exfiltrated
- See how malicious commands are logged

### Discovery Overview ###
after an adversary gain initial access to your system, do they know anything about whats going on internally? usually, its little to none, so one of the first they start doing is starting for valuable information! <br>

__Discovery in Windows:__
* Files and Folders: (type ...), Get-Content, dir, Get-ChildItem
* Users and Groups: whoami, net user, net localgroup, query user, Get-LocalUser
* Systems and Apps: tasklist /v, systeminfo, wmic product get name,version, Get-Service
* Network Settings: ipconfig, netstat -ano, netsh advfirewall show allprofiles
* Antivirus: Get-WmiObject -Namespace "root\SecurityCenter2" -Query "SELECT * FROM Antivirus"

__Q: Which Privileged gropu does the user belong to?__
- Administrators
__Q: Open Event Viewer and find the command you just ran in Sysmon Logs. What is the "Image" filed of the net command you just ran?__
- `C:\Windows\System32\net.exe`

when most of these command in discovery are ran, they create process on there own that are children of the command prompt that they exist in, making them easy to track. <br>

keep in mind however, if adversary gain access to the machines GUI (either through RDP or literal physical access), they are not only limited to command shell command,s but also graphical tools, like system configuration, apps/programs... <br>

__Q: looking at Sysmon logs, what is the first command the invoice.pdf.exe executes?__
- whoami
__Q: which command did the malware use to check the presence of MS Defender EDR?__
- ``cmd /c "tasklist /v | findstr MsSense.exe || echo No MS Defender EDR"``
__Q: to which domain did the malware send the discovered data?__
- exfil.beecz.cafe

### Collection Overview ###
Now past the point of discovery, adversaries will now attemp to grab all the valueable data they found,and attempt to execute it! <br>

every adversary will define what they think is consider as valueable data, from balckmail, banking/credentials, or stealing corporate data, like ssh/api keys. <br>

__Q: What is the Facebook password that the user saved in Chrome?__
- nsAghv51BBav90!
__Q: Which interesting SSH key does the user store on disk?__
- thm-access-database.key
__Q: What is the secret PDF file explaining THM internal network?__
- thm-network-diagram-2025.pdf

### Detecting Collection ### 
look for viewing of randoms/interesting files from adversaries (using notepad, type ..., Get_ChildItem, copy) <br>

__Q: looking at sysmon logs, what directory does the stealer create?__
* (in temp), staging_58f1
__Q: which three file extensions does this malware search for?__
* docx, pdf, xlsx
__Q: which powershell cmdlet does the malware used to get clipboard content?__
* Get-Clipboard
__Q: which domain does the malware exfiltrate to?__
* collecteddata-storage-2025.s3.amazonaws.com

### Ingress Tool Transfer ###
when a malicious adversary gets something like a malicious payload to the endpoint, its usually very small in order to avoid EDR solutions, so they have two options
1. Live off the land with the supplies on the machine
2. attempt to call and download additional tools to the machine

Common Transfer Techniques: <br>
1. Certutil (YOU KNOW!)
2. curl.exe
3. `powershell -c "Invoke-WebRequest -Uri '' -OutFile ''`
4. through GUI interface :o

Detecting a Transfer:
- a transfer WILL require a network connection, so looking for any network connections or DNS requests from the process will be a good sign. 

looking into this:
- when attempting to query from page with different tools, it gave different results. Why? is it because the user agent, and that is used to retrieve different pages?

## Windows Threat Detection 3 - TryHackMe Room ##
Objectives of the Room: <br>
- Understand C2 / Command and Control Structures in a Windows Environment
- Analyse and practice finding C2 persistance in a Windows Environment

### Command and Control / C2 ###
goofy ah black terminal of doom and despair when starting the machine lol :o <br>

in some cases, C2 control is not needed if the actor is able to complete there objectives in one session, however, when that is not the case, adversaries will usually establish (1/many) different ways to reconnect to a machine. <br>
- think temp folders, malicious dlls, masquerding processes, ssh keys, netstat connections, scheluded tasks ... 

__Q1: Which susipicious archive did the user download?__
- URGENT!.exe
__Q2: Where did the attackers hide the C2 malware file?__
- `C:\Users\Administrator\AppData\Roaming\update.exe`
__Q3: What is the domainn of the Command and Control Server.__
- route.m365officesync.workers.dev

### Persistence Overview ###
Data Stealing attacks usually are a "smash and grab". Other attacks though usually like to maintain persistence to continue data exfiltration over a longer period of time. <br>
- create new user
- create backdoor/web shell

User Groups to Watch for:
- Local Administrator
- Remote Desktop Users

### Persistence: Tasks and Services ###
there is a BUTT ton of ways to create persistence on a machine, so lets cover some: <br>
1. Create a Windows Service that runs after the OS starts. Look for unusual service creations, changes to registry run keys.
2. Create a Scheluded Tasked, look for schelude task creation events (4698) and launch of malicious processes. 

__Q1: Which Windows Service was created to persist the Nessie Malware?__
- Data Protection Service (multiple red flags, service having no description being a big one)
__Q2: Which scheluded task was created to persist the Troy malware?__
- AmazonSync
__Q3: What flag do you get after finding and running the Troy Malware__
- for the challenge question the malware asks, looking into sysmon for when the troy process is created, and the parent commandline is there.
- THM{c2_is_on_schelude}

### Persistence: Run Keys and Startup ###
run keys can be doing on certain users without adminstrative permissionsk, making it a very valid option when trying to establish persistence! <br>
- Add malware to Startup Folder
- Add malware to Run Keys

Note: Programs started within the Startup folder with have a parent process from explorer.exe, a valid binary, however, that does verify the integrity of the child process at all. <br>

__Q1: What is the parent process image of the "Odin" malware?__
- look at after reboot logs, also since its in startup folder, its explorer.exe
- C:\Windows\explorer.exe
__Q2: What is the last line that the "Odin" malware outputs?__
- "Done Doing Bad Stuff!"
__Q3: What flag do you get after finding and running the "Kitten" malware?__
- THM{persisting_in_basket}

### Impact and Threat Detection Recap ###
so why do threat actors want to establish persistence?
1. Add host to a botnet: thing about Mirai Botnet, and how these swarms of malicious compromised computers can be used for crypto mining, stealing data, C2 architecture, and used in mass DDOS attacks
2. Spying on a victim as part of a state-sponser campaign. think how nice it would be for a rival government adversary for it to be able to spy on critical infra, military planning, and confidential information for blackmailing.
3. Using a victim as an entry point. Maybe today there is no way to further escalate privilege in a network, but maybe if you wait a bit ... a new vulnerability will arise!

