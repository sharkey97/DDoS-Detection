# DDoS-Detection
Python implementation of DDoS detector deployable on Linux

<h1> Python DoS Detection Tool </h1>

The following code extracts are implemented using Python version 2.7.18. If using on Python3, replace ‘raw_input’ with ‘input’. The code is designed for implementation on a Linux operating system but can be used to monitor a separate Windows machine by specifying the IP Address, as is done here. No installation is required, run the program through a Linux terminal using the command >>> python [filename.py]
Hostnames can also be automatically set to test the effect of a DoS on the host machine (Uncomment lines 3 and 4 and comment out line 5 to do this). However, for testing purposes, a manual address was set.
The line ‘print row.strip()’ Can be uncommented to view all packets in real-time also. For testing and visualisation purposes this was left commented out. The attack was carried out using Metasploit inside a Kali Linux VM, implementing the built-in SYNFLOOD tool. The Target was the host computer and was carried out over a bridged network adapter. Firewalls had to be modified on the host to allow incoming IPv4 TCP packets from VirtualBox. IP address shown, targeted, and blocked is the same and is done so for demonstration purposes only, a real-world scenario would block a foreign address, not the host address seen here.

<h3> Output while an attack is taking place </h3>

<p align="center">
  <img src="https://user-images.githubusercontent.com/45834305/152824201-a625b750-3a71-4e75-a498-27c37d045192.png">
</p>

<h3> Output during no attack </h3>

<p align="center">
  <img src="https://user-images.githubusercontent.com/45834305/152824379-374796fc-d0b8-4837-9f5f-371f8739e4be.png">
</p>
