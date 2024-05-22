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
import json
from time import sleep
from .logo import *
from .system import *

class main:
  def install_tools(self):
    while True:
      tool=tools()
      num=1
      total=len(tool.names)
      os.system("clear")
      logo.install_tools()
      print("\007")
      for tool_name in tool.names:
        print (f" \033[01;32m[ \033[01;37m{num} \033[01;32m] \033[01;33minstall \033[01;32m{tool_name}\033[00m")
        num+=1
      print("")
      logo.back()
      cmd=input("\033[1;36m ##> \033[00m")
      if cmd=="00" or cmd=="back":
        self.menu()
        break
      else:
        try:
          if int(cmd)>=1 and int(cmd)<=int(total):
            os.system("clear")
            logo.installing()
            print("\033[01;32minstalling ....\033[00m")
            tool.install(tool.names[int(cmd)-1])
          else:
            print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input !!\033[00m")
            sleep(1)
        except ValueError:
          print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input !!\033[00m")
          sleep(1)

  def category(self):
    while True:
      tool=tools()
      total=len(tool.category)
      num=1
      os.system("clear")
      logo.tool_header()
      print("")
      for cat in tool.category:
        print (f"  \033[01;32m[ \033[01;37m{num} \033[01;32m] \033[01;33m{tool.category_data[cat]}\033[00m")
        num+=1
      print("")
      logo.back()
      cmd=input("\033[1;36m ##> \033[00m")
      if cmd=="00" or cmd=="back":
        self.menu()
        break
      else:
        try:
          if int(cmd) in range(1,int(total)+1):
            while True:
              print(int(cmd)-1)
              print(tool.category[int(cmd)-1])
              cnt=1
              os.system("clear")
              logo.tool_header()
              print("")
              tmp_cat_tool=[]
              for i in tool.names:
                if tool.category[int(cmd)-1] in tool.data[i]["category"]:
                  tmp_cat_tool.append(tool.data[i]['name'])
                  print(f" \033[01;32m[ \033[00m{cnt} \033[01;32m] \033[01;33minstall \033[01;32m{tool.data[i]['name']}\033[00m")
                  cnt+=1
              print("")
              logo.back()
              tcmd=input("\033[1;36m ##> \033[00m")
              if tcmd=="00" or tcmd=="back":
                break
              else:
                try:
                  cat_total=len(tmp_cat_tool)
                  if int(tcmd) in range(1,int(cat_total)+1):
                    os.system("clear")
                    logo.installing()
                    print("\033[01;32minstalling ....\033[00m")
                    tool.install(tmp_cat_tool[int(tcmd)-1])
                  else:
                    print(f"\007\033[01;31mSorry \033[01;37m: '{tcmd}' \033[01;31minvalid input !!\033[00m")
                    sleep(1)
                except ValueError:
                  print(f"\007\033[01;31mSorry \033[01;37m: '{tcmd}' \033[01;31minvalid input !!\033[00m")
                  sleep(1)
          else:
            print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input !!\033[00m")
            sleep(1)
        except ValueError:
          print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input !!\033[00m")
          sleep(1)

  def update(self):
    while True:
      os.system("clear")
      logo.update()
      cmd=input("\033[1;36m ##> \033[00m")
      if cmd=="1":
        system=sys()
        if system.connection:
          os.system("clear")
          logo.updating()
          if system.sudo != None:
            if os.path.exists(system.home+"/Tool-X"):
              pass
            else:
              os.system(system.sudo+" git clone https://github.com/NxPKG/Tool-X.git "+system.home+"/Tool-X")
            if os.path.exists(system.home+"/Tool-X/install.aex"):
              os.system("cd "+system.home+"/Tool-X && "+system.sudo+" sh install.aex")
              if os.path.exists(system.bin+"/Tool-X") and os.path.exists(system.conf_dir+"/Tool-X"):
                os.system("clear")
                logo.updated()
                cmd=input("\033[1;36m ##> \033[00m")
              else:
                os.system("clear")
                logo.update_error()
                cmd=input("\033[1;36m ##> \033[00m")
            else:
              os.system("clear")
              logo.update_error()
              cmd=input("\033[1;36m ##> \033[00m")
          else:
            if os.path.exists(system.home+"/Tool-X"):
              pass
            else:
              os.system("git clone https://github.com/NxPKG/Tool-X.git "+system.home+"/Tool-X")
            if os.path.exists(system.home+"/Tool-X/install.aex"):
              os.system("cd "+system.home+"/Tool-X && sh install.aex")
              if os.path.exists(system.bin+"/Tool-X") and os.path.exists(system.conf_dir+"/Tool-X"):
                os.system("clear")
                logo.updated()
                cmd=input("\033[1;36m ##> \033[00m")
              else:
                os.system("clear")
                logo.update_error()
                cmd=input("\033[1;36m ##> \033[00m")
            else:
              os.system("clear")
              logo.update_error()
              cmd=input("\033[1;36m ##> \033[00m")
        else:
          os.system("clear")
          logo.nonet()
          tmp=input("\033[1;36m ##> \033[00m")
      elif cmd=="0" or cmd=="back":
        self.menu()
        break
      else:
        print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input !!\033[00m")
        sleep(1)

  def about(self):
    while True:
      tool=tools()
      total=len(tool.names)
      os.system("clear")
      logo.about(total)
      cmd=input("\033[1;36m ##> \033[00m")
      self.menu()
      break

  @classmethod
  def menu(self):
    while True:
      tool=tools()
      system=sys()
      total=len(tool.names)
      os.system("clear")
      logo.menu(total)
      cmd=input("\033[1;36m ##> \033[00m")
      if cmd == "1":
        self.install_tools(self)
        break
      elif cmd == "2":
        self.category(self)
        break
      elif cmd == "3":
        self.update(self)
        break
      elif cmd == "4":
        self.about(self)
        break
      elif cmd=="x" or cmd=="X" or cmd=="exit":
        os.system("clear")
        logo.exit()
        break
      elif cmd=="rm -t" or cmd=="rm -T" or cmd=="uninstall tool-x" or cmd=="unistall Tool-X":
        if system.sudo:
          os.system(system.sudo+" rm -rf "+system.bin+"/Tool-X")
          os.system(system.sudo+" rm -rf "+system.bin+"/toolx")
          os.system(system.sudo+" rm -rf "+system.conf_dir+"/Tool-X")
        else:
          os.system("rm -rf "+system.bin+"/Tool-X")
          os.system("rm -rf "+system.bin+"/toolx")
          os.system("rm -rf "+system.conf_dir+"/Tool-X")
        os.system("clear")
        logo.exit()
        break
      else:
        print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input !!\033[00m")
        sleep(1)

class tools:
  data=None
  names=None
  category=None
  category_data=None
  def __init__(self):
    system=sys()
    with open(system.conf_dir+"/Tool-X/core/data.json") as data_file:
      self.data=json.load(data_file)
    with open(system.conf_dir+"/Tool-X/core/cat.json") as cat_file:
      self.category_data=json.load(cat_file)
    self.names=list(self.data.keys())
    self.category=list(self.category_data.keys())

  def install(self,name):
    package_name=self.data[name]["package_name"]
    package_manager=self.data[name]["package_manager"]
    url=self.data[name]["url"]
    req=list(self.data[name]["dependency"])
    system=sys()

    if system.connection:
      if len(req)!=0 and req[0]!=None:
        for dep in req:
          if os.path.exists(system.bin+"/"+dep):
            pass
          else:
            if system.sudo != None:
              os.system(system.sudo+" "+system.pac+" install "+dep+" -y")
            else:
              os.system(system.pac+" install "+dep+" -y")

      if package_manager=="package_manager":
        if os.path.exists(system.bin+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input("\033[1;36m ##> \033[00m")
        else:
          if system.sudo != None:
            os.system(system.sudo+" "+system.pac+" install "+package_name+" -y")
          else:
            os.system(system.pac+" install "+package_name+" -y")
          # check tool is installed or not
          if os.path.exists(system.bin+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input("\033[1;36m ##> \033[00m")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=input("\033[1;36m ##> \033[00m")

      elif package_manager=="git":
        if os.path.exists(system.home+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input("\033[1;36m ##> \033[00m")
        else:
          if system.sudo != None:
            os.system(system.sudo+" git clone "+url+" "+system.home+"/"+package_name)
          else:
            os.system("git clone "+url+" "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input("\033[1;36m ##> \033[00m")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=input("\033[1;36m ##> \033[00m")

      elif package_manager=="wget":
        if os.path.exists(system.home+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input("\033[1;36m ##> \033[00m")
        else:
          if system.sudo != None:
            os.system(system.sudo+" wget "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("wget "+url+" -o "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input("\033[1;36m ##> \033[00m")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=input("\033[1;36m ##> \033[00m")

      elif package_manager=="curl":
        if os.path.exists(system.home+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input("\033[1;36m ##> \033[00m")
        else:
          if system.sudo != None:
            os.system(system.sudo+" curl "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("curl "+url+" -o "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input("\033[1;36m ##> \033[00m")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=input("\033[1;36m ##> \033[00m")
    else:
      os.system("clear")
      logo.nonet()
      tmp=input("\033[1;36m ##> \033[00m")
