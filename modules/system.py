import os
import sys
import requests

class SystemInfo:
    """
    Provides information about the system environment, including package manager, sudo access, and internet connectivity.
    """

    def __init__(self):
        self.home = os.getenv("HOME")
        self.bin = None
        self.sudo = None
        self.connection = self.check_internet_connection()
        self.conf_dir = self.find_config_dir()
        self.pac, self.sys = self.detect_package_manager()

    def check_internet_connection(self):
        """
        Checks if the system has an active internet connection.
        """
        try:
            requests.get("https://www.google.com").ok
            return True
        except:
            return False

    def find_config_dir(self):
        """
        Determines the configuration directory based on the system.
        """
        for dir in ["/usr/etc", "/data/data/com.termux/files/usr/etc", "/etc"]:
            if os.path.exists(dir):
                return dir
        return None

    def detect_package_manager(self):
        """
        Detects the package manager and system type.
        """
        for pac, sys in [
            ("yum", "linux"),
            ("apt-get", "linux"),
            ("pkg", "linux"),
            ("brew", "linux"),
            ("apk", "linux"),
        ]:
            for bin_dir in ["/usr/bin", "/bin", "/usr/sbin", "/sbin"]:
                if os.path.exists(os.path.join(bin_dir, pac)):
                    self.bin = bin_dir
                    return pac, sys
        return None, None

    def check_sudo_access(self):
        """
        Checks if the system has sudo access.
        """
        for sudo_path in [
            "/usr/lib/sudo",
            "/lib/sudo",
            "/usr/bin/sudo",
            "/bin/sudo",
            "/usr/sbin/sudo",
            "/sbin/sudo",
        ]:
            if os.path.exists(sudo_path):
                self.sudo = "sudo"
                return True
        return False

    def get_sudo_command(self):
        """
        Returns the sudo command if available, otherwise None.
        """
        return self.sudo

if __name__ == "__main__":
    system = SystemInfo()
    print(f"System: {system.sys}")
    print(f"Package Manager: {system.pac}")
    print(f"Sudo Access: {system.sudo}")
    print(f"Internet Connection: {system.connection}")
    print(f"Configuration Directory: {system.conf_dir}")
