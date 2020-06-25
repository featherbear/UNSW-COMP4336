#!/bin/sh

# Extract only the first 60 seconds worth of packets for frames with the SSID of z5206677

mkdir processed
find . -maxdepth 1 -iname "*.pcapng" -type f -exec tshark -r "{}" -Y "frame.time_relative <= 60 && wlan.ssid == \"z5206677\"" -w "processed/{}" \; 