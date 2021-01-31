import subprocess

MAX_ERROR_COUNT = 3

class Adb():
	def __init__(self, device_id):
		self.device_id = device_id
		print(device_id)
	def __enter__(self):
		self.connect()
		return self
	def __exit__(self, exc_type, exc_value, traceback):
		self.disconnect()
	def __exec_cmd(self, cmd):
		error_count = 0
		result = subprocess.run(cmd)
		if result.returncode != 0:
			error_count += 1
			if error_count >= MAX_ERROR_COUNT:
				raise OSError()
			else:
				this.__exec_cmd()
	def connect(self):
		self.__exec_cmd("adb connect {0}".format(self.device_id))
	def disconnect(self):
		self.__exec_cmd("adb disconnect {0}".format(self.device_id))
	def tap(self, x, y):
		self.__exec_cmd("adb shell input touchscreen tap {x} {y}".format(x=x, y=y))
