### DownUnderCTF WriteUp's ###

first CTF taken seriously in a bit, lets see if my skills are still gooddd :P


### Easy Challenges ###
quick challenges that are not worthy of a whole section

discord challenge flag --> found in img in announcements page at launch of ctf
zeus executable challenge:
1. file zeus --> saw it was an elf exe, whipped out ghidra for analysis
2. after decompiling, did some touch up of relevent function names
3. challenge was a very simple if statement that was trying to obsecure its objective, but basically, when running the exe, it needs two parameters, the "-invocation", and then the invocation string defined in the function.
![ZEUS!](images/image-1.png)

brainrot website challenge:
- looking at web code, if sent a POST request to /admin/flag with an X-API-Key header, it will give the flag. just a matter of getting the key
- checking all the pages with burpsuite and looking at network requests, i see a js script doing some functions and other stuff, looking at it, it says key is obsecured, but NOT hidden, and it looks like the function there has the key
- asked to chatgpt to figure it out ☠️, got lazy, but it was basically a XOR function, and after having it do all the hard work creating the script, the key was TUNG-TUNG-TUNG-TUNG-SAHUR
- from there, made a payload with burpsuite web proxy, and retrieved the flag

### Down To Module Frequencies ###
still not super hard yet, but i like the thought process on this challenge <br>

original text is in dtmf herts frequency, which can be decoded, in which I create a very simple and crude script to parse the formatting of the text, as i couldnt find a good tool online to do that. <br>

after practicing my very rusty python skills got the text down to:  666#66#555#999#66#444#66#33#8#444#33#7777#55#444#3#7777#9#444#555#555#777#33#6#33#6#22#33#777#8#44#444#7777 <br> 

still didnt look like the flag, but looked like it was close to human readable, in which i then put this into dcode cipher detector, which send it was SMS phone tap, so I used there decoder, and got the flag: <br>

DUCTF{ONLYNINETIESKIDSWILLREMEMBERTHIS} <br>

lol like this one!