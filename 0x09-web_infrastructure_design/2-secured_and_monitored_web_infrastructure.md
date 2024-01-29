# Secured and Monitored Distributed Web Infrastructure

![Image of a secured and monitored infrastructure](https://i.imgur.com/skC2ksP.png)

[Visit Board](https://miro.com/app/board/uXjVOfNFwbY=/)

## Description

This is a 3-server website that is protected, monitored, and accessible.

## Specific Information About This Structure

+ **Target Firewall:**
  - The firewall acts as an intermediary between internal and external networks, blocking traffic that meets predefined criteria. This protects the network, particularly the web server, from unwanted and unauthorized access, safeguarding user rights.

+ **Purpose of SSL Certificate:**
  - SSL certificates are utilized to encrypt traffic between the web server and other networks. This measure prevents man-in-the-middle attacks (MITM) and network sniffers from intercepting and analyzing the traffic between the web server and the external network. SSL certificates ensure confidentiality, data integrity, and secure identity verification.

+ **Purpose of Monitoring Service:**
  - A monitoring service is employed to observe and analyze server performance and network operations. It assesses overall health, providing administrators with alerts if servers deviate from expected performance metrics. The monitoring tool evaluates server availability, measures response time, and notifies administrators of errors, including incorrect/missing data and security breaches/violations.

## Issues with This Operation

+ **Setting SSL at the Load Balancer Level:**
  - Terminating SSL at the load balancer level results in unencrypted traffic between the load balancer and the web server. This poses a security risk, potentially exposing sensitive information.

+ **Problem with Having a MySQL Server:**
  - A single MySQL server lacks scalability and can become a point of failure for the website. In the event of server failure, critical operations like adding or removing users may be compromised.

+ **Servers with Same Hardware Configuration:**
  - Servers with identical hardware configurations may lead to resource contention, with CPU, memory, and I/O competing for resources. This contention can result in poor performance and make troubleshooting challenging. Additionally, a setup with uniform components is not easily scalable.
