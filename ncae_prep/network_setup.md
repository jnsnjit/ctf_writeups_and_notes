## how to connect multiple vm's together ##
*cant believe I have made it this far without doing that yet*<br>

resources:<br>
https://openclassrooms.com/en/courses/7163136-set-up-virtual-machines-using-virtualbox-and-vsphere/7359231-establish-communication-between-virtual-machines

to get vms to act like a real machine, you need to change the network setting from NAT:

- **NAT:** default setting, creates virtual network for vm, can communicate with internet, but not with other devices on their "network". this means that if I spin up multiple vms on my device, they can neither communicate with my host devices or other virtual machines on my computer. good for your classic dummy machine
- **Internal Network:** this setting makes it so your virtual machine can communicate with each other on a private network, but can not communicate with the external world. (one for NCAE!)
- **Bridged Adapter:** makes it so that your network adapter is also used to manage traffic for your virtual machines, make them exist as another machine in your real life network. this way, you can have machines communicate with both the internet AND each other. be warned however, you are directly using you wifi adapter, so keep that in mind.
