#!/usr/bin/env python

import boto3
import json

# Connect to AWS using the configured credentials
session = boto3.Session()
ec2_client = session.client("ec2", region_name="us-east-2")

# Get a list of running EC2 instances
response = ec2_client.describe_instances(
    Filters=[
        {"Name": "instance-state-name", "Values": ["running"]}
    ]
)

# Extract instance details from the response
instances = []
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instances.append(instance)

# Prepare the inventory in Ansible-compatible JSON format
inventory = {"_meta": {"hostvars": {}}}
ec2_group = {"hosts": []}  # Group for EC2 instances

for instance in instances:
    inventory["_meta"]["hostvars"][instance["InstanceId"]] = {
        "ansible_host": instance["PublicIpAddress"],
        "ansible_user": "ec2-user",
    }
    ec2_group["hosts"].append(instance["InstanceId"])

inventory["ec2"] = ec2_group

# Print the inventory as JSON
print(json.dumps(inventory))