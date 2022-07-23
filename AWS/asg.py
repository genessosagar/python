import subprocess
import os

cmd = "aws autoscaling describe-auto-scaling-groups --query 'AutoScalingGroups[].[AutoScalingGroupName]' --profile profile-name"
asg = subprocess.getoutput(cmd)
l1 = list(asg.split("\n"))
for i in l1:
    os.system("aws autoscaling update-auto-scaling-group --auto-scaling-group-name {} --min-size 0 --max-size 2 --desired-capacity 0 --profile profile-name".format(i))
