"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import aws

sg = aws.ec2.vpcSecurityGroupIds(
    "web-sg",
    description = "web sg for HTTP",
    ingress=[
        {
            'protocol': 'tcp',
            'from_port': 80,
            'to_port': 80
            'cidr_blocks': ['0.0.0.0/0']
        }
    ]
)

ami = aws.get_ami(
    most_recent="true",
    owner=['amazon'],
    filters=[{'name': 'name', 'values': ['amzn-ami-hvm-*']}]
)

user_data = """
#!/bin/bash
uname -n > index.html
nohup python -m SimpleHTTPServer 80 &
"""


instance = aws.ec2.Instance(
    "pulumi-webapp",
    instance_type="t2.micro",
    security_group=[sg.name],
    ami = ami.id,
    user_data = user_data
)

pulumi.export("web-app-ip", instance.public_ip)