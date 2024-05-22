"""
Tool-X

Tool-X is dual-licensed under the terms of the MIT License and the
GNU General Public License v3.0 (GPL-3.0). You may choose either
license to govern your use of this project.

MIT License:
Permission is hereby granted, free of charge, to any person obtaining a 
copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation the 
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

GPL-3.0 License:
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
 
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import os
import sys
import logging
from time import sleep
from modules.logo import Logo
from modules.system import System

# Configure logging
logging.basicConfig(level=logging.INFO)

YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
NC = "\033[00m"

class ToolXInstaller:

    def __init__(self):
        self.system = System()
        self.logo = Logo()

    def prompt_installation(self):
        os.system("clear")
        self.logo.ins_tnc()
        return input(f"{YELLOW}Do you want to install Tool-X [Y/n]> {NC}").strip().lower() == 'y'

    def create_directories(self):
        if not os.path.exists(self.system.conf_dir + "/Tool-X"):
            os.makedirs(self.system.conf_dir + "/Tool-X", exist_ok=True)

    def copy_files(self):
        files_to_copy = ["modules", "core", "Tool-X.py"]
        for item in files_to_copy:
            os.system(f"{self.system.sudo or ''} cp -r {item} {self.system.conf_dir}/Tool-X")

        binaries = ["core/Tool-X", "core/toolx"]
        for binary in binaries:
            os.system(f"{self.system.sudo or ''} cp -r {binary} {self.system.bin}")
            os.system(f"{self.system.sudo or ''} chmod +x {self.system.bin}/{os.path.basename(binary)}")

    def clean_up(self):
        os.system(f"cd .. && {self.system.sudo or ''} rm -rf Tool-X")

    def verify_installation(self):
        return all(os.path.exists(path) for path in [self.system.bin + "/Tool-X", self.system.conf_dir + "/Tool-X"])

    def install(self):
        if not self.prompt_installation():
            return

        try:
            os.system("clear")
            self.logo.installing()
            self.create_directories()
            self.copy_files()
            self.clean_up()

            if self.verify_installation():
                os.system("clear")
                self.logo.ins_sc()
                input(f"{BLUE}Tool-X{NC}@{BLUE}space {YELLOW}$ {NC}")
            else:
                os.system("clear")
                self.logo.not_ins()
                input(f"{BLUE}Tool-X{NC}@{BLUE}space {YELLOW}$ {NC}")

        except Exception as e:
            logging.error(f"Installation failed: {e}")
            os.system("clear")
            self.logo.not_ins()
            input(f"{BLUE}Tool-X{NC}@{BLUE}space {YELLOW}$ {NC}")

    def uninstall(self):
        try:
            os.system(f"{self.system.sudo or ''} rm -rf {self.system.conf_dir}/Tool-X")
            os.system(f"{self.system.sudo or ''} rm -f {self.system.bin}/Tool-X")
            os.system(f"{self.system.sudo or ''} rm -f {self.system.bin}/toolx")
            logging.info("Tool-X has been uninstalled successfully.")
        except Exception as e:
            logging.error(f"Uninstallation failed: {e}")

if __name__ == "__main__":
    installer = ToolXInstaller()
    try:
        installer.install()
    except KeyboardInterrupt:
        os.system("clear")
        installer.logo.exit()
