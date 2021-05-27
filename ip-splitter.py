import ipaddress 
ip_block = "2001:00E0::/48"  #ip address to split 
prefix_len_difference=16 #this will result in the below /48 block to be splitted into /64 as prefix_len_difference is 16bits 

subnets = list(ipaddress.ip_network(ip_block).subnets(prefixlen_diff=prefix_len_difference))
for items in subnets: 
       print(str(items)) 