## Multi-Room Series - TryHackMe Premium Rooms - SOC Metrics and Objectives ##
With any department, efficency can be measured using KPI metrics. 
- MTTR
- MTTD
- SLA
- MTTA

Topics Covered:
- Importance of KPI metrics listed above
- Importance of tackling False Positive rate as a L1 analyst
- Practice managing SOC team performance metrics

### Core Metrics ###
__Goal of the SOC - Protect CIA (Confidentiality, Integrity, and Availability)__ <br>
Goal of an L1 analyst? Correctly report True Positives to the higher level analyst! <br>

| Metrics | Formula | Measures |
|:-------:|:-------:|:--------:|
| Alert Count | AC=total alerts | Overall load of analysts |
| False Positive % | FPR=F/AC   | Level of noise in alerts |
| Alert Escalation % | AER = EA/AC | Experience of L1 analyst |
| Threat Detection % | TDR=DT/TT   | Reliability of SOC team |

1. _Alert Count:_ too low, lack of visability with the SIEM, undetected problems... too high, analyst are overwhelmed, and quality in alert triage is decreased... Ideal is 5-30 alerts per day per L1 analyst.

2. _False Positive Rate:_ If most alerts generated are falsed marked as malicious events, analysts are likely to miss true malicious activity within the spam of alerts generated.  0% is not realistic, but if over 80% of logs generated are falsely created, that is an issue that requires enginnered tuning in order to filter the false positives out. 

3. _Alert Escalation Rate:_ The more independent the L1 analyst can be, the better a job they are doing! but the quality of escalation matters greatly, the more that you escalate

4. _Threat Detection Rate:_ Should be at 100%! anything below has devasting consequences, and means that your network has a problem that was not solved by the SOC team.

### Triage Metrics ###
The SIEM creating the Alert is just the beginning of the story. It needs to be _responded_ by someone, properly _acknowledged_, and _remediated_ as fast as possible! <br>

| Metric | Common SLA | Description |
|:------:|:----------:|:-----------:|
| SOC Availability | 24/7 | Working Schedule |
| Mean Time to Detect MTTD | 5 minutes | Time between attack and detection time in SOC tools |
| Mean Time to Acknowledge | 10 minutes | Average time for L1 analyst to start triage of alert |
| Mean Time to Respond | 60 minutes | Time taken by SOC to stop incident from spreading |

### Improving Metrics ###
How to improve metrics? <br>
- Too many false positives? try making a playbook to automate common alerts
- Too late on detect time? talk to SOC enginners to refine detection time
- Take too long to acknowlegde alerts? make sure all analyst know about new alerts, and ensure alerts are distributed equally. 
- Take too long to respond to issues? as the L1, make your part of the process as efficent as possible!