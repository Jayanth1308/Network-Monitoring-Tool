import subprocess
import time
import boto3
from email.mime.text import MIMEText

def check_network(host):
    try:
        response = subprocess.call(['ping', '-c', '1', host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return response == 0
    except Exception as e:
        print(f"An error occurred while checking network status for {host}: {e}")
        return False

def send_notification(node):
    AWS_REGION = 'us-east-1' 
    SENDER_EMAIL = 'jayanth2k2@gmail.com'
    RECIPIENT_EMAIL = 'jayanth2k2@gmail.com'

    subject = f"Network Node Unreachable: {node}"
    body = f"The node {node} is unreachable."

    ses_client = boto3.client('ses', region_name=AWS_REGION)

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = SENDER_EMAIL
    message['To'] = RECIPIENT_EMAIL

    try:
        response = ses_client.send_raw_email(
            Source=SENDER_EMAIL,
            Destinations=[RECIPIENT_EMAIL],
            RawMessage={'Data': message.as_string()}
        )
        print(f"Email notification sent for unreachable node: {node}")
    except Exception as e:
        print(f"Failed to send email notification: {e}")

def log_status(timestamp, node, status):
    with open('monitor.log', 'a') as log_file:
        log_file.write(f"{timestamp} - Node {node} is {status}\n")

def monitor_nodes(nodes):
    while True:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        for node in nodes:
            status = "reachable" if check_network(node) else "unreachable"
            print(f"{timestamp} - Node {node} is {status}")
            log_status(timestamp, node, status)
            if status == "unreachable":
                send_notification(node)
        time.sleep(5)

if __name__ == "__main__":
    nodes_to_monitor = ["8.8.8.8", "8.8.4.4", "192.168.1.100"]  # List of nodes to monitor
    monitor_nodes(nodes_to_monitor)

