haproxy_cfg = """global
	log /dev/log	local0
	log /dev/log	local1 notice
	chroot /var/lib/haproxy
	user haproxy
	group haproxy
	daemon
	maxconn '{settings.HA_maxconn}'

defaults
	log	global
	mode	http
	option	httplog
	option	dontlognull
	option	forwardfor
	option	http-server-close
        contimeout 5000
        clitimeout 50000
        srvtimeout 50000
	retries 3
	option redispatch
	errorfile 400 /etc/haproxy/errors/400.http
	errorfile 403 /etc/haproxy/errors/403.http
	errorfile 408 /etc/haproxy/errors/408.http
	errorfile 500 /etc/haproxy/errors/500.http
	errorfile 502 /etc/haproxy/errors/502.http
	errorfile 503 /etc/haproxy/errors/503.http
	errorfile 504 /etc/haproxy/errors/504.http
frontend http-in
	bind '{settings.HA_domain_name}'
	mode http
      # default_backend host_httpd-in
        acl host_http-in hdr(host) -i '{settings.HA_cvip}'
        use_backend host_httpd-in if host_http-in
backend host_httpd-in
	mode http
	balance '{settings.HA_balance_type}'
	#balance leastconn
        option httpclose
	option forwardfor
        #option forwardfor header X-Forwarded-For
	#reqidel ^X-Real-IP
	cookie JSESSIONID prefix
	cookie SERVERID insert indirect
      # option httpchk HEAD /index.html HTTP/1.0
	server '{settings.HA_servers['node1'][0]}'	'{settings.HA_servers['node1'][1]}'	cookie	A	check
	server '{settings.HA_servers['node2'][0]}'      '{settings.HA_servers['node2'][1]}'	cookie	B	check
        server '{settings.HA_servers['node3'][0]}'      '{settings.HA_servers['node3'][1]}'	cookie	C	check

listen stats 0.0.0.0:9000
	stats '{settings.HA_stats_status}'
	stats uri /stats
	stats realm Strictly\ Private
        stats auth '{HA_stats_auth}'
"""
