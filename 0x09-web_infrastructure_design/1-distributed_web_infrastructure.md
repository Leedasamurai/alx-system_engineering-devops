# Distributed Web Infrastructure

![Image of a distributed web infrastructure](https://i.imgur.com/2MWsRew.png)

[Visit Board](https://miro.com/app/board/uXjVOfI6jcU=/)

## Description

This distributed web infrastructure aims to optimize performance by intelligently distributing traffic between a primary server and a replica server. The load-balancer plays a crucial role in balancing the workload and enhancing overall system reliability.

## Specifics About This Infrastructure

+ **Why Each Element is Added:**

  - **Nginx Web Server & Application Server:**
    - Handles HTTP requests, serves static content, and executes application code.

  - **HAproxy (Load-Balancer):**
    - Distributes incoming requests across multiple servers, improving performance and reliability.

  - **MySQL Database:**
    - Stores and manages data for the website.

+ **Distribution Algorithm of HAproxy:**

  - **Algorithm Used: Round Robin.**
    - The Round Robin algorithm distributes incoming requests equally among the available servers, ensuring a balanced load distribution.

+ **Load-Balancer Setup:**

  - **Active-Active Setup:**
    - Both servers actively handle incoming requests simultaneously.
    - Enhances performance and availability.

+ **Database Primary-Replica (Master-Slave) Cluster:**

  - **How It Works:**
    - The Primary Node handles write operations and replicates data to the Replica Node.
    - The Replica Node handles read operations and stays synchronized with the Primary Node.

  - **Difference Between Primary and Replica in Regard to the Application:**
    - **Primary Node:**
      - Handles write operations, making it suitable for tasks like inserting, updating, or deleting data.
    - **Replica Node:**
      - Handles read operations, serving queries and requests for data without affecting the write operations on the Primary Node.
      - Provides redundancy for improved reliability.

## Issues With This Infrastructure

+ **Single Point of Failure (SPOF):**

  - **Load-Balancer:**
    - If the load-balancer (HAproxy) fails, it becomes a single point of failure.

+ **Security Issues:**

  - **Lack of Firewall:**
    - Exposes servers and services to potential security threats.

  - **No HTTPS:**
    - Communication between the client and servers is not encrypted, risking data integrity and privacy.

+ **No Monitoring:**

  - Lack of monitoring tools or systems makes it challenging to identify and address performance issues or potential failures promptly.

This infrastructure design addresses performance and redundancy concerns but introduces vulnerabilities due to missing security measures and monitoring. Enhancements such as implementing a firewall, HTTPS, and monitoring tools are necessary to improve overall reliability and security.

