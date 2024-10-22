## Sunshine CTF ##

these two challenges I am going to lump together due to the nature of their solution/problem

### icmp1 ###
**icmp = internet control message protocol**

challenge is a small pcap file, in which after checking the icmp packets, the flag is found in plaintext 

sun{only_a_ping_away}

description of the challenge basically gives it away, always remember that icmp is a messaging protocal and has messaging capabilities, not just for pinging. if building server, likely you wont need it, so disable the port.

### icmp2 ###

again, the solution can be found in the same way, except now the flag is seperated in multiple packets, however, a good wireshark filter like data will weed out the info you dont need

sun{icmp_is_fun_1337}

things to note for the future,

icmp comes in different protocals, one for ipv4 and one for ipv6, can be important in analyzing network traffic
zero trust! limit things you dont use
plaintext in packets can be filtered for with the word "data" in the filter bar



