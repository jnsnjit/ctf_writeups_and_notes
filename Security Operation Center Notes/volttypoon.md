## Volt Typhoon - TryHackMe Splunk Lab ##
if ever getting lost, look at mitre attack and other threat intelligence frameworks to get a better understanding of the adversary! 

Log Source Types Ingested:
- ADSS / ADSelfService+
- Powershell
- WMIC / Windows Management Instrumentation Command-line
roughly 2,500 totals events in capture <br>

### Initial Access ###
__Q1: At what time was the Dean's password changed and their account was compromised by the adversary?__
`sourcetype=adss username="dean-admin" action_name="Password Change"`
- 2024-03-24T11:10:22

__Q2: Shortly after the account was compromised, the attacker created a new administrator account, what is the name of the new account?__<br>
having the timestamp and ipaddress that made the action, we can narrow the timeframe to see what happenned after the compromise, and look for the administrator account action. <br>
`sourcetype=adss action_name=Enrollment `(after time of last question)
- voltyp-admin

### Execution ###
now that they have their now admin account "voltyp-admin", lets now track malicious activity they will attempt to do... <br>

__WMIC / Windows Management Instrumentation Command-line:__ older, legacy first of a pseudo powershell. <br>

Volt Typoon APT is known to use WMIC for gathering infor, dumping databases, and infilrating and exploiting networks