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
@hosts(settings.cluster_hosts)
def configure_haproxy():
	""" Configuring HAProxy: change parameters in setting.py
	"""
	result = run('echo "{haproxycfg}" > /etc/haproxy/haproxy.cfg'.format(
	haproxycfg=haproxycfg.haproxy_cfg.format(
		settings=settings)
		)
	)

