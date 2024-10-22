## DeadFaceCTF ##

*this challenge I ALMOST GOT, but kind of just ran out of time to get it, solution is a bit silly but interesting, learned a bit and wrote some scripts to help filter through information in captured packets* <br>

1. first analyzing <br>
small pcap capture, only 7kb's
after reading description of challenge, there was mention of two key words I didnt know of the top of my head: <br>
- proxy machine
- C2 server

after some reasearch: <br>
**C2 Server:** Command and Control Servers, machine that threat actors use to coordinate attacks automously/remote <br>
**Proxy Machine:**  machine that recieves the network traffic before leaving the network (before endpoint router), and filters information. think about like NAT addressing, or like a domain controller/autheniticator <br>

take note however, the pcap only captures on network traffic, and since the proxy machine is filter the outside world info before reaching the comprised machine, we can not learn too much about the C2 server without looking at traffic past the proxy machine, so either the proxy machine or endpoint router.

comprised host ip: -.-.-.135
proxy machine: -.-.-.188

only tcp packets captured, interesting, in which there is plain text payloads...

two things:
from machine: qrqrqrqrrqrqrrrqr (string of q's and r's)<br>
from proxy (c2): ack       (acknowledgement)<br>

from here, and thinking about the name of the challenge, QR code should have probably spoke out to me, but instead I went into a different path, which was that the q and r represents 1's and 0's, and that the first + last line was all R's = end communication signal

so, I exported the important packets in capture, and made these filtering python scripts (with a little help from the gpt), and by the end, I was not really about to extract anything crazy, but i went through a bunch of different ideas:

frequency = alphabet correspondence (26+2 for brackets)
32QR -> one ascii symbol --> string by the end --> first and last RRRRRRRRR = nothing/filler

after the comp, one of my teammates, ben, found the qr thing, and makes a TON of sense

now i actually just tried to read the qr, and if I had access to the text instead of the image, I would convert the hex (51 52 51 52 51 52) in to black and white boxes to make the eyes of the qr code more readable, and then I would probably be able to read the flag


