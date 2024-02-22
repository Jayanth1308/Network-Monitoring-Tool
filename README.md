# Network Monitoring and Notification Script

This Python script monitors the network connectivity status of specified nodes and sends email notifications when any node becomes unreachable.

## Features

- Accepts a list of node IP addresses or hostnames as input.
- Uses the ping command to check the connectivity status of each node.
- Logs the results to a file with timestamps.
- Implements an option to send an email notification if any node is unreachable.
- Provides proper error handling and logging of results.
- Utilizes Boto3 to send email notifications via Amazon SES.
- Clean and well-structured code with appropriate comments.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3 installed on your system.
- Boto3 library installed (`pip install boto3`).
- AWS credentials configured on your system with permissions to send emails via Amazon SES.
- Verified sender email address in Amazon SES.

## Usage

1. Clone this repository to your local machine.

2. Update the AWS region and sender email address in the script (`network_monitor.py`) with your own values.

3. Add the node IP addresses or hostnames you want to monitor to the `nodes_to_monitor` list in the script.

4. Run the script using Python:


5. The script will start monitoring the specified nodes for network connectivity. It will print the status of each node to the console and log the results to the `network_status.log` file. If any node becomes unreachable, it will send an email notification.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
