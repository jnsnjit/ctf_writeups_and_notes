## good practices for linux sys administration ##

ufw --> like windows firewall
least priv

ufw --help
ufw works in least priv, blocks everything unless specified

depending on firewall, incoming connections/port rules may not deny/kick out users currently using a service
failtoban --> look at log files, filter for activity that it does not like, if someone is violating set rules, ban/timeout ip addr.