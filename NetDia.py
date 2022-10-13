from ttp import ttp
from netmiko import ConnectHandler
from netmiko_connect import netmiko_connect

#The TTP Template that spits out our .drawio file after collecting the switch data.
ttptemplate = """
<vars>
hostname='gethostname'
IfsNormalize = {
                'Ge': ['^GigabitEthernet'],
                'Te': ['^TenGigabitEthernet']
}
</vars>

<group name="cdp*" expand="">
Device ID: {{ target.id }}
  IP address: {{ target.top_label }}
Platform: {{ target.bottom_label | ORPHRASE }},  Capabilities: {{ ignore(ORPHRASE) }}
Interface: {{ src_label | resuball(IfsNormalize) }},  Port ID (outgoing port): {{ trgt_label | ORPHRASE | resuball(IfsNormalize) }}
{{ source | set("hostname") }}
</group>

<output format="n2g" load="python">
path = "cdp"
module = "drawio"
node_duplicates = "update"
method = "from_list"
algo = "kk"
</output>

<out returner="file" url="./Output/" filename="cdp_diagram.drawio"/>
"""
switchlist = netmiko_connect()

#Establishes cdp_neigh_list, which will hold the string data for each switch IP targeted in the CSV file.
cdp_neigh_list = []
for i in range(len(switchlist)):
    connect = switchlist[i]
    #Uses netmiko to connect to switch using template assigned in "switchlist"
    net_connect = ConnectHandler(**connect)
    #Collects the CDP neighbor from the switch. Also adds the hostname/command entered into the switch. This allows 'gethostname' in the ttp_template to work properly.
    output = "<input load =\"text\">\n" + net_connect.find_prompt() + "show cdp neigh det \n" + net_connect.send_command("show cdp neigh det") + "\n</input>\n"
    cdp_neigh_list.append(output)
#This appends all of our collected data from the switches into ttptemplate.
#
ttp_template = "".join(cdp_neigh_list) + ttptemplate
print(ttp_template)
parser = ttp(template=ttp_template)
parser.parse()
print("Please check output folder for cdp_diagram.drawio file.")
