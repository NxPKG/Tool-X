class Logo:
    HEADER = '''
\007
\033[1;33m
         _____           _    __  __
        |_   _|__   ___ | |   \ \/ /
          | |/ _ \ / _ \| |____\  /
          | | (_) | (_) | |____/  \    
          |_|\___/ \___/|_|   /_/\_\ \033[1;91mv2.1
\033[1;36m =============================================\033[1;m
\033[1;33m|          Install Best Hacking Tool          |
\033[1;36m =============================================\033[00m
'''

    FOOTER = '''
\033[1;36m_______________________________________________
===============================================\033[00m
'''

    @classmethod
    def display(cls, message: str):
        print(cls.HEADER + message + cls.FOOTER)

    @classmethod
    def tool_header(cls):
        print(cls.HEADER)

    @classmethod
    def tool_footer(cls):
        print(cls.FOOTER)

    @classmethod
    def not_installed(cls):
        cls.display('''
\033[1;31m  [ + ]  \033[1;31mWe can't install Tool-X.\033[1;m
\033[1;31m  [ + ]  \033[1;31mThere are some errors.\033[1;m
\033[1;31m  [ + ]  \033[1;31mPlease try again after some time.\033[1;m
''')

    @classmethod
    def install_terms_and_conditions(cls):
        cls.display('''
\033[1;33m  [ + ] \033[1;32mUse It At Your Own Risk.
\033[1;33m  [ + ] \033[1;32mNo Warranty.
\033[1;33m  [ + ] \033[1;32mUse it for legal purposes only.
\033[1;33m  [ + ] \033[1;32mWe are not responsible for your actions.
\033[1;33m  [ + ] \033[1;32mDo not do things that are forbidden.

\033[1;31m If you are installing this tool,
 that means you agree with all terms.
''')

    @classmethod
    def installation_success(cls):
        cls.display('''
\033[1;33m    [ + ] \033[1;32mTool-X installed successfully.
\033[1;33m    [ + ] \033[1;32mTo run Tool-X,
\033[1;33m    [ + ] \033[1;32mType Tool-X in your terminal.
''')

    @classmethod
    def update(cls):
        cls.display('''
\033[1;33m  [ 1 ] \033[1;32mUpdate your Tool-X.
\033[1;33m  [ 0 ] \033[1;32mFor Back.\033[00m
''')

    @classmethod
    def updated(cls):
        cls.display('''
\033[1;33m      [ + ] \033[1;32mTool-X Updated Successfully.
\033[1;33m      [ + ] \033[1;32mPress Enter to continue.\033[00m
''')

    @classmethod
    def no_network(cls):
        cls.display('''
\033[1;31m  [ + ]  \033[1;31mNo network connection?\033[1;m
\033[1;31m  [ + ]  \033[1;31mAre you offline?\033[1;m
\033[1;31m  [ + ]  \033[1;31mPlease try again after some time.\033[00m
''')

    @classmethod
    def update_error(cls):
        cls.display('''
\033[1;31m  [ + ]  \033[1;31mWe can't update Tool-X.\033[1;m
\033[1;31m  [ + ]  \033[1;31mPlease try again after some time.\033[00m
''')

    @classmethod
    def about(cls, total):
        cls.display(f'''
\033[1;33m       [+] Tool Name :- \033[1;32mTool-X
\033[1;33m       [+] Author :- \033[1;32mNx PKG
\033[1;33m       [+] Latest Update :- \033[1;32m23/3/2019.\033[1;m
\033[1;33m       [+]
