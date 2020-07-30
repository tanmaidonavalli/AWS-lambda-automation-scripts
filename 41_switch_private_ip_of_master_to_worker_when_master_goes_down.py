import boto3
master_id = "i-03454c58b1d97e20b"
slave_id = "i-08d4735b8a5e39f19"
secondary_ip = "172.31.34.200"
ec2_res = boto3.resource('ec2', 'ap-south-1')

# to check state of master, we are working on single instance hence create its object
primary_instance = ec2_res.Instance(master_id)
if primary_instance.state['Name'] == "running":
    print("master is up and running")
else:
    secondary_instance = ec2_res.Instance(slave_id)

    # to get network interface information of our ec2
    pnetwork_interface_info = primary_instance.network_interfaces_attribute[0]
    snetwork_interface_info = secondary_instance.network_interfaces_attribute[0]

    # to assign seconary ip, we need network interfaceid
    pnw_interface_id = pnetwork_interface_info["NetworkInterfaceId"]
    snw_interface_id = snetwork_interface_info["NetworkInterfaceId"]

    # to unassign we have to use client object
    ec2_cli = boto3.client('ec2', 'ap-south-1')
    ec2_cli.unassign_private_ip_addresses(
        NetworkInterfaceId=pnw_interface_id,
        PrivateIpAddresses=[secondary_ip]
    )
    ec2_cli.assign_private_ip_addresses(
        AllowReassignment=True,
        NetworkInterfaceId=snw_interface_id,
        PrivateIpAddresses=[secondary_ip]
    )
    print(f"Secondary Private ip '{secondary_ip}' of {primary_instance.id} is now assigned to {secondary_instance.id} ")