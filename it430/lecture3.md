# Week 3 - Password Cracking #
should be a good review of password idealogy and hashing td <br>

LANMAN == superbad <br>
NT Hash == still bad <br>
NTLM == meh <br>
Kerberos == security standard for windows <br>

__John the Ripper:__ awesome cmdline tool with password cracking abilities

## Mitigations for Password Attacks ##
1. Password Complexity and Length Requirements
- built into Active Directory
- pass-phrase == best
- password resets != not good for humans, good for service accounts that are randomized
2. Disable weaker password encryption types (LANMAN..)
3. Enable Multifactor Authentication

## Password Cracking Reporting ##
DPAT - Domain Password Audit Tool: <br>
_based of password cracked, it will automatically generate a report for it_ <br>

