import socket
# import termcolor

def scan(target, ports):
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1, ports):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+]Port " + str(port) + " Open")
        sock.close()
    except:
        pass

targets = input("[*] Enter Targets To Scan(split them by a commma): ")
ports = int(input("[*] Enter How Many Ports To Scan: "))
if ',' in targets:
    # print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets,ports)
