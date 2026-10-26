# ISO/IEC 27001:2022 Gap Analysis: Contoh Resto Nusantara

**Overall readiness: 10.9%** (88 open gaps across 93 Annex A controls)

> Self-assessment only. This is not a certification; certification requires an audit by an accredited certification body.

## Readiness by theme

| Theme | Applicable | Excluded | Readiness |
|---|---|---|---|
| Organizational | 37 | 0 | 8.1% |
| People | 7 | 1 | 14.3% |
| Physical | 14 | 0 | 10.7% |
| Technological | 34 | 0 | 13.2% |

## Top 15 gaps (by risk)

| Control | Title | Status | Risk | Owner | Notes |
|---|---|---|---|---|---|
| 5.17 | Authentication information | missing | 5 | IT | Passwords shared over WhatsApp |
| 8.2 | Privileged access rights | missing | 5 | IT | Owner and IT share one superuser account |
| 5.15 | Access control | partial | 5 | IT | Shared admin login for POS back office across outlets |
| 5.34 | Privacy and protection of PII | partial | 5 | Marketing | Loyalty member phone numbers stored; UU PDP 27/2022 applies |
| 8.5 | Secure authentication | partial | 5 | IT | MFA on email only; not on Supabase or GitHub |
| 5.24 | Information security incident management planning and preparation | missing | 4 | IT | No incident response plan |
| 8.8 | Management of technical vulnerabilities | missing | 4 | IT | No patch schedule for outlet PCs |
| 5.1 | Policies for information security | partial | 4 | IT | Draft policy exists but not approved by management |
| 5.9 | Inventory of information and other associated assets | partial | 4 | IT | POS terminals listed in spreadsheet; laptops and cloud accounts not listed |
| 5.16 | Identity management | partial | 4 | IT | Staff accounts created ad hoc; no joiner/leaver process |
| 5.23 | Information security for use of cloud services | partial | 4 | IT | Google Workspace and Supabase in use; no cloud usage rules |
| 8.13 | Information backup | partial | 4 | IT | Daily database backup but restore never tested |
| 8.28 | Secure coding | partial | 4 | IT | Secrets sometimes committed to repositories |
| 5.2 | Information security roles and responsibilities | missing | 3 | Management | No named information security owner |
| 5.3 | Segregation of duties | not_assessed | 3 | - | - |

## Statement of Applicability (draft)

| Control | Title | Applicable | Status | Justification / evidence |
|---|---|---|---|---|
| 5.1 | Policies for information security | Yes | partial | Draft policy exists but not approved by management |
| 5.2 | Information security roles and responsibilities | Yes | missing | No named information security owner |
| 5.3 | Segregation of duties | Yes | not_assessed | - |
| 5.4 | Management responsibilities | Yes | not_assessed | - |
| 5.5 | Contact with authorities | Yes | not_assessed | - |
| 5.6 | Contact with special interest groups | Yes | not_assessed | - |
| 5.7 | Threat intelligence | Yes | not_assessed | - |
| 5.8 | Information security in project management | Yes | not_assessed | - |
| 5.9 | Inventory of information and other associated assets | Yes | partial | POS terminals listed in spreadsheet; laptops and cloud accounts not listed |
| 5.10 | Acceptable use of information and other associated assets | Yes | missing | - |
| 5.11 | Return of assets | Yes | not_assessed | - |
| 5.12 | Classification of information | Yes | not_assessed | - |
| 5.13 | Labelling of information | Yes | not_assessed | - |
| 5.14 | Information transfer | Yes | not_assessed | - |
| 5.15 | Access control | Yes | partial | Shared admin login for POS back office across outlets |
| 5.16 | Identity management | Yes | partial | Staff accounts created ad hoc; no joiner/leaver process |
| 5.17 | Authentication information | Yes | missing | Passwords shared over WhatsApp |
| 5.18 | Access rights | Yes | not_assessed | - |
| 5.19 | Information security in supplier relationships | Yes | missing | POS and payroll vendors have no security clauses |
| 5.20 | Addressing information security within supplier agreements | Yes | not_assessed | - |
| 5.21 | Managing information security in the ICT supply chain | Yes | not_assessed | - |
| 5.22 | Monitoring, review and change management of supplier services | Yes | not_assessed | - |
| 5.23 | Information security for use of cloud services | Yes | partial | Google Workspace and Supabase in use; no cloud usage rules |
| 5.24 | Information security incident management planning and preparation | Yes | missing | No incident response plan |
| 5.25 | Assessment and decision on information security events | Yes | not_assessed | - |
| 5.26 | Response to information security incidents | Yes | not_assessed | - |
| 5.27 | Learning from information security incidents | Yes | not_assessed | - |
| 5.28 | Collection of evidence | Yes | not_assessed | - |
| 5.29 | Information security during disruption | Yes | not_assessed | - |
| 5.30 | ICT readiness for business continuity | Yes | missing | No tested recovery for POS reporting database |
| 5.31 | Legal, statutory, regulatory and contractual requirements | Yes | not_assessed | - |
| 5.32 | Intellectual property rights | Yes | not_assessed | - |
| 5.33 | Protection of records | Yes | not_assessed | - |
| 5.34 | Privacy and protection of PII | Yes | partial | Loyalty member phone numbers stored; UU PDP 27/2022 applies |
| 5.35 | Independent review of information security | Yes | not_assessed | - |
| 5.36 | Compliance with policies, rules and standards for information security | Yes | not_assessed | - |
| 5.37 | Documented operating procedures | Yes | not_assessed | - |
| 6.1 | Screening | Yes | not_assessed | - |
| 6.2 | Terms and conditions of employment | Yes | not_assessed | - |
| 6.3 | Information security awareness, education and training | Yes | missing | No security awareness training for outlet staff |
| 6.4 | Disciplinary process | Yes | not_assessed | - |
| 6.5 | Responsibilities after termination or change of employment | Yes | not_assessed | - |
| 6.6 | Confidentiality or non-disclosure agreements | Yes | implemented | NDA included in employment contract |
| 6.7 | Remote working | No | not_applicable | Outlet staff do not work remotely; head office staff use company laptops on site only |
| 6.8 | Information security event reporting | Yes | not_assessed | - |
| 7.1 | Physical security perimeters | Yes | implemented | Outlets locked after hours; CCTV at cashier |
| 7.2 | Physical entry | Yes | not_assessed | - |
| 7.3 | Securing offices, rooms and facilities | Yes | not_assessed | - |
| 7.4 | Physical security monitoring | Yes | not_assessed | - |
| 7.5 | Protecting against physical and environmental threats | Yes | not_assessed | - |
| 7.6 | Working in secure areas | Yes | not_assessed | - |
| 7.7 | Clear desk and clear screen | Yes | partial | Cashier screens left logged in during breaks |
| 7.8 | Equipment siting and protection | Yes | not_assessed | - |
| 7.9 | Security of assets off-premises | Yes | not_assessed | - |
| 7.10 | Storage media | Yes | not_assessed | - |
| 7.11 | Supporting utilities | Yes | not_assessed | - |
| 7.12 | Cabling security | Yes | not_assessed | - |
| 7.13 | Equipment maintenance | Yes | not_assessed | - |
| 7.14 | Secure disposal or re-use of equipment | Yes | not_assessed | - |
| 8.1 | User endpoint devices | Yes | partial | Company laptops without disk encryption |
| 8.2 | Privileged access rights | Yes | missing | Owner and IT share one superuser account |
| 8.3 | Information access restriction | Yes | not_assessed | - |
| 8.4 | Access to source code | Yes | not_assessed | - |
| 8.5 | Secure authentication | Yes | partial | MFA on email only; not on Supabase or GitHub |
| 8.6 | Capacity management | Yes | not_assessed | - |
| 8.7 | Protection against malware | Yes | implemented | Windows Defender enabled on all office PCs |
| 8.8 | Management of technical vulnerabilities | Yes | missing | No patch schedule for outlet PCs |
| 8.9 | Configuration management | Yes | not_assessed | - |
| 8.10 | Information deletion | Yes | not_assessed | - |
| 8.11 | Data masking | Yes | not_assessed | - |
| 8.12 | Data leakage prevention | Yes | not_assessed | - |
| 8.13 | Information backup | Yes | partial | Daily database backup but restore never tested |
| 8.14 | Redundancy of information processing facilities | Yes | not_assessed | - |
| 8.15 | Logging | Yes | missing | No central logs for internal web apps |
| 8.16 | Monitoring activities | Yes | not_assessed | - |
| 8.17 | Clock synchronization | Yes | not_assessed | - |
| 8.18 | Use of privileged utility programs | Yes | not_assessed | - |
| 8.19 | Installation of software on operational systems | Yes | not_assessed | - |
| 8.20 | Networks security | Yes | not_assessed | - |
| 8.21 | Security of network services | Yes | not_assessed | - |
| 8.22 | Segregation of networks | Yes | not_assessed | - |
| 8.23 | Web filtering | Yes | not_assessed | - |
| 8.24 | Use of cryptography | Yes | implemented | HTTPS on all web apps via Vercel |
| 8.25 | Secure development life cycle | Yes | partial | Code in GitHub; no review or security checks before deploy |
| 8.26 | Application security requirements | Yes | not_assessed | - |
| 8.27 | Secure system architecture and engineering principles | Yes | not_assessed | - |
| 8.28 | Secure coding | Yes | partial | Secrets sometimes committed to repositories |
| 8.29 | Security testing in development and acceptance | Yes | not_assessed | - |
| 8.30 | Outsourced development | Yes | not_assessed | - |
| 8.31 | Separation of development, test and production environments | Yes | not_assessed | - |
| 8.32 | Change management | Yes | missing | Production changes deployed directly from laptop |
| 8.33 | Test information | Yes | not_assessed | - |
| 8.34 | Protection of information systems during audit testing | Yes | not_assessed | - |
