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

