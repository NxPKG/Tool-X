import os
import json
from time import sleep

from .logo import logo
from .system import sys

class ToolX:
    """
    Main class for Tool-X, handling installation, category browsing, updates, and about information.
    """

    def __init__(self):
        self.tools = Tools()
        self.system = sys()

    def install_tools(self):
        """
        Displays a list of tools and allows the user to install them.
        """
        while True:
            os.system("clear")
            logo.install_tools()
            print("\007")

            # Display list of available tools
            for num, tool_name in enumerate(self.tools.names, start=1):
                print(f"  \033[01;32m[ \033[01;37m{num} \033[01;32m] \033[01;33minstall \033[01;32m{tool_name}\033[00m")

            print("")
            logo.back()
            cmd = input("\033[1;36m ##> \033[00m")

            if cmd.lower() == "00" or cmd.lower() == "back":
                self.menu()
                break
            else:
                try:
                    cmd_int = int(cmd)
                    if 1 <= cmd_int <= len(self.tools.names):
                        self.install_tool(self.tools.names[cmd_int - 1])
                    else:
                        self.invalid_input()
                except ValueError:
                    self.invalid_input()

    def install_tool(self, tool_name):
        """
        Installs a specific tool based on its name.
        """
        os.system("clear")
        logo.installing()
        print("\033[01;32minstalling ....\033[00m")
        self.tools.install(tool_name)

    def category(self):
        """
        Displays a list of categories and allows the user to browse tools within each category.
        """
        while True:
            os.system("clear")
            logo.tool_header()
            print("")

            # Display list of categories
            for num, cat in enumerate(self.tools.category, start=1):
                print(f"  \033[01;32m[ \033[01;37m{num} \033[01;32m] \033[01;33m{self.tools.category_data[cat]}\033[00m")

            print("")
            logo.back()
            cmd = input("\033[1;36m ##> \033[00m")

            if cmd.lower() == "00" or cmd.lower() == "back":
                self.menu()
                break
            else:
                try:
                    cmd_int = int(cmd)
                    if 1 <= cmd_int <= len(self.tools.category):
                        self.browse_category(self.tools.category[cmd_int - 1])
                    else:
                        self.invalid_input()
                except ValueError:
                    self.invalid_input()

    def browse_category(self, category):
        """
        Displays tools within a selected category and allows the user to install them.
        """
        while True:
            os.system("clear")
            logo.tool_header()
            print("")

            tmp_cat_tool = []
            for i, tool_name in enumerate(self.tools.names, start=1):
                if category in self.tools.data[tool_name]["category"]:
                    tmp_cat_tool.append(self.tools.data[tool_name]['name'])
                    print(f"  \033[01;32m[ \033[00m{i} \033[01;32m] \033[01;33minstall \033[01;32m{self.tools.data[tool_name]['name']}\033[00m")

            print("")
            logo.back()
            tcmd = input("\033[1;36m ##> \033[00m")

            if tcmd.lower() == "00" or tcmd.lower() == "back":
                break
            else:
                try:
                    tcmd_int = int(tcmd)
                    if 1 <= tcmd_int <= len(tmp_cat_tool):
                        self.install_tool(tmp_cat_tool[tcmd_int - 1])
                    else:
                        self.invalid_input()
                except ValueError:
                    self.invalid_input()

    def update(self):
        """
        Handles updating Tool-X.
        """
        while True:
            os.system("clear")
            logo.update()
            cmd = input("\033[1;36m ##> \033[00m")

            if cmd == "1":
                if self.system.connection:
                    self.update_tool_x()
                else:
                    self.no_internet()
            elif cmd.lower() == "0" or cmd.lower() == "back":
                self.menu()
                break
            else:
                self.invalid_input()

    def update_tool_x(self):
        """
        Performs the actual update process for Tool-X.
        """
        os.system("clear")
        logo.updating()

        if self.system.sudo is not None:
            if not os.path.exists(self.system.home + "/Tool-X"):
                os.system(self.system.sudo + " git clone https://github.com/NxPKG/Tool-X.git " + self.system.home + "/Tool-X")

            if os.path.exists(self.system.home + "/Tool-X/install.aex"):
                os.system("cd " + self.system.home + "/Tool-X && " + self.system.sudo + " sh install.aex")

                if os.path.exists(self.system.bin + "/Tool-X") and os.path.exists(self.system.conf_dir + "/Tool-X"):
                    os.system("clear")
                    logo.updated()
                    input("\033[1;36m ##> \033[00m")
                else:
                    self.update_error()
            else:
                self.update_error()
        else:
            if not os.path.exists(self.system.home + "/Tool-X"):
                os.system("git clone https://github.com/NxPKG/Tool-X.git " + self.system.home + "/Tool-X")

            if os.path.exists(self.system.home + "/Tool-X/install.aex"):
                os.system("cd " + self.system.home + "/Tool-X && sh install.aex")

                if os.path.exists(self.system.bin + "/Tool-X") and os.path.exists(self.system.conf_dir + "/Tool-X"):
                    os.system("clear")
                    logo.updated()
                    input("\033[1;36m ##> \033[00m")
                else:
                    self.update_error()
            else:
                self.update_error()

    def add_tools(self):
        """
        Allows users to add new tools.
        """
        os.system("clear")
        logo.add_tools()
        
        # Prompt user for tool information
        category = input("Enter category for the new tool: ")
        repo_url = input("Enter repository URL for the new tool: ")
        title = input("Enter title for the new tool: ")
        description = input("Enter description for the new tool: ")
        
        # Update tool data JSON files
        new_tool_data = {
            "title": title,
            "description": description,
            "url": repo_url,
            "category": category  # Assuming category is a list
        }
        self.tools.add_tool(new_tool_data)
        
        input("\nNew tool added successfully! Press Enter to continue...")
        self.menu()
        
    def about(self):
        """
        Displays information about Tool-X.
        """
        while True:
            os.system("clear")
            logo.about(len(self.tools.names))
            input("\033[1;36m ##> \033[00m")
            self.menu()
            break

    def menu(self):
        """
        Main menu of Tool-X.
        """
        while True:
            os.system("clear")
            logo.menu(len(self.tools.names))
            cmd = input("\033[1;36m ##> \033[00m")

            if cmd == "1":
                self.install_tools()
                break
            elif cmd == "2":
                self.category()
                break
            elif cmd == "3":
                self.update()
                break
            elif cmd == "4":
                self.about()
                break
            elif cmd == "5":
                self.add_tools()  # Option for adding new tools
                break
            elif cmd.lower() in ("x", "exit"):
                os.system("clear")
                logo.exit()
                break
            elif cmd.lower() in ("rm -t", "rm -T", "uninstall tool-x", "unistall Tool-X"):
                self.uninstall_tool_x()
                break
            else:
                self.invalid_input()

    def uninstall_tool_x(self):
        """
        Uninstalls Tool-X.
        """
        if self.system.sudo:
            os.system(self.system.sudo + " rm -rf " + self.system.bin + "/Tool-X")
            os.system(self.system.sudo + " rm -rf " + self.system.bin + "/toolx")
            os.system(self.system.sudo + " rm -rf " + self.system.conf_dir + "/Tool-X")
        else:
            os.system("rm -rf " + self.system.bin + "/Tool-X")
            os.system("rm -rf " + self.system.bin + "/toolx")
            os.system("rm -rf " + self.system.conf_dir + "/Tool-X")
        os.system("clear")
        logo.exit()

    def invalid_input(self):
        """
        Handles invalid user input.
        """
        print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input !!\033[00m")
        sleep(1)

    def no_internet(self):
        """
        Displays a message when there is no internet connection.
        """
        os.system("clear")
        logo.nonet()
        input("\033[1;36m ##> \033[00m")

    def update_error(self):
        """
        Displays an error message if the update process fails.
        """
        os.system("clear")
        logo.update_error()
        input("\033[1;36m ##> \033[00m")

class Tools:
    """
    Class to manage tool data and installation logic.
    """

    def __init__(self):
        self.system = sys()
        self.load_data()

    def load_data(self):
        """
        Loads tool data from JSON files.
        """
        with open(self.system.conf_dir + "/Tool-X/core/data.json") as data_file:
            self.data = json.load(data_file)
        with open(self.system.conf_dir + "/Tool-X/core/cat.json") as cat_file:
            self.category_data = json.load(cat_file)
        self.names = list(self.data.keys())
        self.category = list(self.category_data.keys())

    def install(self, name):
        """
        Installs a tool based on its name.
        """
        package_name = self.data[name]["package_name"]
        package_manager = self.data[name]["package_manager"]
        url = self.data[name]["url"]
        req = list(self.data[name]["dependency"])

        if self.system.connection:
            self.install_dependencies(req)

            if package_manager == "package_manager":
                self.install_package_manager(package_name)
            elif package_manager == "git":
                self.install_git(package_name, url)
            elif package_manager == "wget":
                self.install_wget(package_name, url)
            elif package_manager == "curl":
                self.install_curl(package_name, url)
        else:
            os.system("clear")
            logo.nonet()
            input("\033[1;36m ##> \033[00m")

    def install_dependencies(self, req):
        """
        Installs dependencies for a tool.
        """
        if len(req) != 0 and req[0] is not None:
            for dep in req:
                if os.path.exists(self.system.bin + "/" + dep):
                    pass
                else:
                    if self.system.sudo is not None:
                        os.system(self.system.sudo + " " + self.system.pac + " install " + dep + " -y")
                    else:
                        os.system(self.system.pac + " install " + dep + " -y")

    def install_package_manager(self, package_name):
        """
        Installs a tool using the package manager.
        """
        if os.path.exists(self.system.bin + "/" + package_name):
            os.system("clear")
            logo.already_installed(package_name)
            input("\033[1;36m ##> \033[00m")
        else:
            if self.system.sudo is not None:
                os.system(self.system.sudo + " " + self.system.pac + " install " + package_name + " -y")
            else:
                os.system(self.system.pac + " install " + package_name + " -y")
            self.check_installation(package_name)

    def install_git(self, package_name, url):
        """
        Installs a tool using Git.
        """
        if os.path.exists(self.system.home + "/" + package_name):
            os.system("clear")
            logo.already_installed(package_name)
            input("\033[1;36m ##> \033[00m")
        else:
            if self.system.sudo is not None:
                os.system(self.system.sudo + " git clone " + url + " " + self.system.home + "/" + package_name)
            else:
                os.system("git clone " + url + " " + self.system.home + "/" + package_name)
            self.check_installation(package_name)

    def install_wget(self, package_name, url):
        """
        Installs a tool using wget.
        """
        if os.path.exists(self.system.home + "/" + package_name):
            os.system("clear")
            logo.already_installed(package_name)
            input("\033[1;36m ##> \033[00m")
        else:
            if self.system.sudo is not None:
                os.system(self.system.sudo + " wget " + url + " -o " + self.system.home + "/" + package_name)
            else:
                os.system("wget " + url + " -o " + self.system.home + "/" + package_name)
            self.check_installation(package_name)

    def install_curl(self, package_name, url):
        """
        Installs a tool using curl.
        """
        if os.path.exists(self.system.home + "/" + package_name):
            os.system("clear")
            logo.already_installed(package_name)
            input("\033[1;36m ##> \033[00m")
        else:
            if self.system.sudo is not None:
                os.system(self.system.sudo + " curl " + url + " -o " + self.system.home + "/" + package_name)
            else:
                os.system("curl " + url + " -o " + self.system.home + "/" + package_name)
            self.check_installation(package_name)

    def check_installation(self, package_name):
        """
        Checks if a tool was successfully installed.
        """
        if os.path.exists(self.system.bin + "/" + package_name):
            os.system("clear")
            logo.installed(package_name)
            input("\033[1;36m ##> \033[00m")
        else:
            os.system("clear")
            logo.not_installed(package_name)
            input("\033[1;36m ##> \033[00m")

    def add_tool(self, new_tool_data):
        """
        Adds a new tool to the tool data JSON files.
        """
        # Append new tool data to existing data
        self.data[new_tool_data["title"]] = {
            "package_name": "",  # Update with relevant information if applicable
            "package_manager": "",  # Update with relevant information if applicable
            "url": new_tool_data["url"],
            "dependency": [],  # Update with relevant information if applicable
            "category": new_tool_data["category"]
        }

        # Update categories JSON file if necessary
        if new_tool_data["category"] not in self.category_data:
            self.category_data[new_tool_data["category"]] = new_tool_data["category"]

        # Write updated data to JSON files
        with open(self.system.conf_dir + "/Tool-X/core/data.json", "w") as data_file:
            json.dump(self.data, data_file, indent=4)
        with open(self.system.conf_dir + "/Tool-X/core/cat.json", "w") as cat_file:
            json.dump(self.category_data, cat_file, indent=4)

if __name__ == "__main__":
    toolx = ToolX()
    toolx.menu()
