# The Pentester Automation Tool

## Description
This application automates most of the penetration testing tasks using the command line. It automates DNS information ,Gathering emails, WHOIS, Files, SocialMedia, Scan for live hosts, Port scan, Vulnerability assessment, Brute-force attack, Scan for Web site security as well.
This application can be used only on the author's favorite OS "Kali Linux", it will not work on other Linux versions unless you install all the tools manually.

## Contributing
If you're willing to help on this project ,you're welcomed to send your suggestions to the owner at: gus.khawaja@guskhawaja.me

##Demo
A full tutorial of the source code architecture is available at Pluralsight:
https://www.pluralsight.com/courses/penetration-testing-automation-using-python-kali-linux


## Information Gathering
  ```DNS
  To get information about a dns:
  $python pat.py --company [YourClientDomainName] -dns
  ```
  
   ```Emails
  To get a list of email addresses:
  $python pat.py --company [YourClientDomainName] -emails
  ```
  
   ```WHOIS
  To get information about WHOIS:
  $python pat.py --company [YourClientDomainName] -whois
  ```
  
   ```Files
  To get a list of leaked files on the internet:
  $python pat.py --company [YourClientDomainName] -files
  ```
  
   ```SocialMedia
  To get information about your client social media:
  $python pat.py --company [YourClientDomainName] -socialmedia
  ```
  
   ```WebSearch
  To get information about your client using the search engines:
  $python pat.py --company [YourClientDomainName] -websearch
  ```
  
## Scanning
   ```LiveHosts
  To scan for live hosts:
  $python pat.py --company [YourClientDomainName] -ip [NetworkIPAddress/Range] -livehosts
  ```
  
   ```PortScan
  For Port Scanning:
  $python pat.py --company [YourClientDomainName] -ip [NetworkIPAddress/Range] -portscan
  ```
  
## Vulnerability Assessment
   ```VulnsScan
  Vulnerability Scan:
  $python pat.py --company [YourClientDomainName] -ip [NetworkIPAddress/Range] -vulns
  ```
  
   ```BruteForce
  To brute-force the services on the client host machine(s):
  $python pat.py --company [YourClientDomainName] -ip [NetworkIPAddress/Range] -bruteforce
  ```
## Web Application Scan  
   ```WAF
  To get information about the existence of Web Application Firewall (WAF):
  $python pat.py --company [YourClientDomainName] --url [WebServerUrl] -waf
  ```
  
   ```SSL
  To get information about the server SSL/TLS security:
  $python pat.py --company [YourClientDomainName] --url [WebServerUrl] -ssl
  ```
  
   ```LoadBalance
  To get information about the webserver load balancing:
  $python pat.py --company [YourClientDomainName] --url [WebServerUrl] -loadbalance
  ```
  
  ```WebVulns
  Web Server Vulnerability Assessment:
  $python pat.py --company [YourClientDomainName] --url [WebServerUrl] -webvulns
  ```
  