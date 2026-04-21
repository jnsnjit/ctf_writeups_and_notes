## Authentication - Lecture 5 ## 
__def:__ establishment of trust between endpoint and system. <br>

__Basic Security Requirements:__
1. identify information system users, process acting on behalf of users or devices
2. authenticate / verify that the indetities of the user as a prerequisite to allowing access to organizational information systems

__Derived Security Requirements:__
1. use multi-factor authentication to prevent singular fault break
2. employ replay-resistant authentication attacks

__Security Requirements:__
- prevent reuse of identifiers for a certain time period
- disable identifiers after a given time of inactivity
- enforce a minimum password complexity
- prohibit password reuse for a specific number of generations
- allow temporary password use for system logons with an immediate change to a permanent password
- store and transmit only cryptographically-protected password
- obscure feedback of authentication information

## Types of Authentication ##
1. Something you know (password, PIN, security question)
2. Something you have (key fob, electronic ID, key card)
3. Something you are (Biometrics, face, thumb, eye)
4. Something you do (Voice pattern, handwritting, typing rhythm)

### Password-Based Authentication ###
Most commonely used line of defense <br>

Windows --> SAM file stores user and pass, locked by SYSTEM, which is also in use while the OS is operating <br>
Linux --> /etc/shadow contains password with salted hash <br>

## Kerberos ## 
1. Client requests TGT (Ticket-Granting Ticket) from the KDC (Key Distribution Center)
2. KDC verifies credentials, sends back encrypted TGT and Session Key. 
3. Client will store TGT, if the session expires, do steps 1-2 again.
4. When the Client requests a resource, it will send it’s TGT to the TGS. (Ticket Granting Server)
5. TGS will verify the TGT, if valid, the TGS will send an encrypted session key for that resource.
6. From there, you will have a session key to have access to the destination resource you need authorization for.

Key Points:
1. Kerberos is a single-sign on solution
2. is a AAA service (Authentication, Authorization, Accounting)
3. Authenitication Server provides auth, TGS provides the session tickets

## Types of Password Attacks ##
1. Passive Online Attacks
the capture of communication without the alerting of the authorizing party. <br>
- Wiresniffing, MITM, replay

2. Active Online Attacks
Attack tries a list of passwords one by one againts the victim to crack the password. <br>
- Hash injection, Phishing, Live Password Brute Forcing, Trojan, Spyware

3. Offline Attacks
Attack copies the targets password file and then tries to crack passwords in his own system at different location. <br> 
- Rainbow Tables, Distributed Network, Pre-computed hashes.

4. Non-electronic Attacks
Attacker uses social enginnering / human tactics to obtain a password <br>
- Shoulder surfing, social enginnering, dumpster diving.

## Token Based Authentication ##
Card Types:
1. Memory card --> mag strip that stores data (does no processing)
2. Smart Tokens --> has embedded microprocessor, small portable objects, provide authentication through static, dynamic, or challenge-response prompts.
3. Smart Card --> contains a microprocessor, memory, and I/O ports

## Biometric Authentication ##
must balance between cost and accuracy <br>

as you create the decision thresold, of what you consider the genuine user, that is what determines how close you as an imposter need to get in order to get a false positive authentication <br>

## Remote Authentication ##
most of the time authentication happens remotely! so how do we do it securely? Usually use a form of challenge-response protocol to counter eavesdropping and other threats like message relaying. <br>
