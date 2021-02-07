import pulumi
import pulumi_aws as aws

ami = aws.get_ami(
    most_recent ="true",
    owners=["137112412989"], # aws temp
    filters=[{"name": "name", "values":["amzn-ami-hvm-*-x86_64-ebs"]}]
)

group = aws.ec2.SecurityGroup(
    "web-security group",
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'icmp', 'from_port': 8, 'to_port': 0, 'cidr_blocks': ['0.0.0.0/0']},
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0']} 
    ]
)

pulumi.export("ami_id", ami.id)