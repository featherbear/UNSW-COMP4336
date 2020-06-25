#/bin/sh

# Export the signal strength from the packets in the current directory

find . -maxdepth 1 -iname "*.pcapng" -type f -exec bash -c 'tshark -r "{}" -T fields -e frame.number -e frame.time -e wlan_radio.signal_dbm -E header=y -E separator=, -E quote=d -E occurrence=f > "{}.csv" ' \;
