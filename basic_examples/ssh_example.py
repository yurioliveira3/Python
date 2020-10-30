from paramiko import SSHClient
from paramiko import AutoAddPolicy
from scp import SCPClient

#Define host's here
hosts = ('xx.xx.xx.xx','yy.yy.yy.yy');

ssh = SSHClient(); #Set SSH client
ssh.load_system_host_keys(); #Get SSH keys from know_hosts
ssh.set_missing_host_key_policy(AutoAddPolicy()); #If host is not recognized, auto add him

for h in hosts: #Iterate 
    ssh.connect(hostname=h, 
                port = '22',
                username='usr',
                password='pwd'
                );

    scp = SCPClient(ssh.get_transport()); #SCPCLient takes a transport with paramiko

    print ("Put files in host: ", h);
    if h == 'yy.yy.yy.yy': #Check if is a specify host
        scp.put('local_file', 'host_path');
    else: 
        scp.put('local_file', 'host_path');
    
    scp.close();

print("Process Completed!");