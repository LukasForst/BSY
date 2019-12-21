input_pcap = bonus_assignment_stage1.pcap

unique_ips:
	tshark -r $(input_pcap) -T fields -e ip.dst ip.src | sort | uniq

label_ips:
	make -s unique_ips | ./list_public.py
