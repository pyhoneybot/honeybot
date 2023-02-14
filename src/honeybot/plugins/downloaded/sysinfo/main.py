"""
[sysinfo.py]
System Information Plugin.

[Author]
Girish Mahabir

[About]
Responds to .sysinfo, gets System Information of the host.

[Commands]
>>> .sysinfo
returns General System Information, Boot Date and time, CPU information,
Memory information, Disk Information and Network Information.
"""
import platform
from datetime import datetime

import psutil


class Plugin:
    def __init__(self):
        pass

    def get_size(self, bytes):
        suffix = "B"
        self.bytes = bytes
        """
        Scale bytes to its proper format.
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if self.bytes < factor:
                return f"{self.bytes:.2f}{unit}{suffix}"
            self.bytes /= factor

    def run(self, incoming, methods, info, bot_info):
        try:
            if info["command"] == "PRIVMSG" and info["args"][1] == ".botinfo":
                methods["send"](info["address"], "Info Available:")
                methods["send"](info["address"], "System Information: sysinfo")
                methods["send"](info["address"], "Boot Information: bootinfo")
                methods["send"](info["address"], "CPU Information: cpuinfo")
                methods["send"](info["address"], "Memory Information: memoryinfo")
                methods["send"](info["address"], "Disk Information: diskinfo")
                methods["send"](info["address"], "Network Information: networkinfo")

            if info["command"] == "PRIVMSG" and info["args"][1] == ".sysinfo":
                # System Information.
                methods["send"](info["address"], "=" * 40 + "System Information" + "=" * 40)
                uname = platform.uname()
                methods["send"](info["address"], f"System: {uname.system}")
                methods["send"](info["address"], f"Node Name: {uname.node}")
                methods["send"](info["address"], f"Release: {uname.release}")
                methods["send"](info["address"], f"Version: {uname.version}")
                methods["send"](info["address"], f"Machine: {uname.machine}")
                methods["send"](info["address"], f"Processor: {uname.processor}")

            if info["command"] == "PRIVMSG" and info["args"][1] == ".bootinfo":
                # Data and Time computer was booted.
                # Boot Time.
                methods["send"](info["address"], "=" * 40 + "Boot Time" + "=" * 40)
                boot_time_timestamp = psutil.boot_time()
                bt = datetime.fromtimestamp(boot_time_timestamp)
                methods["send"](
                    info["address"],
                    f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}",
                )

            if info["command"] == "PRIVMSG" and info["args"][1] == ".cpuinfo":
                # CPU Information.
                # Let's Print, CPU information.
                methods["send"](info["address"], "=" * 40 + "CPU Info" + "=" * 40)
                # Number of cores.
                methods["send"](
                    info["address"],
                    f"Physical cores: {psutil.cpu_count(logical=False)}",
                )
                methods["send"](
                    info["address"],
                    f"Total cores: {psutil.cpu_count(logical=True)}",
                )
                # CPU frequencies.
                cpufreq = psutil.cpu_freq()
                methods["send"](info["address"], f"Max Frequency: {cpufreq.max:.2f}Mhz")
                methods["send"](info["address"], f"Min Frequency: {cpufreq.min:.2f}Mhz")
                methods["send"](info["address"], f"Current Frequency: {cpufreq.current:.2f}Mhz")
                # CPU usage.
                methods["send"](info["address"], "CPU Usage Per Core:")
                for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
                    methods["send"](info["address"], f"Core {i}: {percentage}%")
                methods["send"](info["address"], f"Total CPU Usage: {psutil.cpu_percent()}%")

            if info["command"] == "PRIVMSG" and info["args"][1] == ".memoryinfo":
                # Memory Information.
                methods["send"](info["address"], "=" * 40 + "Memory Information" + "=" * 40)
                # Get the memory details.
                svmem = psutil.virtual_memory()
                methods["send"](info["address"], f"Total: {self.get_size(svmem.total)}")
                methods["send"](info["address"], f"Available: {self.get_size(svmem.available)}")
                methods["send"](info["address"], f"Used: {self.get_size(svmem.used)}")
                methods["send"](info["address"], f"Percentage: {svmem.percent}%")
                methods["send"](info["address"], "=" * 20 + "SWAP" + "=" * 20)
                # Get the swap memory details (if exists).
                swap = psutil.swap_memory()
                methods["send"](info["address"], f"Total: {self.get_size(swap.total)}")
                methods["send"](info["address"], f"Free: {self.get_size(swap.free)}")
                methods["send"](info["address"], f"Used: {self.get_size(swap.used)}")
                methods["send"](info["address"], f"Percentage: {swap.percent}%")

            if info["command"] == "PRIVMSG" and info["args"][1] == ".networkinfo":
                # Network information
                methods["send"](info["address"], "=" * 40 + "Network Information" + "=" * 40)
                # Get all network interfaces (virtual and physical).
                if_addrs = psutil.net_if_addrs()
                for interface_name, interface_addresses in if_addrs.items():
                    for address in interface_addresses:
                        # methods["send"](info["address"],
                        # f"=== Interface: {interface_name} ===")
                        if str(address.family) == "AddressFamily.AF_INET":
                            methods["send"](
                                info["address"],
                                f"IP Address: {address.address}  ||  "
                                f"Netmask: {address.netmask}".format(),
                            )
                        elif str(address.family) == "AddressFamily.AF_PACKET":
                            methods["send"](
                                info["address"],
                                f"MAC Address: {address.address} ||  Netmask: {address.netmask}",
                            )
                # Get IO statistics since boot.
                net_io = psutil.net_io_counters()
                methods["send"](
                    info["address"],
                    f"Total Bytes Sent: {self.get_size(net_io.bytes_sent)}"
                    " ||  Total Bytes Received: "
                    f"{self.get_size(net_io.bytes_recv)}",
                )

            if info["command"] == "PRIVMSG" and info["args"][1] == ".diskinfo":
                # Disk Information
                methods["send"](
                    info["address"],
                    "=" * 40 + "Disk Information" + "=" * 40 + "\nPartitions and Usage:",
                )
                # Get all disk partitions.
                partitions = psutil.disk_partitions()
                for partition in partitions:
                    methods["send"](
                        info["address"],
                        f"=== Device: {partition.device} ===\n"
                        f"  Mountpoint: {partition.mountpoint}\n"
                        f"  File system type: {partition.fstype}",
                    )
                    try:
                        partition_usage = psutil.disk_usage(partition.mountpoint)
                    except PermissionError:
                        # This can be catch due to disks that
                        # isn't ready.
                        continue
                    methods["send"](
                        info["address"],
                        "  Total Size: "
                        f"{self.get_size(partition_usage.total)}\n  "
                        f"Used: {self.get_size(partition_usage.used)}\n  "
                        f"Free: {self.get_size(partition_usage.free)}\n  "
                        f"Percentage: {partition_usage.percent}%",
                    )
                # Get IO statistics since boot.
                disk_io = psutil.disk_io_counters()
                methods["send"](
                    info["address"],
                    f"Total read: {self.get_size(disk_io.read_bytes)}\n"
                    f"Total write: {self.get_size(disk_io.write_bytes)}",
                )
        except Exception as e:
            print("woops plug", e)
