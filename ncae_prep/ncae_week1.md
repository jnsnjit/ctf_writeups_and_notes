## Week 1 Notes ##
_chances are there is way too many backdoors already set up on ur machine, so as soon as possible, you got crack down on that._
_pick something for the challenge to specialize, that being router config, one of the services, etc._ <br>
1. make sure ssh is installed, know for distros
- apt

install openssh-server openssh-client <br>
ssh-keygen -t encryption-type -f path/of/key <br>
(using ecdsa - lightweight and good for older machine but still maintains a level of security) <br>

2. prob using ecdsa 
scp (secure copy) <br>
scp _source_ _destination_ <br>
make sure that the authorized keys on the machine only have permission for read-write (chmod something :skull:) <br>
for ssh configuration --> add some simple things like max trys, ban IP's, etc... <br>

3. in general, after making config changes or anything
sudo systemctl restart sshd.service (insert service)

4. setting up passwordless authentication
for future easy access, make a config file with required info for login, and specify login with it when attempting ssh connections. <br>

5. ftp setup (dont use p21)
sudo apt install vsftpd <br>
config file --> nano /etc/vsftp.conf <br>

look in chroot (jailing for new logins) <br>
for ftp, there is a location where ftp must be accepted, make sure this is defined, and that ftp permissions do not exist outside the directory that it should not be in. <br>
## Extra Notes: ##
__ncae notes: the basics!__<br>

172.20._.2/16 - network    (- = team number)
router is mikrotik router --> https://help.mikrotik.com/docs/spaces/ROS/pages/328151/First+Time+Configuration (router manual)

__default out-the-box creds:__ <br>
admin, skip password, maybe might be password

__has its own commands, here are some ones you should know:__ <br>
- /ip address print 
- /interface print
- /ip route print
- /ip service print
(THIS ONE IS IMPORTANT, by default out the box this has telnet and other potentially unwanted ports open, so good to know) <br>

/ip address address = 172.20._team_number_.1/16 (know ur subnet) interface=(pick one of ur interfaces, can find in hardware description of your machine <br>
w - see who is logged in on the machine

killall -u _username_ (remove a user from a machine) <br>