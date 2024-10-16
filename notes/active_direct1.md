# what is active directory? #

is some type of technology (some adminstrator machine maybe), that has access to all objs like:

- users
- computers
- resources
- printers
- shared files/folders 

in an organization's network!

basically stores information, and gives out access and permission based of given information
example: printer? ok well give it printer like permission, dont allow it to do stuff that a printer should not be doing

remember windows active directory from BT? 
goal is to have all objects defined on the network accessable and watchable in one place

     --->       --->  
user  👍   AD   👍   proper resources     (think of zero trust infrasture!)(only allow what is needed)
     <---       <---

some obj types in AD:
<Forest>
<Domain>
<Organizational_Unit>
<User>
<Group>
<Contact>
<Computer>
<Shared_Folder>
<Printer>
<Site>
<Subnet>

just like OOP programming, classes define objects, user object must have certain attributes

container obj: {user, group,...}
leaf obj:      printer1,printer2

Security Prinicipal Object: objects that can be authenticated and assigned permissions
must have a GUID and SID
- 128 bit Globally Unique Identifier
- Security Indentifier 

### Forest ###
highest level obj
objects can ONLY comminucate within a forest unless trusted

### Trees ###
level below a forest       (think abt tree architecture)

### Domain ###
logical grouping of objects, step below a tree, no limit of number of objects in domain
do NOT need to be in the same physical location \

<Domain_Controller> = responsible for all authentications, authorizations, additions, deletions, edits, and modifications inside its domain; //AKA supreme control of its area
