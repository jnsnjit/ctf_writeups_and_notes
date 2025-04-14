## texSAW 2025! ##
not much time for this ctf this weekend, but knocked out a few challenges in forensics so ill do a recap!

### favorite flower ###
**Category**: forensics (obscurification, steganography, analysis)
**Difficulty**: easy
**Tools**: linux cmd (exiftool, binwalk, file, steghide, xxd, strings, zteg, stegonline)
**Date**: 4/11/25
**Attachments**: [img](prettyflower.png)

_analysis_ <br>

after downloading the file, taking a look at it, it is an fully functional png, so can mostly elimate that its the correct file type, but to be certain, just do a check:<br>

```
file prettyflower.png
```

after checking, next up is a quick look at the metadata of the file, which includes author, date, file size, etc...: <br>
```
exiftool prettyflower.png
strings -n 7 prettyflower.png
xxd prettyflower.png
```
none of these turned any results, so i continue to try some other tools, like zsteg and stegonline to look for embed files within the photo, but due to the actual png being already pretty small in size, i wasnt expecting much.

finally i came to looking at the actually image itself, looking for any potential embed watermarks, and after messing around with stegonline rgb filter tools, I found the flag!
[img](texSAW_chall_prettyflower.png)

flag: texSAW{Ringmaster}
### freaky flower ###
**Category**: forensics (obscurification, steganography, analysis)
**Difficulty**: easy
**Tools**: linux cmd (exiftool, binwalk, file, steghide, xxd, strings, zteg, stegonline)
**Date**: 4/11/25
**Attachments**: chal2.psd

_analysis_ <br>

after downloading the file, taking a look at it, it is .psd filetype, which is apparently adobe photoshop, which i didnt know about until know:<br>

```
file chal2.psd
```

after checking, next up is a quick look at the metadata of the file, which includes author, date, file size, etc...: <br>
```
exiftool prettyflower.png
```
flag is found within the metadata of the file, pretty easy chall!
[img](texSAW_chall_chal2psd.png)
flag: texSAW{sneaky_sunflowers_sure_suck}

### scrambled packets ###
**Category**: forensics (packet analysis, obscurification, steganography, protocols)
**Difficulty**: medium
**Tools**: wireshark, tcpdump, notepad, ?!NETWORK_MINER!? (could potentially write a code script if more information was needed to be parsed)
**Date**: 4/11/25
**Attachments**: cap.pcap

_analysis_ <br>

definitly required a brain for this challenge, but I like how it was done, definitly didn't feel cheesy. opened in wireshark, take a quick look at the overall capture, relativity big, contain a multitude of protocols, dns, http, icmp, tcp. <br>

step 1: starting with the unencrypted protocols <br>

after a first glance, there is a lot of both ICMP and HTTP traffic, so I went to take a look at them first, starting with icmp because its more irregular to be sending like 70 icmp requests within the span of a short period of time. (also didnt mention before, but theres only two computers involved in traffic in this capture) <br>

heres a sample packet:<br>
[img](texSAW_chall_scatteredpack1.png)<br>

looking at this, there is a lot to gather from, but ill briefly explain the thought process:
- all of the ICMP requests/replys send data within them at the end of the packet
- some of those ICMP packets only send just 1 byte of data == one ascii character
- of those that contained just one, it appears to be some type of flag because scattered in the 70 packets are like {, }, _
- from that, I deduced that this most definitly the right path, so I stopped looking at the other packets 

used a wireshark filter to capture what is only needed:<br>
icmp && (sort packet by packet length, all of the one ascii character packets had a size of 62) <br>
from there, the characters i captured was: <br>

k e T _ A S } o _ e e f h t o t x _ W a e } n n <br>

step 2: looks like i caught all the important stuff, start a more cryptographic deduction section: (build flag) <br>
TexSAW{}  _  _  _  <br>
koeefhtotaenn   <br>

at this point, this are the options:
1. find out all four word combinations with these sequences of letters (tried it, but too many options existed, so this would not be valid)
2. find out how the packet were "Scrambled"!

step 3: unscramable <br>

looking back at the original packets, and thinking about the word scrambled, one of the first ideas I thought was about anything that could delimit the order of how these characters might be sorted. some options I thought about was...
- ttl (time to live): all of the packets were assigned 62, so cant be that.
- identifier: nothing of use came out of looking at that.
- response time: appeared random, kept it in the back of the head but prob not.

Eureku!<br>
its the sequence number. look at the image attached about, sequence num 0/0 is also the first character in the flag: T. this follows for the first characters and the last one, }. so its most definitly the solution.<br>

after crafting the flag, it is...:<br>
TexSAW{not_the_fake_one}<br>
0123456789.............23<br>


