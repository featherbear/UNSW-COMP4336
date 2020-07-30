---
title: "Mobile IP"
date: 2020-07-29T09:00:00+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# The Challenge

## IP World

A mesh of subnets interconnected by routers

* A device has a unique IP to connect
* The IP address must carry the subnet prefix

### The Issue

Since the IP address carries the subnet prefix, when it changes subnet (connecting to different cells) - the IP address must change!

## Quasi-Mobility

Internet access from any subnet, but **cannot move across subnet boundaries**

## Full Mobility

Internet access from any subnet, and is able to move across subnet boundaries

## DHCP-WLAN

* Idea - Host-based Routing
  * The entire 32 bits of the IP address used for routing
  * IP can therefore remain the same
  * But will need a GIANT routing table

# The Solution - IP Mobility

![](2020-07-31_00-12-59.png)

**Location server** tracks the location (subnet) of a device.  
The location server can then help routers forward packets correctly

IETF RFC5944 (preceded  by RFC3344 (2005))

## Dual IP Address

A mobile host has TWO IP addresses  

* Home address - Permanent (static) address
* Care of address - Temporary address

Connections to the permanent address are routed to the temporary address.  
Home address is stored in DNS tables.

## Agents

A router contains a home agent and foreign agent software that coordinates the forwarding.

### Home Agent

???

### Foreign Agent

Accepts packets from home agents, and delivers them to visiting mobile hosts.

#### Foreign Agent CoA

Another router (for a subnet) that has several IP addresses.  
The mobile device will then use of these IP addresses as its Care of Address. 

Several devices can use the same Care of Address.  

No new IP addresses consumed - DHCP **not** used!  
Mobile connects using its permanent address

#### Co-located CoA

* IP address exclusive to the mobile device

A foreign agent is optional, and may not be needed.  

When moving to a different subnet, a new IP is assigned via DHCP

---

## Foreign Agent Process

* Phase 1 - Agent Discovery (or DHCP for Co-located CoA)
* Phase 2 - Registration
* Phase 3 - Data Transfer

### Agent Discovery (Foreign Agent **Only**)

IP Addresses of the Foreign Agent is advertised over ICMP.  
Mobile devices wait for these periodic advertisements.  
The mobile can also request an address directly from the router.

The mobile sends its permanent IP and MAC address to the foreign agent.  
The foreign agent relays this to the home agent

### Registration

UDP Port 434

**IP Handoff**  

Registration may take a long time...  

**Solution 1**: Wait for registration.  
**Solution 2**: Predict movement and pre-register for quick handover.  

**Issues - Latency**

* Double crossing - (remote host goes over the internet to the home agent, which communicates over the internet to the mobile host)
* Triangular routing - (remote host goes over the internet to the home agent, which goes to mobile host)

**Mitigations**  

* Route optimisation - Home Agent notifies the remote host of the new address
  * However, may lead to sync issues (old address)
  * Also will require new functionality of the FA software

### Data Transfer

IP-in-IP Protocol Encapsulation.

In the parent IP packet, the `next protocol` value is also IP.


---

## Reverse Tunnelling

The remote host and mobile host ***could*** connect to each other directly, eliminating the need to go through the home agent.  
However a firewall mechanism called _ingress filtering_ will prevent this from working.

Ingress filtering -> Prevents packets from passing only if the source address matches the packet origin.  

Due to this, data must go back from the mobile host through the home agent, into the remote host.

---

# Network Mobility

Consider an ***entire subnet*** that moves

## NEMO Standard

* Onboard Router
* Onboard Fixed Device - Does not need Mobile IP since it always communicates with a given Onboard Router
* Onboard User Device - Double IP tunnelling -> IP-in-IP-in-IP

## Multihoming

If the network infrastructure is unstable, there will be a bad quality of service to users.  
Multihoming involves connecting to a Home Agent over different network links.  

This allows load balancing and redundancy

# IPv6

Don't need DHCP, can use MAC address to generate its IP address!  
_Decreases the registration time_!  

IPv6 Type 1 - src and destination

IPv4 needs IP-in-IP tunneling to carry both sets of address pairs.  
IPv6 Type 2 - can include extra address pairs! Can also mitigate ingress filtering restrictions!

***An IPv6 implementation is more efficient than an 'upgraded IPv4' scheme, due to its extra header capability***

---

# Proxy Mobile IP

> Not for global networks, only for campus deployment  
> **Does _not_ use the internet**  
> **Does _not_ need client-side software**

To support Mobile IP, user devices need software and firmware upgrades.  

* Cost overhead
* Admin overhead
* Deployment overhead

Proxy Mobile IPs allows user devices to not require any special software.  
The network edge (access points) install a Mobile IP client-proxy, which is transparent to the clients.  

* LMA - Local Mobility Anchor
  * Single device in the network core
  * Connects to multiple MAGs

* MAG - Mobile Access Gateway
  * In the AP
  * Notifies the MAG of its connected hosts

Data from the WAN first goes to the LMA.  
The MAG stations see if the Mobile Host is attached to them, and notifies the LMA.  
The LMA then forwards the packet to that specific MAG, which sens the packet to the Mobile Host.