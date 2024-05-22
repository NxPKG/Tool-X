/*
 * Tool-X
 *
 * Tool-X is dual-licensed under the terms of the MIT License and the
 * GNU General Public License v3.0 (GPL-3.0). You may choose either
 * license to govern your use of this project.
 *
 * MIT License:
 * Permission is hereby granted, free of charge, to any person obtaining a 
copy
 * of this software and associated documentation files (the "Software"), 
to deal
 * in the Software without restriction, including without limitation the 
rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or 
sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included 
in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
IN THE
 * SOFTWARE.
 *
 * GPL-3.0 License:
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <https://www.gnu.org/licenses/>.
 */

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
