# Load Balancer Configuration with Web Server Redundancy

## Introduction
This project enhances our web infrastructure by introducing redundancy for our web servers and setting up a load balancer. By doubling the number of web servers and configuring them behind a load balancer, we aim to increase our infrastructure's traffic handling capabilities and reliability. Automation scripts in Bash and configurations using Puppet are utilized for efficient replication and setup across new Ubuntu servers.

## Requirements

### General:
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All Bash script files must be executable
- Bash scripts must pass `Shellcheck` (version 0.3.7) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose
- Puppet manifests must pass `puppet-lint` without any errors

### Specific:
- Configure Nginx on web servers to add a custom HTTP header `X-Served-By`
- Install and configure HAProxy to distribute traffic to web servers
- Use Puppet to automate the configuration of custom HTTP response headers

## Project Files

| File Name                                 | Description                                                        |
|-------------------------------------------|--------------------------------------------------------------------|
| `0-custom_http_response_header`           | Bash script to configure a brand new Ubuntu machine with custom Nginx header |
| `1-install_load_balancer.sh`              | Bash script to install and configure HAProxy on `lb-01` server    |
| `2-puppet_custom_http_response_header.pp` | Puppet manifest to configure Nginx with a custom HTTP header on Ubuntu servers |

## Usage

### Bash Scripts

Ensure the bash scripts are executable:

```bash
chmod +x 0-custom_http_response_header
chmod +x 1-install_load_balancer.sh

## Authour

Lesego Phuku
