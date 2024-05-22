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
from time import sleep
from modules.logo import *
from modules.system import *

yellow="\033[1;33m"
blue="\033[1;34m"
nc="\033[00m"

class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input(f"{yellow}Do you want to install Tool-X [Y/n]> {nc}")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if os.path.exists(system.conf_dir+"/Tool-X"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/Tool-X")
          os.system(system.sudo+" cp -r modules core Tool-X.py "+system.conf_dir+"/Tool-X")
          os.system(system.sudo+" cp -r core/Tool-X "+system.bin)
          os.system(system.sudo+" cp -r core/toolx "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/Tool-X")
          os.system(system.sudo+" chmod +x "+system.bin+"/toolx")
          os.system("cd .. && "+system.sudo+" rm -rf Tool-X")
          if os.path.exists(system.bin+"/Tool-X") and os.path.exists(system.conf_dir+"/Tool-X"):
            os.system("clear")
            logo.ins_sc()
            tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
            break
        else:
          if os.path.exists(system.conf_dir+"/Tool-X"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/Tool-X")
          os.system("cp -r modules core Tool-X.py "+system.conf_dir+"/Tool-X")
          os.system("cp -r core/Tool-X "+system.bin)
          os.system("cp -r core/toolx "+system.bin)
          os.system("chmod +x "+system.bin+"/Tool-X")
          os.system("chmod +x "+system.bin+"/toolx")
          os.system("cd .. && rm -rf Tool-X")
          if os.path.exists(system.bin+"/Tool-X") and os.path.exists(system.conf_dir+"/Tool-X"):
            os.system("clear")
            logo.ins_sc()
            tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
