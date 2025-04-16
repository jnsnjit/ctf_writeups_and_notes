## Hardening Active Directory Try Hack Me Room ##

Domain --> Domain Controller <br>
__def__: a domain is the core unit of the logical structure for Active Directory <br>
__def__: a domain controller is the active directory server that servers as the brain of the AD services. <br>

Trees: set of domains    Forests: set of trees <br>

all of active directory works in a parent-child like node tree.
trust in AD == i will share resources with you! <br>
two categores of trust: <br>
| <br>
|->  trust based of characteristics: transitive + non-transitive trust. <br>
|       __A<>B<>C__ <br>
|->  trust based of directions: one way + two way trust. <br>

everything in AD is an object, if it holds another, "container", if not, "leaf". think about tree formats when thinking about AD! <br>

__GOOD SECURITY PRACTICE NUMBER 1:__
in AD, passwords for users are stored in two hashs by default, LAN Hash and Windows NT Hash --> disable LAN hash, its a weaker encryption, so just stick with the stronger one. :O <br>
can be modified by: <br>
Group Policy Management Editor > Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options > double click Network security - Do not store LM hash value on next password change policy > select "Define policy setting" <br>

__NUMBER 2:__
enable SMB block signing, to stop and detect SMB message injections! <br>

__NUMBER 3:__
enable LDAP signing as well (lightweight directory access protocol).<br>

__NUMBER 4:__
make sure to define some type of password policy! (DUH!) <br>

### Implementing Least Privilege ###
to promote the idea of least priv:
- make sure people only have the roles and access to the resources they need.
- define as much user accounts and priv's as possible.
- create shared accounts for users who need little to no privilege.
- audit accounts for changes in privileges, what resources they are accessing, and verify privileges are correct.

_Use Microsoft Security Compliance Toolkit! (free tool)_ <br>

### Known Active Directory Attacks ###

losing domain acount == game over <br>

heres some common attacks on how that happens:

__Kerberoasting__ <br>
Kerberoasting is a common and successful post-exploitation technique for attackers to get privileged access to AD. The attacker exploits Kerberos Ticket Granting Service (TGS) to request an encrypted password, and then the attacker cracks it offline through various brute force techniques. These attacks are difficult to detect as the request is made through an approved user, and no unusual traffic pattern is generated during this process. (Noahs challenge in JerseyCTF2025 tickets-plz utilizes this as part of the challenge solution.) <br>

__Weak and Easy-to-Guess Passwords__ <br>
The easiest target for intruders to breach security is the weak and easy-to-guess old passwords. <br>

__Brute Forcing Remote Desktop Protocol__ <br>
The intruders or attackers use scanning tools to brute force the weak credentials. Once the brute force is successful, they quickly access the compromised systems and try to do privilege escalation along with a persistent foothold in the target's computer. The best recommendation is to never expose RDP without additional security controls to the public internet. RDP should never face public internet, and if access to it is needed outside the network, use a VPN to tunnel in. <br>

__Publically Accessible Share__ <br>
During AD configuration, some share folders are publicly accessible or left unauthenticated, providing an initial foothold for attackers for lateral movement. <br>