## Security Control Categories ##
FOUR BROAD CATEGORIES -->         TMOP

Technical Controls: tech, hardware, and software implemented. (firewall, anti-virus, encryption, IDS) <br>
Managerial Controls: strategic planning and governance side of security. (risk assessment, training programs)<br>
Operational Controls: procedures designed to protect data, governed by human actions and internal proccesses.
- backup procedures
- account reviews
- user training programs
Physical Controls: tangible real world measures to protect assest (cameras, fences, guards, shreding, locks)<br>

## Security Control Types ## 
6 BASIC TYPES....

1. Preventative: proactive measures... (firewall)
2. Deterrent: discourage by making time-effort ratio not worth it for potential attackers.
3. Detective: monitor and alert orgs to malicious activities as they occur/shortly after. (IDS - intrusion detection systems)
4. Corrective: mitigate any potential damage and restore systems to their normal state.
5. Compensating: alternative measures that are implemented when primary security controls are not feasible.
6. Directive: rooted in policy, set standard behaviors in a organization.

## GAP Analysis ## 
def: process of evaluating the differences between an org's current performance and its desired performance

1. Define the scope of the analysis                      1
2. Gather data on the current state of the organization  2
3. Analysis data to identify gaps                        3
4. Develop a plan to bridge gaps                         4

TECH v Business GAP analysis: <br>
--> tech focuses on an orgs tech infra and where it comes short <br>
--> business focuses on a orgs business processes and where they fall short <br>

POA&M --> plan of action and milestones

## Zero Trust ## 
Deperimeterization: instead of strong perimeter networks to focusing on ZERO TRUST architecture and the cloud. <br>
"trust nothing and verify everything"<br>
zero trust demands from ALL DEVICES, USERS, and TRANSACTIONS in the network for verification.

**Control Plane:** overarching framework and set of components responsible for defining, managing, and enforcing policies related to the user in the organization.
- adaptive identity: real time validation of user based of location, behavior, device, etc...
- threat scope reduction: limit what is only needed for the user to work.
- policy-driven access control: develop and manage user access policies based of responsibilties and roles.
- secured zones: isolated ares in the network to house sensitive data.
1. Policy Engine: references access request with predefined policies.
2. Policy Adminstrators: establish manage policies
**Data Plane:** actual movement of packets and traffic based of logic provided by the control plane.