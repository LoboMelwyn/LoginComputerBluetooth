# PAM interface in python

# sudo apt-get install libpam-python bluetooth libbluetooth-dev gobject
# sudo pip install pybluez

# Import required modules
import subprocess
import sys
import os
import bluetooth, time

def doAuth(pamh):
	"""Do Authentication here"""
	search_time = 10
	# Hardcoded the data for now
	addr = "18:F0:E4:CB:64:8E"
	state = bluetooth.lookup_name(addr, timeout=20)
	services = bluetooth.find_service(address=addr)
	if state == None and services == []:
	        return pamh.PAM_SYSTEM_ERR
	else:
		return pamh.PAM_SUCCESS
	return pamh.PAM_SYSTEM_ERR

def pam_sm_authenticate(pamh, flags, args):
	"""Called by PAM when the user wants to authenticate, in sudo for example"""
	return doAuth(pamh)

def pam_sm_open_session(pamh, flags, args):
	"""Called when starting a session, such as su"""
	return doAuth(pamh)

def pam_sm_close_session(pamh, flags, argv):
	"""We don't need to clean anyting up at the end of a session, so return true"""
	return pamh.PAM_SUCCESS

def pam_sm_setcred(pamh, flags, argv):
	"""We don't need set any credentials, so return true"""
	return pamh.PAM_SUCCESS
