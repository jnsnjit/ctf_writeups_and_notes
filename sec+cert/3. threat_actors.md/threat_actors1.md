## Threat Actors! ##

__def: an individual or entity responsible for incidents that impact security and data protection.__ <br>
Threat actors have attributed!<br>
threat actor needs a driver/motivation... ranging from blackmail, espionage, to revenge. <br>

__TTP's: Tactics, Techniques, and Procedures - methods and patterns associated with group/individual actor.__<br>
 
## Hacker Motivations ##

- Data Exfiltration:
*the unauthorized transfer of data from a computer. they want personal information for finanicial gain*<br>
- Blackmail:
*obtaining sensitive information with the objective to threaten its release into the public unless certain demands are meet. think bitcoin?!*<br>
- Espionage:
*tech spying on individuals, orgs, or nations with the intent to gather classified information.*<br>
- Service Disruption:
*usually achieved with some type of Distributed Denial of Service (DDoS) attack, overwhelm a server or service in or to make it unavailible for normal users*<br>
- Finanicial Gain:
*done to achieve company secrets with the objective to net money*<br>
- Philosophical or Political Beliefs / Hacktivism:
*attacks done in order to promote a political agenda, social change, or as protest.*<br>
- Ethical Reasons:
*authorized hackers, motivated with the intent to improve security, like finding exploits/bug bounty.*<br>
- Revenge:
*think disgruntled laided-off employee, with the goal to harm their former employee via breaching data, disrupting services, or leaking sensitive information.*<br>
- Disruption/Chaos:
*hacking adrenline junkies, engage in malicious activities for the thrill of it, to challenge their skills, or to cause harm.*<br>
- War:
*cyber attacks with the intention to be used as a tool in warfare, both on and off the battlefield.*<br>

## Threat Actor Attributes ##

__Internal__ = individuals or entities within an organization who pose a threat to its security. <br>
   || <br> 
__External__ = individuals or entities outside an organization that attempt to breach cybersecurity defenses. <br>

__Resources/Funding__ --> what tools,skills, and personnel does a threat actor have at their disposal. <br>
__Sophistication/Capability__ --> actor's technical skill, complexity of tools, ability to avoid detection. <br>
low skill = Script Kiddie (someone who mostly uses premade software to do their bidding, low tech skills) <br>
high skill = nation-state hacker, hacking groups , ... <br>

## Unskilled Attackers ##

__def: individuals with limited technical expertise who utilize tools, scripts, and exploit to carry out low skill attacks.__<br>
can still pose a threat! mostly with systems that exist with known, unpatched vulnerabilities. <br>
pros: sheer number of unskilled hackers, brute force, can easily damage infra <br>
cons: easy to stop with basic defense, easy to catch, give up quick <br>


## Hacktivists ##

__def: cyber attackers who carry out their activities driven by socialecopolicitial idealogies to draw attention to their cause.__ <br>

- Website Defacement
- DDOS Attacks
- DOXXING
- Data Exfiltration with intent to just release information
<br>
idealogical beliefs >> finanical gain   (ANONYMOUS)(LulzSec)

## Organized Crime ##

__def: well structured groups that execute cyberattacks for financial gain --> think fraud, ransomware, identity theft, and credit card fraud.__ <br>
Cyber Mafia operating at the international level!?
- Crypto exploits
- Data Exfil
- Dark Web
goal is MONEY. <br>

## Nation-State Actors ##

__def: highly skilled attacks sponsored by the government to carry out cyber espionage, sabotage critical systems, or cyber warfare against other nation states/specific targets.__ <br>
can operate indepently!
- False Flag Attack: orchestrated in a way where the attack appears to originate from a different source/group.
- Advanced Persistent Threat(APT): synonymous with nation-state actor, long term persistence and stealth.

APT --> think about espionage, gathering intel, and disrupting politics. <br>
Stuxnet Worm: piece of malware that was designed to sabotage iran's nuclear program (US and Israel). <br>


## HONEY! ##

__DEFINITIONS:__<br>
1. Honeypots: decoy systems or server designed to attract and deceive potential attackers via simlating real world IT assets.

2. Honeytokens: fake pieces of data inserted into a database or system meant to alert administrators when they are accessed or used.

3. Honeynets: the connection of multiple honeypots to create an entire decoy network/system, meant to observe and watch multi-stage attacks.

4. Honeyfiles: decoy files placed within systems to detect unauthorized access or data breaches.

__Strategies to stop/monitor a threat actor__
- Bogus DNS: fake dns entries in a systems dns server, attackers from outside wont know they are fake.
- Decoy Directories: fake folders and files in sys storage meant to mislead attackers.
- Dynamic Page Generation: websites that have directories that present ever-changing content to web crawler in or to confuse/slow threat actors (remember hellpot?)
- Port Triggering: security mechanisms where specific services or ports on a network device remain closed until a specific outbound traffic pattern is detected.
- Fake Telemetry Data: system can respond to an attacker's network scan attempt by sending out fake network data.

## Shadow IT ##
__def: the use of information technology systems, devices, software, applications, and services without explicit organizational approval.__<br>
examples...
- use of personal devices for work purposes.
- installation of unapproved software.
- use of non-approved cloud services 
happens when security practices are TOO high!

## Threat Vectors and Attack Surfaces ## 
__Threat Vector: the means / pathway in which an attacker gained unauthorized access to a computer or network.__<br>
__Attack Surface: encompasses all the various points where an unauthorized user can try to enter/extract data from an enviroment.__<br>
- Restrict Access 
- Remove Unnecessary Software
- Disabling Unused Protocols

Different Threat Vectors: __Messages, Images, Files, Voice Calls, Removeable Devices, Unsecure Networks__ <br>