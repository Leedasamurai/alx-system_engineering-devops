# Simple Web Stack

![Web Stack Diagram](https://i.imgur.com/AgPl4U3.png)

## Description

This is a straightforward web infrastructure hosting a website accessible through `www.foobar.com`. The absence of firewalls and SSL certificates exposes the server's network, and components like the database and application server share the server's resources (CPU, RAM, and SSD).

## Specifics About This Infrastructure

+ **What a server is.**<br/>
  A server acts as the backbone, providing services to other computers known as *clients*.

+ **The role of the domain name.**<br/>
  The domain name serves as a user-friendly alias for an IP address, facilitating easier recognition and memorization. DNS maps the IP address and domain name alias.

+ **The type of DNS record `www` is in `www.foobar.com`.**<br/>
  `www.foobar.com` utilizes an **A record**. You can verify this with `dig www.foobar.com`. In this setup, an **A** record is used, signifying an Address Mapping record.

+ **The role of the web server.**<br/>
  The web server, a vital software/hardware, handles HTTP requests and responds with requested content or error messages.

+ **The role of the application server.**<br/>
  Responsible for installing, operating, and hosting applications and services, the application server facilitates the hosting and delivery of high-end applications for end users and organizations.

+ **The role of the database.**<br/>
  The database maintains organized information, easily accessible, managed, and updated.

+ **What the server uses to communicate with the client.**<br/>
  Communication between the server and the client occurs via the TCP/IP protocol suite over the internet network.

## Issues With This Infrastructure

+ **Multiple SPOF (Single Point Of Failure) in this infrastructure.**<br/>
  For instance, if the MySQL database server goes down, the entire site becomes inaccessible.

+ **Downtime when maintenance needed.**<br/>
  Maintenance checks require components to be taken down, causing downtime. With only one server, the website experiences downtime during maintenance.

+ **Cannot scale if there's too much incoming traffic.**<br/>
  Scaling is challenging as the infrastructure relies on a single server, which can quickly become resource-constrained or slow down under heavy traffic.

