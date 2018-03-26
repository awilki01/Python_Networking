from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

crypto_map = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for i in crypto_map:
    print i.text

crypto_map5 = crypto_map[4]
print crypto_map5
print crypto_map5.children

for child in crypto_map5.children:
    print child.text

print "-------------------------------------------------------"
print "Crypto Map Entries....."

for entry in crypto_map:
    print entry.text
    for child in entry.children:
        print child.text

print "-------------------------------------------------------"
print "Crypto Map Entries with PFS Group 2....."

crypto_map_w_pfs2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"pfs group2")

for entry in crypto_map_w_pfs2:
    print entry.text

print "-------------------------------------------------------"
print "Crypto Map Entries without AES....."

crypto_map_w_pfs2 = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES")

for entry in crypto_map_w_pfs2:
    print entry.text

















