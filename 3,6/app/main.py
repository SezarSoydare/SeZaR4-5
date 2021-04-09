import os, time
from app import config
from app import login
from app import crack
from src import friends_list
from src import friends
from src import search_name
from src import likes
from bs4 import BeautifulSoup as parser

class Brute(object):

    def __init__(self, url):
        self.url = url
        self.config = config.Config()
        self.cookie = self.config.loadCookie()
        self.menu = ' '
        self.menu += '\x1b[0;97m[\x1b[0;96m1\x1b[0;97m] Darhenani UserName Frendakant\n'
        self.menu += ' \x1b[0;97m[\x1b[0;96m2\x1b[0;97m] Darhenani UserName Public\n'
        self.menu += ' \x1b[0;97m[\x1b[0;96m3\x1b[0;97m] Darhenani naw la rey Naw nwsin\n'
        self.menu += ' \x1b[0;97m[\x1b[0;96m4\x1b[0;97m] Darhenani UserName Post\n'
        self.menu += ' \x1b[0;97m[\x1b[0;96m5\x1b[0;97m] Dast Pe Krdni \033[1;92mHack\033[1;97m\n'
        self.menu += ' \x1b[0;97m[\x1b[0;96m6\x1b[0;97m] Darchwn La acawnt\n'
        self.menu += ' \x1b[0;97m[\x1b[0;91m0\x1b[0;97m] Darchwn\n'
        self.menu += '\033[1;97m----------------------------------------------------------------------------\033[1;97m'
        if self.cookie == False:
            login.loginFb(self, self.url, self.config)
            self.cookie = self.config.loadCookie()

    def start(self):
        response = self.config.httpRequest(self.url + '/profile.php', self.cookie).encode('utf-8')
        if 'mbasic_logout_button' in str(response):
            self.main(response)
        else:
            os.remove('log/cookies.log')
            print '\n\x1b[0;97m[\033[1;91mAGADARE\033[1;97m]\033[1;91m Chockiesakat ba kalk naya tkaya Danayki taza dane\x1b[0m'
            raw_input('\n[ Press Enter]')
            login.loginFb(self, self.url, self.config)
            self.cookie = self.config.loadCookie()
            self.start()
            exit()

    def main(self, response):
        os.system('clear')
        os.system('figlet S e Z a R')

        html = parser(response, 'html.parser')
        print '\033[1;97m----------------------------------------------------------------------------\033['
        print ('\x1b[0;97m [\x1b[0;95m\xc3\x97\x1b[0;97m] \x1b[0;96mNawe Acawntakat \x1b[0;91m:\x1b[0;93m ').decode('utf-8') + html.title.text.upper()
        print '\033[1;97m----------------------------------------------------------------------------\033['
        print self.menu
        try:
            choose = int(raw_input('\x1b[1;97m [\x1b[1;94m\xe2\x80\xa2\x1b[1;91m\xe2\x80\xa2\x1b[1;97m] \x1b[90m\xe2\x96\xba\x1b[1;93m '))
        except ValueError:
            print '\n\x1b[0;97m [\x1b[0;91m!\x1b[0;97m]\x1b[0;91m Lihat Menu Dong Ajg'
            os.system('python2 crack.py')

        if choose == 1 or choose == 1:
            exit(friends_list.main(self, self.cookie, self.url, self.config))
        elif choose == 2 or choose == 2:
            exit(friends.main(self, self.cookie, self.url, self.config))
        elif choose == 3 or choose == 3:
            exit(search_name.main(self, self.cookie, self.url, self.config))
        elif choose == 4 or choose == 4:
            exit(likes.main(self, self.cookie, self.url, self.config))
        elif choose == 5 or choose == 5:
            ngentod = raw_input('\n\x1b[0;97m[\x1b[0;91m?\x1b[0;97m] Datawedast bkay ba Crack [y/n]\x1b[0;91m :\x1b[0;92m ')
            print '\033[1;97m----------------------------------------------------------------------------\033['
            if ngentod.lower() == '':
                exit('\n  \x1b[0;91mTkaya y/n halbzhera!')
            elif ngentod.lower() == 'y':
                exit(crack.Brute().main())
            elif ngentod.lower() == 'n':
                os.system('python2 crack.py')
            else:
                exit('  \x1b[0;91mTkaya y/n Halbzhera!')
        elif choose == 777262777777 or choose == 777262777777:
            print '\n\n\x1b[0;92m   [ \x1b[0;96mMohon Tunggu Sedang Meng Update Tools \x1b[0;92m]\n'
            time.sleep(2)
            os.system('git pull')
            print ' \n\x1b[0;97m[\x1b[0;92m\xe2\x9c\x93\x1b[0;97m]\x1b[0;92m Berhasil Di Update!\n'
            time.sleep(2)
            os.system('python2 crack.py')
        elif choose == 0 or choose == 0:
            time.sleep(2)
            os.system('exit')
            os.system('exit')
        elif choose == 6 or choose == 6:
            ask = raw_input('\n\x1b[0;97mDatawe darchet la chockiesakat? [y/n]\x1b[0;91m :\x1b[0;92m ')
            if ask.lower() == 'y':
                print '\n \x1b[0;97m  [\x1b[0;95m\xe2\x80\xa2\x1b[0;97m] Darchwet\x1b[0;92m...'
                time.sleep(2)
                os.remove('log/cookies.log')
                print '\n\x1b[0;97m  [\x1b[0;92m\xe2\x88\x9a\x1b[0;97m] !'
                time.sleep(2)
                login.loginFb(self, self.url, self.config)
                self.cookie = self.config.loadCookie()
                self.start()
            else:
                self.cookie = self.config.loadCookie()
                print '\n\x1b[0;97m  [\x1b[0;91m!\x1b[0;97m] \x1b[0;91mBatal Terhapus'
                self.start()
        else:
            print '\n \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] \x1b[0;91mLihat Menu Dong Ajg'
            os.system('python2 crack.py')
