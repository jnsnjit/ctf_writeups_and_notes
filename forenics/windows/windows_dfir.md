## Windows Deep Forensics Incident Response ##
time to get my hands dirty with a good DFIR lab! <br>

### Reliability of System Tools ###
When opening a machine for forensics analysis, it would not be wise to utilize system-bound tools existing on the machine prior, as adversaries can modify environment files to hijack, stop, or mitigate the potential forensics analysis that can be done. <br>

Because of this, __STEP 1__ of a DFIR analysis should be the verification of any signs of potential execution hijacking.

__STEP 1 (Bring Your Own Tools):__
1. this tools should be from KNOWN good machines, and a trusted integrity (good hash).
2. checking ALL enviromental variables is a good start... go into a trusted cmd and type "set" to view them. Important sections to verify include:
    - ComSpec (  command prompt exe is ran from)
    - Path (all env path values)
    - PSModulePath (PS directories)
    - Public (Public facing folder location)
    - TEMP/TMP (temp locations on machine)
3. verify integrity of powershell terminal... 
    - check ps location
    - check ps profile information

In this simulation, there is a lot of red flags with the powershell profile, such as writing to different hosts, removing eventlogs, stop services, and erasing ps shell history. <br>

4. Preserve Evidence. in this scenario, this profile is unsafe to use, so preserve it, and utilize a fresh one from a known good. 
5. Once utilizing powershell ...:
    - check version and imported modules

__Q: What tool did the adversary use to delete the logs?:__ wevtutil <br>

__Q: What was the registry path used by the adversary to store and steal the login credentials:__ HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest <br>

### System Profiling ###
Once the analysis of base system tools have been done, we can now began a deeper analysis of profiling the system. <br>
1. System Information: note down DNS Hostname, IP address (ipv4+ipv6), and MAC Addresses. 
- Get-CimInstance win32_networkadapterconfiguration -Filter IPEnabled=TRUE | ft DNSHostname, IPAddress, MACAddress
__CCTL-WS-018-b21 {10.10.116.18, fe80::9cb4:51e1:9567:943a} 02:38:78:70:B6:55__
- Get-CimInstance -ClassName Win32_OperatingSystem | fl CSName, Version, BuildNumber, InstallDate, LastBootUpTime, OSArchitecture

``` CsName         : CCTL-WS-018-B21 ```
``` Version        : 10.0.17763 ```
``` InstallDate    : 3/17/2021 5:59:06 PM ```
``` LastBootUpTime : 7/23/2025 9:25:47 PM ```
``` OSArchitecture : 64-bit ```

2. Retriving Date and TimeZone information! very important for timelining and documentation. 
- Get-Date ; Get-TimeZone
``` Id                         : Turkey Standard Time ```
``` DisplayName                : (UTC+03:00) Istanbul ```
``` StandardName               : Turkey Standard Time ```
``` DaylightName               : Turkey Daylight Time ```
``` BaseUtcOffset              : 03:00:00 ```
``` SupportsDaylightSavingTime : True ```
- Get-GPResultantSetOfPolicy -ReportType HTML -Path (Join-Path -Path (Get-Location).Path -ChildPath "RSOPReport.html")
``` RsopMode        : Logging ```
``` Namespace       : \\CCTL-WS-018-B21\Root\Rsop\NSB46278E6_3AA5_44B4_B1B5_1652A1F06A49 ```
``` LoggingComputer : CCTL-WS-018-B21 ```
``` LoggingUser     : CCTL-WS-018-B21\Administrator ```
``` LoggingMode     : UserAndComputer ```

### Checking Users, Policies, and Adminstrative Actions ###
when an adversary gains access to a new system, an option that can take is create or compromise accounts on the machine to maintain and potentially elevate their access. <br>
1. Look at User Accounts:
- Get-LocalUser | tee l-users.txt (write to output file)
``` ADMIN-SRV          True    Trusted admin account of LMV Co. for administering the *-SRV and CCTL-* zones. ```
```Administrator      True    Built-in account for administering the computer```
```Adminstrator       True    Built-in account for administering the computer```
```DefaultAccount     False   A user account managed by the system.```
```Guest              True    Built-in account for guest access to the computer```
```WDAGUtilityAccount False   A user account managed and used by the system for Windows Defender Application Guard sce...```
- WEIRD ah accounts, me when they misspell Administrator ☠️
2. Check Local Groups:
- __``Get-LocalGroup | ForEach-Object { $members = Get-LocalGroupMember -Group $_.Name; if ($members) { Write-Output "`nGroup: $($_.Name)"; $members | ForEach-Object { Write-Output "`tMember: $($_.Name)" } } } | tee gp-members.txt``__

Group: Administrators <br>
	Member: CCTL-WS-018-B21\Administrator <br>
	Member: CCTL-WS-018-B21\ADMIN-SRV <br>
	Member: CCTL-WS-018-B21\Adminstrator <br>
...
<br>

__Q: What is the total number of suspicious accounts?:__ 3 (Guest, Adminstrator, Administrator)<br>

``Get-LocalUser -Name Adminstrator | select * | tee guest_info.txt``<br
__Q: What is the security Identifier / SID of the Guest Account?:__ S-1-5-21-1966530601-3185510712-10604624-501 <br>
__Q: When was the last time the Adminstrator (purposely misspelled) account was logged on?:__ 2/28/2024 10:21:10 AM <br>

### Understanding Network Scope ###
adversaries not only like to move laternally across a network, but also like to establish C2 connections through beaconing and consistent outbound traffic. Analysing network activity is important! <br>

```Get-NetTCPConnection | select Local*, Remote*, State, OwningProcess,` @{n="ProcName";e={(Get-Process -Id $_.OwningProcess).ProcessName}},` @{n="ProcPath";e={(Get-Process -Id $_.OwningProcess).Path}} | sort State | ft -Auto | tee tcp-conn.txt```
or tbh to just use netstat like ... !<br>
`TCP    10.10.224.74:49678     silver-pvt:ssh         CLOSE_WAIT`
`TCP    10.10.224.74:49705     silver-pvt:ssh         CLOSE_WAIT`

#### Network Shares ###
--> folders and drives that are shared across the network (think SMB! + Eternal Blue), adversaries LOVE to utilize protocols like this to plant malicious stagers through a network, either as an attack on availiblity (Ransomware), or utilize to potentially compromise a user/service account with higher privileges. <br>
`` Get-CimInstance -Class Win32_Share | tee net-shares.txt ``

#### Firewall Access ####
looking at the firewall also reveal a butt ton of information, especially regarding with the attempt to exfiltrate information outside a machine to a remote destination. <br>
`` Get-NetFirewallProfile | ft Name, Enabled, DefaultInboundAction, DefaultOutboundAction | tee fw-profiles.txt ``

Name | Enabled | DefaultInboundAction | DefaultOutboundAction <br>
---------------------------------------------------------- <br>
Domain    False        NotConfigured         NotConfigured <br>
Private   False        NotConfigured         NotConfigured <br>
Public    False        NotConfigured         NotConfigured <br>

all good here ... <br>

### Startup Persistance and Registry Keys ###
being able to ensure persistence is on of the most crucial steps for adversaries to take in order to continue malicious activities over long periods of time! <br>

Sysinternals Autoruns!!! == great for finding out registry key information regarding to persistence like start on boot ... etc. <br>

<br><br>
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit
   C:\Windows\system32\userinit.exe
     C:\Windows\system32\userinit.exe
     Userinit Logon Application
     Microsoft Corporation
     10.0.17763.1
     c:\windows\system32\userinit.exe
     12/31/1958 2:49 PM
     MD5:      BF8825D08BC235F0609CA8BBEF4E179C
     SHA1:     470C3E60F9B2B6D83F95C7916A5361E34DEC3471
     PESHA1:   DF688108336B5E2AC79D652521CAE6F14BC4D450
     SHA256:   1FE7F7C59EC7EAA276739FA85F7DDA6136D81184E0AEB385B6AC9FEAAA8C4394
     PESHA256: A5160EF5F4B97E938DA7E956A3331FB66EA3F9EA7E7D8BEEF313F318F2C11B98
     IMPHASH:  8419D97ABDFEB6C320F0C39028647572
   cmd.exe
     cmd.exe
     Windows Command Processor
     Microsoft Corporation
     10.0.17763.1697
     c:\windows\system32\cmd.exe
     5/30/2008 3:32 AM
     MD5:      911D039E71583A07320B32BDE22F8E22
     SHA1:     DED8FD7F36417F66EB6ADA10E0C0D7C0022986E9
     PESHA1:   8F4C943F540AB1BFD6DD2A2820FA9EE7794CE550
     SHA256:   BC866CFCDDA37E24DC2634DC282C7A0E6F55209DA17A8FA105B07414C0E7C527
     PESHA256: 5F98D08805D4EEE36337C81914F0D82191A4D58D24EA2FF2E522A95A5D6E5B73
     IMPHASH:  272245E2988E1E430500B852C4FB5E18
<br>

`` Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\NetSh" | tee netsh-records.txt `` 
some unusual properties with this guy ... <br>

__Q: What user account will be used to run the AnyDesk application?__ Public <br>
__Q: What is the value data stored in "Userinit" key?__ C:\Windows\system32\userinit[.]exe, cmd[.]exe /c "start /min netsh[.]exe -c" <br>
__Q: What is the name of the suspicious DLL linked in netshell hive key?__ .\fwshield.dll <br>

### Services and Scheluded Items ###
another vector of persistance that adversaries really like to use! <br>

`LMVCSS                 Less Murphy Ventures Service Shield              Running Auto      C:\Users\Administrator\AppData\SpcTmp\INITIAL_LANTERN.exe                            2096` GULP! <br>

### Processes and Directories ###
bc processes are dynamic, they are easy to check for signs of anomalies when adveraries attempt to inject malicious code into them... <br>

``` Get-WmiObject -Class Win32_Process | ForEach-Object {$owner = $_.GetOwner(); [PSCustomObject]@{Name=$_.Name; PID=$_.ProcessId; P_PID=$_.ParentProcessID; User="$($owner.User)"; CommandLine=if ($_.CommandLine.Length -le 60) { $_.CommandLine } else { $_.Commandline.Substring(0, 60) + "..." }; Path=$_.Path}} | ft -AutoSize | tee process-summary.txt ```

``` Get-ChildItem -Path "C:\Users" -Force | Where-Object { $_.PSIsContainer } | ForEach-Object { Get-ChildItem -Path "$($_.FullName)\AppData\Local\Temp" -Recurse -Force -ErrorAction SilentlyContinue | Select-Object @{Name='User';Expression={$_.FullName.Split('\')[2]}}, FullName, Name, Extension } | ft -Autosize | tee temp-folders.txt ``` 
me when there is jmp.exe in the users local temp folder ☠️🫡 <br>

WHAT AN AWESOME ROOM! 😁