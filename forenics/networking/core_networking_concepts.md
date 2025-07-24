## TryHackMe - Core Networking Protocols ## 

### DNS / Domain Name Service ###
DNS serves as the bridge between ip address and domain names of those addresses. <br>
UDP/TCP port 53 <br>

DNS Record Types: 
1. __A Record:__ the a address record maps a hostname to one or more IPv4 addresses.
2. __AAAA Record:__ same as A, but maps for IPv6.
3. __CNAME Record:__ The CNAME (Canonical Name) record maps a domain name to aanother domain name. useful!
4. __MX Record:__ MX (Mail Exchange) record specifies the mail server responsible for handling emails for a domain. 

want to know abt DNS info?
- whois, nslookup, dig ... <br>

### HTTP | HTTPS ###
HTTP - Hypertext Transfer Protocol
HTTPS - Hypertext Transfer Protocol Secure

HTTP(S) Methods:
- GET: retrieve data from a server
- POST: submit data to a server
- PUT: used to create a resource to overwrite an existing one
- DELETE: used to delete a specified file/resource

### FTP: File Transfer Protocol ###
meant for file transfer :p (port 21):
- USER: input username
- PASS: input password
- RETR: download file from server
- STOR: upload file to server

### SMTP: Simple Mail Transfer Protocol ###
port 25!
simple commands:
- HELO/EHLO: initate SMTP session
- MAIL FROM: specify sender email
- RCPT TO: specify recipient email
- DATA: indicate sending of mail contents
- . indicate EOF message

### POP3: Post Office Mail Protocol ###
allows for client to communicate with mail server to retrieve email messages. <br>
Simple Commands include:
- USER
- PASS
- STAT: request number of messages and total size
- LIST: list all messages and sizes
- RETR: retrieve specified message
- DELE: mark a message for deletion
- QUIT: end POP3 session, applying changes

### IMAP: Internet Message Access Protocol ###
need messages to be sync'd on multiple devices? IMAP is your guy! <3 <br>
