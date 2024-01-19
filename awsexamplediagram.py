from diagrams import Cluster, Diagram
from diagrams.aws.network import VPC
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53, ELB

with Diagram("AWS Networking/Host Diagram", show=False):
    with Cluster("Region 1"):
        with Cluster("Public VPC"):
            web1 = EC2("Web Server\n(Apache)")
            Route53("HTTP/HTTPS\nAccess") >> ELB("Load Balancer") >> web1

        with Cluster("Private VPC"):
            bastion1 = EC2("Bastion Host")
            db1 = RDS("RDS Instance")
            bastion1 - db1

    with Cluster("Region 2"):
        with Cluster("Public VPC"):
            web2 = EC2("Web Server\n(Apache)")
            Route53("HTTP/HTTPS\nAccess") >> ELB("Load Balancer") >> web2

        with Cluster("Private VPC"):
            bastion2 = EC2("Bastion Host")
            db2 = RDS("RDS Instance")
            bastion2 - db2

    web1 >> bastion1
    web2 >> bastion2
    bastion1 >> db1
    bastion2 >> db2
