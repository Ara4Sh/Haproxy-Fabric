keepalivedcfg = """global_defs {
        notification_email {
                a.shams@dabacenter.ir
        }
        notification_email_from haproxy2@dabacenter.ir
        router_id haproxy
}

vrrp_script haproxy {
        script "killall -0 haproxy"
        interval 2
        weight 2
}

vrrp_instance VI_1 {
        state MASTER
        interface eth0
        smtp_alert
        virtual_router_id 10
        priority 101
        advert_int 1
        authentication {
                auth_type PASS
                auth_pass arashshams123 # use 8 chars & something better
        }
        virtual_ipaddress {
                172.20.4.50
        }
        track_script {
                haproxy
        }
}
""" 
