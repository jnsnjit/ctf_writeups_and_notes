# Lecture Six - Firewalls, IDS, and IPS Systems #
There needs to be some type of "security guard", a device that allows accepted inbound and outbound traffic for users inside and outside a system! <br>

## Design Goals of a Firewall ##
1. all traffic from inside to outside MUST pass through the firewall (can be a potential bottleneck)
2. only authorized traffic defined by the local security policy will be allowed to pass
3. the firewall itself is immune to penetration

Firewalls can also:
- User Identity: user must provide authentication (IPSEC), basically turns into a VPN
- Network Activity: control access based on considerations like the time of request, rate of requests, or other activity patterns

## Capabilities and Limits ##
Negatives:
1. Creates a single choke point, cant protect against attacks bypassing the firewall
2. May not fully protect from internal threats
3. Laptops, PDA, or other portable storage device may be infected outside, and physically brought in and used internally

Positives:
1. Provides a location for monitoring security events
2. platform for several internet functions that are not security related (NAT, internet usage)
3. can serve as a platform for VPN protocols like IPSEC

## Types of Firewalls ##
### Packet Filtering ###
(Stateless) <br>
IN/OUT EXT/INT <br>

__ACL:__ Access control list, there is standard and extended versions. <br>
Standard:
- only 1-99 lists
- can only only and block based of src ips
- should be placed closer to the destination

``` access list 10 permit|deny 192.168.1.2 0.0.0.0```
``` access list 1 deny 192.168.30.0 0.0.0.255 ```

Extended:
- 100-999
- can block by src, dest, src port, dest port
- placed closer to the src of the traffic generated

access list, num 100-999, operation, transfer protocol, src, src wildcard mask, dest, dest wildcard mask, any eq (port number)<br>
``` access-list 103 permit|deny tcp|udp|ip|icmp 192.168.0.0 0.0.0.255 any eq 80 ``<br>

Notes for Homework:
host 10.10.10.2
acl rules (will be applied to router) (extended) <br>
``` config t ```
```access-list 102 deny tcp 10.10.10.2```
```interface fastEthernet 0/0```
```ip access-group 102 in/out ```

no access-list #rule-number <br>

#### Pros and Cons ###
Strengths:
- simplicity and very fast!
Weaknesses: 
- cannot prevent attacks that employ application specific vulnerabilties
- limited logging founctionality
- does not support advanced user authentication
- vulnerable to attacks on tcp/ip protocol bugs (ip spoofing, source routing)

### Stateful Inspection Firewall ###
Stateful! <br>
will keep a record of network connections and states! <br>

|src addr | src port | dest add | dest port | connection state           |
|---------|----------|----------|-----------|----------------------------|
|x.x.x.x  | x        | x.x.x.x  | x         | Established/Closed/Waiting |

### Application Proxy Firewall ###
application proxy, acts as a relay of application-level traffic. <br>
connections are analyzed all the way up to the application layer for analysis. <br>
ex: Squid, Modsecurity, WAF's

### Circuit-level Firewall ### 
sets up two connections, one between itself and the user, and the one with itself and the server. <br>
works on the __session__ layer and lower, scrutinizes the TCP handshake process, much faster then an application proxy firewall with handling packets. <br>
typically used when inside users are trusted! <br>
- application-level gateway inbound, circuit-level gateway outbound 
ex: SOCKS proxy, TLS firewall <br>

## Bastion Host ##
__def:__ system that is identified as a critical point in the network's security <br>
- run secure O/S, and only perform ESSENTIAL services (DNS, HTTP, SMTP, FTP)
- may require authentication to access proxy
- disallow write operations on the disk
- each proxy is independent of all other proxies (isolation and segmentation)

## Firewall Topologies ##
1. Host-resident firewall:
2. Screening router: single router between internal and external network
3. Single bastion inline: single firewall device that is between internal and external router
4. Single bastion t: has a third network interface on bastion to a DMZ where externally visible servers are placed (medium to large organizations)
<br>
                 --> DMZ public access <br>
LAN --> FIREWALL --> Internet <br>
                 <--    <br> 

5. Double Bastion Inline: two firewalls that segment dmz and internal lan
LAN --> FIREWALL --> INTERNAL DMZ --> FIREWALL --> Internet <br>

6. Double Bastion T

## IDS - Intrusion Detection System ##
### NIDS ###
__def:__ monitors network traffic, provides early warning systems for attacks, and analyzes network, transport, and application protocals. <br>

__inline deployment:__ network traffic MUST pass through it, with the motivation to stop the attack, placed at divisions in the network. <br>
__passive deployment:__ monitors a copy of actual traffic, monitoring key locations like any DMZ's <br>
- SPAN: switch port analyzer, managed switch (able to config span ports for mirroring), allows traffic received on one interface to be copied to another monitoring interface.
- hub based: the hub will relay whatever it receives to all interfaces, easy to do, but complex / collisions to deal with.
- tap based: think of like a wire tap (not popular, meant for QUICK deployments)

#### Pros ####
1. cost of ownership is low because IDS is shared on the network
2. packet analysis can look of all network traffic
3. packets are captured in a separate machine, for a forensics POV, it preverse logs on another device
4. real-time detection and response
5. operating system independence

### HIDS ###
__def:__ monitors traffic on the host machine, able to stop compromises in progress, monitors system processes and calls. <br>

#### Pros ####
1. good for protecting critical servers
2. software agent resides on system
3. detects multiple intrusions by analyzing logs of operating systems
4. monitoring file checksums and integrity
5. GREAT for behavioristic scanning on a machines behavior

## IPS - Intrusion Prevention Systems ##
not only with it detect malicious behaviors, but also attempt to perform migitations to stop it from continuing. <br>

Drop - packet is dropped <br>
Reject - packet is rejected and is logged, with an error message returned <br>
Sdrop - packet is rejected and not logged <br>


## UTM - Unified Threat Management Application ##
performs ALL functions!
- Routing
- Firewall
- IDS
- IPS
- WAF
- VPN 