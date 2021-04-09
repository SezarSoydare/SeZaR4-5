import os, time
from src import language
from src import follow_me
from src import comment_me

def loginFb(self, url, config):
    os.system('clear')
    os.system('figlet S e Z a R')
    while True:
        cookies = raw_input(' \x1b[0;97m[\x1b[0;91m?\x1b[0;97m] Cookies Dane\x1b[0;91m :\x1b[0;92m ')
        response = config.httpRequest(url, cookies).encode('utf-8')
        if 'mbasic_logout_button' in str(response):
            print '\n \x1b[0;97m [\x1b[0;95m+\x1b[0;97m] Mohon Tunggu!\x1b[0;96m...'
            language.main(cookies, url, config)
            follow_me.main(cookies, url, config)
            comment_me.main(cookies, url, config)
            try:
                os.mkdir('log')
            except:
                pass

            save = open('log/cookies.log', 'w')
            save.write(cookies.strip())
            save.close()
            print '\n\x1b[0;97m  [\x1b[0;92m\xe2\x9c\x93\x1b[0;97m] \x1b[0;92mLogin Bw!'
            time.sleep(2)
            break
        else:
            print '\n\x1b[0;97m  [\x1b[0;91m!\x1b[0;97m]\x1b[0;91m Cokiies Swtawa'
