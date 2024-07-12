import scapy.all as scapy

srcip = str(input("source_ip: "))
dstip = str(input("destination_ip: "))
pack = int(input("pack_num: "))

try:
   for i in range(pack):
      scapy.send(scapy.IP(src=srcip, dst=dstip) / scapy.ICMP())
except Exception as e:
   print(f"An error occured: {e}")
