# what is active directory? #

is some type of technology (some adminstrator machine maybe), that has access to all objs like:

- users
- computers
- resources
- printers
- shared files/folders 

in an organization's network!

basically stores information, and gives out access and permission based of given information
example: __printer?__ ok well give it printer like permission, dont allow it to do stuff that a printer should not be doing

remember windows active directory from BT? 
goal is to have all objects defined on the network accessable and watchable in one place

     --->       --->  
__user  👍   AD   👍   proper resources__     (think of zero trust infrasture!)(only allow what is needed)
     <---       <---

some obj types in AD:
- Forest
- Domain
- Organizational_Unit
- User
- Group
- Contact
- Computer
- Shared_Folder
- Printer
- Site
- Subnet

just like *OOP programming*, classes define objects, user object must have certain attributes

container obj: {user, group,...}
leaf obj:      printer1,printer2

__Security Prinicipal Object:__ objects that can be authenticated and assigned permissions
must have a __GUID__ and __SID__
- 128 bit Globally Unique Identifier
- Security Indentifier 

### Forest ###
__HIGHEST__ level obj
objects can ONLY comminucate within a forest unless trusted

### Trees ###
level below a forest       (think abt *tree architecture*)

### Domain ###
logical grouping of objects, step below a tree, no limit of number of objects in domain
do NOT need to be in the same physical location \

### Domain_Controller ###
 responsible for all authentications, authorizations, additions, deletions, edits, and modifications inside its domain; //AKA supreme control of its area

## NICC Meeting ##
domain controller + dns (thinking)

nmap -Pn (what is this flag, look up later) (Pn means no PINGING) (meant to be secretive)

__LDAP__ - keeps track of all objects | list

__Kerbosos__ - grants ticket/auth which gives permission

(*kerbrute*): https://github.com/ropnop/kerbrute


nmap -sS -O scanme.nmap.org/24

Launches a stealth SYN scan against each machine that is up out of the 256 IPs on the /24 sized network where Scanme resides. It also tries to determine what operating system is running on each host that is up and running. This requires root privileges because of the SYN scan and OS detection.

*crackmapexec* (network cracking tool)
_SMB_ (think about shared file systems in windows directory, cool to know) - u - p

njit gives windows server (didnt know that)
tryhackme
