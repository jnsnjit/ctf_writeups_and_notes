## notes on honeypots ##

__three basic honeypot types:__

- low: emulate a service (fake ssh port🔥)
- medium: emulate a application (fake database/login page 💯) 
- high: emulate a machine (fake system 🧠)

scale of hard you want to try/design
*def* honeynet: a system of multiple connected honeypots
must learn digocean! 

honeypot of choice: malbait
https://github.com/batchmcnulty/Malbait

idea of how I would set this up... 
1. pick a network to protect
*similiar to ncae, plan is to set up a internal network of vms*
2. understand to a basic degree to how the perl code spins up "fake" servers listed under TCP/UDP ports (registered ports)
3. run instance of malbait, mess around with tools and potential test audditing system
4. try to add to code!