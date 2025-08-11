## Recovering Active Directory - TryHackMe Premium Room ##
Topics Covered in this Room:
- Remeditation Actions after a domain controller is compromised
- Identifying attack patterns and how to locate an infection vector
- Basic recovery process
- Common misconfigurations by domain administrators
- Post-recovery steps

Room Context:
1. Windows Server 2019, compromised domain controller
2. Infection Date 04/10/2023
3. Created additional accounts, modifying policies, and disrupting services

### Immediate Actions - First Response ###
evicting an attacker can be a LONG process... so the first thing you should do is access the attack surface that have compromised, and what can be isolated and seperated so that they do not escape eradication. <br>

1. Create a Backup of the compromised server for forensic re-evaluation, timestamping, and preserving chain-of-custody
2. Restore Machine to Trusted backup if possible
3. Segregate network and activate a secondary dc to provide essential services
4. Enable enhanced monitoring on restored server to identify any persisting IOC's
5. Limit creation and modification of new accounts, GPO's until recovery process is complete

### Identifying Attack Pattern - Initial Access ###
Understanding how the attack occurred is cruicial to recover a compromised machine. Use tools like ....
- Event Viewer
- BloodHound: AD relational graphing tool that can help reveal hidden relations in AD structure and determine attack paths in an AD enviroment

Red Team Tools:
- PowerView: good for AD enumeration and identification of privileged accounts. 

### Locating an Infection Vector - Find Exploitation Techniques, and who did it ###
Usually when an adversary gets access to a domain controller, they will begin to create new users and modify policies to become part of _tier 0_ group for persistent access. <br>
--> after looking at the DC fro accounts created after the initial attack, there is a new "evil.guy" account. <br>
--> then pivoting to evetn viewer, you can look for event codes related to assigning privileged administrator account access (4728,4729) and find that the user evil.guy was added to a global administrator role. :skull: <br>

_Q: What is the email address for the user evil.guy?_ 
- Used Powershell command: ``` Get-ADUser -Filter * -properties Mail```,   hack@crypto
_Q: What is the total number of user logged on after Dec 1, 2022?_
- Used similiar command: ```Get-ADComputer -Filter * -properties LastLogonDate```, 1
_Q: What event ID will be logged if a user is removed from a universal security group?_
- 4757

### Domain Takeback - How to Recover the Machine ###
1. reset credentials for tier 0 accounts. 
2. remove and root out suspicious accounts
3. Change password for kerberos service account
4. reset passwords of administrative accounts
5. reset password of domain controller machine
6. remove any elements of persistence on the machine
7. Check ACL's and Group Policy for any malicious changes
8. Identity and anomolous inbound or outbound traffic activity

### Common Misconfigurations in Active Directory ###
1. Protect the Boot Order!!
- There really should not be any need for the machine to be able to boot from any other source except the OS, so config the BIOS to not allow booting from CD/DVD, external devices, or floppy drives
2. Protect log-on access to the domain controller!
- By default, all users can log on to any devices in AD structure, but these should really be implement with role-based access control in mind. (LEAST PRIVILEGE!)
3. Weak Passwords == not cool
- When a user uses a weak password, it is not a matter if they will get compromised, but only when... make sure to enable good password policies
4. Restrict Command Line tool usage for ONLY those who use it
- AGAIN, think least privilege, if a user doesnt need access to powershell and other command line and scripting tools, DO NOT GIVE IT TO THEM!
5. Have NTP Sync configured properyl
- Havng time synchronization is a lot more important then you may think, when it comes to timelining attacks and logging activities.

https://learn.microsoft.com/en-us/security/privileged-access-workstations/esae-retirement