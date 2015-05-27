#Fabfile created By Arash Shams (ara4sh@hotmail.com)
#HAProxy and keepalive Installation , Configuration and control.
#to add or change hosts and nodes use setting.py

from fabric.utils import puts, warn
from fabric.api import run, quiet, env
from fabric.decorators import hosts, parallel

import setting
import haproxycfg
import keepalivedcfg

@parallel
@hosts(setting.LB_hosts)
def install_full():
	install_haproxy()
	install_keepalived()
	configure_haproxy()
		


@parallel
@hosts(setting.LB_hosts)
def ubuntu_update():
	"""Update Ubuntu
	"""
	with quiet():
		run('aptitude update')
		upgrade = run('apt-get -y upgrade')
	if upgrade.failed is False:
		puts('Distribution up to date')

@parallel
@hosts(setting.LB_hosts)
def install_haproxy():
	with quiet():
		result = run('apt-get install haproxy')
	if result.failed is False:
		puts('HAproxy installed successfully')
@parallel
@hosts(setting.LB_hosts)
def install_keepalived():
	with quiet():
                result = run('apt-get install keepalived')
        if result.failed is False:
                puts('Keepalived installed successfully')
@parallel
@hosts(setting.LB_hosts)
def configure_haproxy():
	""" Configuring HAProxy: change parameters in setting.py
	"""
	result = run('echo "{haproxycfg}" > /etc/haproxy/haproxy.cfg'.format(
	haproxycfg=haproxycfg.haproxy_cfg.format(
		setting=setting)
		)
	)

# @parallel
@hosts(setting.LB_hosts)
def haproxy(command=None):
	"""Control the HAProxy : start|stop|reload|restart|status
	"""
	if command not in ('start','stop','reload','restart','status'):
		warn('Unknown command: {}\n'
			'Available commands: start, stop, restart , reload , status'.format(command))
	else:
		if command == 'start':
			result = run('service haproxy start')
		elif command == 'stop':
			result = run('service haproxy stop')
		elif command == 'reload':
			result = run('service haproxy reload')
		elif command == 'restart':
			result = run('service haproxy restart')
		elif command == 'status':
                        result = run('service haproxy status')
@parallel
@hosts(setting.LB_hosts)
def keepalived(command=None):
        """Control the keepalived : start|stop|restart|reload|force-reload 
        """
        if command not in ('start','stop','reload','restart','force-reload'):
                warn('Unknown command: {}\n'
                        'Available commands: start, stop, restart , reload , force-reload'.format(command))
        else:
                if command == 'start':
                        result = run('service keepalived start')
                elif command == 'stop':
                        result = run('service keepalived stop')
                elif command == 'reload':
                        result = run('service keepalived reload')
                elif command == 'restart':
                        result = run('service keepalived restart')
                elif command == 'status':
                        result = run('service keepalived force-reload')
                        



