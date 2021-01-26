#!python39
from lib.adb import Adb
from lib import last_bullet

from time import sleep

def scenario(adb):
	while True:
		last_bullet.replay(adb)
		sleep(3)

if __name__ == '__main__':
	with Adb('5b09ee92') as adb:
		scenario(adb)
