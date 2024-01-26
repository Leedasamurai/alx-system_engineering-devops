# Web Infrastructure Project

## Overview

This project demonstrates a basic web infrastructure setup with a focus on simplicity and a LAMP stack (Linux, Apache, MySQL, PHP/Python/Perl). The infrastructure includes one server hosting a website accessible via www.foobar.com.

## Components

1. **Server:**
   - A physical or virtual machine responsible for hosting the entire infrastructure.

2. **Nginx Web Server:**
   - Handles HTTP requests.
   - Serves static content and acts as a reverse proxy.

3. **Application Server:**
   - Executes application code, generates dynamic content.
   - Communicates with the MySQL database.

4. **Application Code Base:**
   - The codebase of the web application (PHP/Python/Perl).

5. **MySQL Database:**
   - Stores and manages data for the website.

6. **Domain Name: www.foobar.com**
   - Human-readable address for the website.
   - DNS translates to the server's IP.

## How to Use

1. **Setup:**
   - Clone this repository to your local machine.

2. **Configuration:**
   - Update configuration files as needed.
   - Ensure server IP is correctly set in DNS records.

3. **Deployment:**
   - Deploy the application code and database schema to the server.

4. **Run:**
   - Start the web and application servers.

5. **Access:**
   - Open a browser and go to www.foobar.com.

## Specifics of the Infrastructure

- **Communication:**
  - The server communicates with user computers using HTTP or HTTPS.

- **DNS Record:**
  - The "www" subdomain is configured with an A record in DNS.

## Issues with the Infrastructure

1. **Single Point of Failure (SPOF):**
   - Any component failure results in website inaccessibility.

2. **Downtime During Maintenance:**
   - Deploying new code may require web server restart, causing downtime.

3. **Scalability Concerns:**
   - Limited ability to handle increased traffic.

## Author

- Lesego Phuku <lesegoleemac@gmail.com>

Feel free to explore the project, contribute, and address the identified issues for a more robust web infrastructure.


