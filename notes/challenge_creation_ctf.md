# Challenge Creation for Each Categories - And What Tools to Use #

# BIN #
most bin challenges revolve around buffer overflow, and how to trigger them within execution. 

function is allocated memory 

== Stack == 
= = = = = = 
= = = = = = 
= = = = = = 
= = = = = =     <_ instruction pointer 
 vars            |
 instru          | 
 ret addr     ---|
  

main() --> bad_func() --> _main()_
__because the bad_func in main, the computer has to know the memory address to get back to main__

gcc -fcf-protection=none -fno-stack-protector -z execstack -no-pie __file.c__

# Web and Hosting # 
### CI/CD ###
1. commit to doing chall
2. dev
3. pushing to git
4. testing
5. pushing to ctfd

name <br>
category <br>
gen topic <br>

announce what you plan to do early!
check commitments
problem => create a thread

rolling development is really important! <br>

__TESTING IS SUPER IMPORTANT, MUST BE SOLVABLE__<br>
__CHALLENGE SECURITY IS IMPORTANT__<br>


### Gen Info ###

challenge spread is SUPER important <br>
Answering Tickets --> uh... rubber ducky method <br>

backup ctfd
export scores
upload
submit canva badges
send results in server

### Infra ###

1. Digital Ocean
- MUST DISABLE PASSWORD AUTH
- Fail2Ban
- nsjail/Docker
- Scale as you need

2. CTFd
- do not host with them
- rules challenge

### Categories ###
web challenge difficulty can be hard to judge <br>
complexity and uniqueness is usually a good indicator <br>

bootstrap studio
Questions
