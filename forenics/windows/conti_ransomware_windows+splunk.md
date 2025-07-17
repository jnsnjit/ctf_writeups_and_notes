## Conti - TryHackMe Challenge ##
https://tryhackme.com/room/contiransomwarehgh <br>

splunk ransomware challenge on windows computer ... learned a lot in this one! <br>

System Monitior - Windows Sysinternal Tool for Better Windows Event Logging! <br>
sysmon is able to capture a lot important events that regular security monitoring loggings in windows event viewer misses. some of these events include:
 - __Event ID 1__: Process creation. The process creation event provides extended information about a newly created process. ProcessGUID field is a unique value for this process across a domain to make event correlation easier. The hash is a full hash of the file with the algorithms in the HashType field. useful for file analysis in OSINT threat intelligence sources.

- __Event ID 2:__ A process changed a file creation time. good for keeping track of real file time creation for forensic analysis and incidence response reporting. many legit process also do this, so keep that in mind. 

- __Event ID 3:__ Network connection. creates logs for TCP/UDP connections on the machine.

- __Event ID 5:__  Process terminated time.

- __Event ID 6:__ Driver loaded, give performance data and hash of driver being loaded.

- __Event ID 7:__ Image loaded

- __Event ID 8:__ CreateRemoteThread. detects when a process creates a thread in another process. Usually only really done but malicious applications attempting to inject code/burrow into other processes.

- __Event ID 9:__ RawAccessRead. when process attempts reading operations, usually down in data exfilration attempts + avoiding auditing tools.

- __Event ID 10:__ ProcessAccess. records when a process creates another process. can detect hacking tools attempt to access restricted areas like the local security authority + pass-the-hash attacks. 

- __Event ID 11:__ FileCreate. monitiors file creation and overwrites. 

- __Event ID 12:__ RegistryEvent (Object create and delete). Registry key and value create and delete operations map to this event type, which can be useful for monitoring for changes to Registry autostart locations, or specific malware registry modifications.

... more important ones as well, these are just scratching the surface! <br>