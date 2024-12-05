## try hack me | advent canlender of cyber challenges ##
am i four days behind? (yes) <br>
can i catch up? YES <br>

__goal is to learn some new stuff and maybe win something!__

## day 1 - legit links and sketchy youtuber mp3 converters ##
*my favorite as a little kid*<br>
after opening attack machine, check webpage, and testing weblink, something is susp with somg.mp3 <br>

file somg.mp3 --> its a MS window link / .lnk, used for link to a path in windows based machines, thats definitly not right <br>

exiftool somg.mp3 for more information.
you see a lot of useful info like when it was created (2018), and other stuff, noting a path to powershell... and a command too, which <br>

-ep Bypass -nop      (allows scripts to run without worrying abt adminstrative and account permissions) <br>
pulls a file (Downloadfile from a remote server) and saves it on local machine
excutes with -iep, also triggers a download of .ps1 file

this file then attempts to look for valueable info in ur machine pulling enviroment files for stuff like crypto wallets. <br>

main goal of challenge is to go over OPSEC (operational security)
- basically OSINT to find threat actors through ditigal traces
- this can be from signitures in code, to reused usernames, public forums ... 

yay finished day!!! interesting stuff  :p   <br>