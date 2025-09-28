# Week 2 - Reconnaissance #

__MITRE ATT@CK Framework:__ <br>
matrix of defined tactics, techniques, and procedures of what adverseries commonly do. <br>
_take a peak at entire internet is broken video later!_<br>

!REMINDER! - do not do reconnaissance on public networks that you are not authorized to do!<br>

_before_ touching a computer ... do OSINT, try to gather as much intel __passively__! <br><br>

__Certificate Transperency__ - websites need certificates in order to be trusted (s). this NEED to be published online, and this info (the entire history of it ... ), can be found online. this can actually bleed info for websites that are not open yet, and not entirely public, great start for mapping an external attack surface. <br>
__crt.sh__ <br><br>

__Breach Awareness__ - websites exist that keep track of disclosed breaches for a company, this can be done for know internal employees in order to potentially started hunt for old passwords lying around on the internet. <br>
__haveibeenpwned.com__,__hudsonrock.com__ <br><br>

__DNS Interrogation__ - Useful for querying information for registered domains. nslookup, dig, whois ...
* on the blue side - deny public address trying to do zone transfers
* have an external hosting dns, and a internally hosting dns record

__Websites__ - tons of social enginnering info. 

__Exiftool__ - great tool written in perl to extract metadata from a file! (used bf!)
__CeWL (Custom Wordlist Generator)__ - open source software to crawl websites ... cool tool!
__Search Engines:__ being able to find information out on the web utilizing the power of search engiges (google dorking be like)


__Network Scanning__ - attackers want to understand a networks topology. we want to know VLAN's, internet connectivity, DMZ, internal networks and the vulnerabilities that come with them. --> NMAP <br>

__Mass Scanning__ - very malicious in most scenarios, but is ideal for network enumeration on a LARGE number of IP's <br>

__TLS-Scan__ - will grab TLS certificates from an IP address provided

__Mitigations for Scanning__
--> setting up private vlans that stop internal endpoint from scanning other machines that they do need access to. <br>