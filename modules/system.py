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
try:
  import requests
except:
  os.system("pip install requests")
  os.system("pip3 install requests")

class sys:
  pac=None
  sys=None
  home=os.getenv("HOME")
  bin=None
  sudo=None
  connection=False
  conf_dir=None
  def __init__(self):
    try:
      if requests.get("https://www.google.com").ok:
        self.connection=True
    except:
      self.connection=False

    # checking for system root access
    if os.path.exists("/usr/lib/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/lib/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/usr/bin/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/bin/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/usr/sbin/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/sbin/sudo"):
      self.sudo="sudo"

    # checking for configuration dir
    if os.path.exists("/usr/etc"):
      self.conf_dir="/usr/etc"
    elif os.path.exists("/data/data/com.termux/files/usr/etc"):
      self.conf_dir="/data/data/com.termux/files/usr/etc"
    elif os.path.exists("/etc"):
      self.conf_dir="/etc"

    # checking for system bin dir and system package manager
    if os.path.exists("/usr/bin/yum"):
      self.sys="linux"
      self.bin="/usr/bin"
      self.pac="yum"
    elif os.path.exists("/bin/yum"):
      self.sys="linux"
      self.bin="/bin"
      self.pac="yum"
    elif os.path.exists("/usr/sbin/yum"):
      self.sys="linux"
      self.bin="/usr/sbin"
      self.pac="yum"
    elif os.path.exists("/sbin/yum"):
      self.sys="linux"
      self.bin="/sbin"
      self.pac="yum"
    elif os.path.exists("/usr/bin/apt"):
      self.sys="linux"
      self.bin="/usr/bin"
      self.pac="apt-get"
    elif os.path.exists("/bin/apt"):
      self.sys="linux"
      self.bin="/bin"
      self.pac="apt-get"
    elif os.path.exists("/usr/sbin/apt"):
      self.sys="linux"
      self.bin="/usr/sbin"
      self.pac="apt-get"
    elif os.path.exists("/sbin/apt"):
      self.sys="linux"
      self.bin="/sbin"
      self.pac="apt-get"
    elif os.path.exists("/data/data/com.termux/files/usr/bin/pkg"):
      self.sys="linux"
      self.bin="/data/data/com.termux/files/usr/bin"
      self.pac="pkg"
    elif os.path.exists("/usr/bin/brew"):
      self.sys="linux"
      self.bin="/usr/bin"
      self.pac="brew"
    elif os.path.exists("/bin/brew"):
      self.sys="linux"
      self.bin="/bin"
      self.pac="brew"
    elif os.path.exists("/usr/sbin/brew"):
      self.sys="linux"
      self.bin="/usr/sbin"
      self.pac="brew"
    elif os.path.exists("/sbin/brew"):
      self.sys="linux"
      self.bin="/sbin"
      self.pac="brew"
    elif os.path.exists("/usr/bin/apk"):
      self.sys="linux"
      self.bin="/usr/bin"
      self.pac="apk"
    elif os.path.exists("/bin/apk"):
      self.sys="linux"
      self.bin="/bin"
      self.pac="apk"
    elif os.path.exists("/usr/sbin/apk"):
      self.sys="linux"
      self.bin="/usr/sbin"
      self.pac="apk"
    elif os.path.exists("/sbin/apk"):
      self.sys="linux"
      self.bin="/sbin"
      self.pac="apk"
