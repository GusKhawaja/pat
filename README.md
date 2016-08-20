# The Pentester Automation Tool

## Description
This application automates most of the penetration testing tasks using the command line. It automates DNS,Gathering emails, WHOIS, Files, SocialMedia, Scan for live hosts, Port scan, Vulnerability assessment, Brute-force attack, Scan for Web site security as well.

## Contributing
If you're willing to help on this project ,you're welcomed to send your suggestions to the owner at: gus.khawaja@guskhawaja.me

## Information Gathering
  ```DNS
  To get information about a dns:
  $python pat.py --company [yourclientdomainname] -dns
  ```
  
   ```Emails
  To get a list of email addresses:
  $python pat.py --company [yourclientdomainname] -emails
  ```
  
   ```WHOIS
  To get information about WHOIS:
  $python pat.py --company [yourclientdomainname] -whois
  ```
  
   ```Files
  To get a list of leaked files on the internet:
  $python pat.py --company [yourclientdomainname] -files
  ```
  
   ```SocialMedia
  To get information about your client social media:
  $python pat.py --company [yourclientdomainname] -socialmedia
  ```
  
   ```WebSearch
  To get information about your client using the search engines:
  $python pat.py --company [yourclientdomainname] -websearch
  ```
  
## Scanning
   ```LiveHosts
  To scan for live hosts:
  $python pat.py --company [yourclientdomainname] -ip [IPAddress/Range] -livehosts
  ```
  
   ```PortScan
  For Port Scanning:
  $python pat.py --company [yourclientdomainname] -dns -ip [IPAddress/Range] -portscan
  ```
  
## Vulnerability Assessment
   ```VulnsScan
  Vulnerability Scan:
  $python pat.py --company [yourclientdomainname] -dns -ip [IPAddress/Range] -vulns
  ```
  
   ```BruteForce
  To brute-force the services on the client host machine(s):
  $python pat.py --company [yourclientdomainname] -dns -ip [IPAddress/Range] -bruteforce
  ```
## Web Application Scan  
   ```WAF
  To get information about the existence of Web Application Firewall (WAF):
  $python pat.py --company [yourclientdomainname] -dns -ip [IPAddress/Range] -waf
  ```
  
   ```SSL
  To get information about the server SSL/TLS security:
  $python pat.py --company [yourclientdomainname] -dns -ip [IPAddress/Range] -ssl
  ```
  
   ```LoadBalance
  To get information about the webserver load balancing:
  $python pat.py --company [yourclientdomainname] -dns -ip [IPAddress/Range] -loadbalance
  ```
  