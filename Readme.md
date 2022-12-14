# Network Diagram
A basic network diagram utilizing CDP neighbors, and draw.io.

This was primarily intended to pull information in a cisco environment for just Core, Distribution, and Access switches, but if you include access switches as well in the .csv it should collect anything that comes up in CDP.

This utilizes a list of IPs from network_IP.csv and netmiko to log in to each device, and collect the cdp neighbor information from it.

TTP parses this into a .drawio file you can edit at https://app.diagrams.net.

Once you have it in an editor, I've found Arrange -> Layout -> Organic provides the best results, depending on how many devices you have connected to.

If you'd rather use a locally installed program like yED Graph Editor, you'll just need to change the module in line 25 of NetDia.py to:

module = "yED"

and also change line 31 to:

\<out returner="file" url="./Output/" filename="cdp_diagram.graphml"/>

Hopefully someone else finds this useful!

![Example](https://github.com/Redderik/NetworkDiagram/raw/main/cdp_diagram.png)