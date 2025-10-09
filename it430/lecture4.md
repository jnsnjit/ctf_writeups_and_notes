# Metasploit and Initial Access #
one of the most loved and utilized tools for gaining initial access to a vulnerable service / endpoint. <br>

Exploit Rankings:
(1) want to use a high ranking one in order to not damage a machine <br>
(2) more niche exploits are lower ranked <br>


rev shell --> connect to you (nice to connect to machines on LAN area and surpassing firewall rules) <br>
bind shell --> establish a listener on the remote machine <br>

meterpreter --> flexible c2 shell<br>
purely running on mem, so that it will not be persistent after restart unless more control is gained <br>

msfconsole
## Basic Commands ##
- ? help
- exit or quit
- sysinfo
- reg
- shell 
- shutdown / reboot
- getpid
- getuid
- ps
- kill
- execute
- migrate: function to hop process to another
- cd / lcd
- pwd ls cat donwload / upload
- mkdir rmdir
- ipconfig / ifconfig route portfwd
a bunch more, but meterpreter docs are great! <br>