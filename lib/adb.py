import subprocess

class Adb():
	def __init__(self, device_id):
		self.device_id = device_id
		print(device_id)
	def __enter__(self):
		self.connect()
		return self
	def __exit__(self, exc_type, exc_value, traceback):
		self.disconnect()
	def connect(self):
		result = subprocess.run("adb connect {0}".format(self.device_id))
		if result.returncode != 0:
			raise Error()
	def disconnect(self):
		result = subprocess.run("adb disconnect {0}".format(self.device_id))
		if result.returncode != 0:
			raise Error()
	def tap(self, x, y):
		result = subprocess.run("adb shell input touchscreen tap {x} {y}".format(x=x, y=y))
		if result.returncode != 0:
			raise Error()
