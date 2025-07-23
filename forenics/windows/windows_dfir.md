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

Group: Administrators 
	Member: CCTL-WS-018-B21\Administrator 
	Member: CCTL-WS-018-B21\ADMIN-SRV
	Member: CCTL-WS-018-B21\Adminstrator

Group: Backup Operators
	Member: CCTL-WS-018-B21\ADMIN-SRV
	Member: CCTL-WS-018-B21\Adminstrator

Group: Device Owners
	Member: CCTL-WS-018-B21\ADMIN-SRV
	Member: CCTL-WS-018-B21\Adminstrator
	Member: CCTL-WS-018-B21\Guest

Group: Event Log Readers
	Member: CCTL-WS-018-B21\ADMIN-SRV

Group: Guests
	Member: CCTL-WS-018-B21\Guest

Group: IIS_IUSRS
	Member: NT AUTHORITY\IUSR

Group: Network Configuration Operators
	Member: CCTL-WS-018-B21\ADMIN-SRV

Group: Power Users
	Member: CCTL-WS-018-B21\ADMIN-SRV
	Member: CCTL-WS-018-B21\Guest

Group: Remote Desktop Users
	Member: CCTL-WS-018-B21\ADMIN-SRV
	Member: CCTL-WS-018-B21\Adminstrator
	Member: CCTL-WS-018-B21\Guest

Group: Remote Management Users
	Member: CCTL-WS-018-B21\ADMIN-SRV
	Member: CCTL-WS-018-B21\Adminstrator
	Member: CCTL-WS-018-B21\Guest

Group: System Managed Accounts Group
	Member: CCTL-WS-018-B21\ADMIN-SRV
	Member: CCTL-WS-018-B21\DefaultAccount

Group: Users
	Member: CCTL-WS-018-B21\ADMIN-SRV
	Member: NT AUTHORITY\Authenticated Users
	Member: NT AUTHORITY\INTERACTIVE
<br>