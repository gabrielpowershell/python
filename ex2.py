#! /usr/bin/env python3

"""
This program terminate instances if proper tag is not used

"""

import time
import boto3

start_time = time.time()
ec2 = boto3.resource('ec2')
ec2_client =  boto3.client('ec2')
tag_deparment = ['Finance', 'Marketing', 'HumanResources', 'Research'] # Your departments
shutdown_instance = False


for instance in ec2.instances.all():
    instance_state = instance.state['Name']
    if instance_state == ('running' or 'pending'):
        for tags in instance.tags:
            for department in tag_deparment:
                if tags['Value'] == department:
                    shutdown_instance = False
                    break
                else:
                    shutdown_instance = True
                    
        print('The following instance will be shutdown', instance.id, 'Shutdown = ', shutdown_instance)
        if shutdown_instance is True:
            ec2_client.stop_instances(
                InstanceIds = [instance.id],
                Force = True
            )
