# Distributed Web Infrastructure

![Image of a distributed web infrastructure](https://i.imgur.com/2MWsRew.png)

[Visit Board](https://miro.com/app/board/uXjVOfI6jcU=/)

## Description

This is a web job designed to distribute some of the load to replica servers, assisted by a load balancer responsible for balancing the workload between two servers (master and replica). The objective is to reduce traffic on the original server.

## Detailed Information About This Infrastructure


+ **additional components:**
  - 2 new servers are used to distribute the load and to greatly enhance redundency.
  - Load balancers improve application performance by increasing response time and reducing network latency. Distribute the load evenly across servers to improve application performance. Route requests to closer servers to reduce latency.

+ **Load Balancer Configuration and Algorithm:**
  - The HAProxy load balancer is configured with a round-robin deployment algorithm. This algorithm selects each server based on their weight, ensuring a smooth and fair distribution of server time. As a dynamic algorithm, round-robin allows the server load to change dynamically.

+ **Load Balancer Settings:**
  - The HAProxy load balancer is enabled in an active-passive configuration. In an active-passive setup, not all nodes are actively serving requests at all times. For instance, in a two-node configuration, if the first node is active, the second node remains passive or in standby. The subsequent passive node can become active if the preceding one is inactive.

+ **Database Master (Master-Slave) Group Operation:**
  - The master replica setting configures one server as the master, and the others follow the master's model. While the master server can handle read/write requests, the replica servers can only perform read requests. Data synchronization occurs when the master server executes a write operation.

+ **Difference Between Master Node and Replica Node:**
  - The master node is responsible for all read and write operations, serving as the primary workhorse. In contrast, the replica node can only perform read operations, reducing the load on the master node for read-intensive tasks.

## Issues With This Architecture

+ **Single Points of Failure (SPOFs):**
  - There are too many single points of failure. For example, if the main MySQL database server goes down, the entire site loses the ability to make changes, such as adding or removing users. Servers with load balancers and application servers connected to the main database server are also vulnerable.

+ **Security Issues:**
  - Data sent over the network is not encrypted using an SSL certificate, potentially exposing it to eavesdropping. Additionally, none of the servers have a firewall installed, leaving no means to block unauthorized IPs.

+ **Lack of Maintenance:**
  - The infrastructure lacks monitoring, making it impossible to know the status of each server. Without monitoring, it becomes challenging to identify and address potential performance issues or failures promptly.
