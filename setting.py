#Created by Arash Shams (Ara4Sh@hotmail.com)
#Change the parameters here.
LB_name = 'HA_Servers'
LB_user = 'root'
LB_hosts = ['node1','node2']
LB_mapping = {
	'node1': ('172.20.4.53'),
	'node2': ('172.20.4.54')
}

HA_maxconn = '20000'
HA_bind_ip = '172.20.4.50:80'
HA_balance_type = 'roundrobin' #leastconn
HA_cvip = '172.20.4.50'
HA_domain_name = 'www1.arash.com'
HA_servers = {
	'www1': ('www1','172.20.4.46:80'),
	'www2': ('www2','172.20.4.47:80'),
	'www3': ('www3','172.20.4.48:80')
}
HA_stats_status = 'enable'
HA_stats_auth = 'arash:arashshams'
#KA_notif_email = 'ara4sh@hotmail.com'
#KA_notif_email_from = 'araxshams@gmail.com'
#KA_router_id = 'haproxy'
#KA_interfaces = 'eth0'
#KA_priority = {
#	'node1': ('101'),
#	'node2': ('102')
#}
#KA_auth_pass = 'arashshams'

