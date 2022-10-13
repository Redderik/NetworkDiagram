import getpass
import csv

def netmiko_connect():
    #Ask input for username.
    username = input('Username: ')
    #Ask input for user password. Getpass obscures input.
    password = getpass.getpass(prompt='Password: ')
    #If your switch secret is different that your connection password, uncomment the secret = getpass line.
    secret = password
    #secret = getpass.getpass(prompt='Secret: ')
    #Establish list to hold all IPs for network equipment.
    networklist = []
    #Opens network_IP.csv which containes all IPs to connect to and build Flowchart.
    with open('network_IP.csv', newline='') as csvfile:
        networkcsv = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #This is basic validation to ensure it is actually an iPv4 address. It watches for less than 12 integers in the list, and counts for 3 decimal points.
        for row in networkcsv:
            decimalcount = ''.join(row).count('.')
            digitcount = sum(c.isdigit() for c in ''.join(row))
            if decimalcount == 3 and digitcount <= 12:
                networklist.append(''.join(row))
    #Establishes list of switches that will be connected to by Netmiko.
    switchlist = []
    for i in range(len(networklist)):
        switch = {
            'device_type': 'cisco_ios',
            'host': networklist[i],
            'username': username,
            'password': password,
            'secret': password,
        }
        switchlist.append(switch)
    #Returns all our switches
    return switchlist