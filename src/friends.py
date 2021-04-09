import os, re, sys, json
from bs4 import BeautifulSoup as parser
from datetime import datetime

def main(self, cookie, url, config):
    flist = raw_input('\n \x1b[0;97m[\x1b[0;91m?\x1b[0;97m] Linke aw Frendanay atawe dayne\x1b[0;91m : \x1b[0;90m')
    try:
        domain = flist.split('//')[1].split('/')[0]
        flist = flist.replace(domain, 'mbasic.facebook.com')
    except IndexError:
        print '\n\x1b[0;97m  [\x1b[0;91m!\x1b[0;97m]\x1b[0;91m Url Tidak Ada'
        os.system('python2 crack.py')

    output = re.findall('https:\\/\\/.*?\\/(.*?)\\/friends\\?lst=', flist)
    _output = re.findall('id=(.*?)&refid=', flist)
    if len(output) == 0 and len(_output) == 0:
        print '\n\x1b[0;97m  [\x1b[0;91m!\x1b[0;97m]\x1b[0;91m Url Tidak Ada'
        os.system('python2 crack.py')
    else:
        if len(output) != 0:
            output = '' + output[0] + ''
        else:
            output = '' + _output[0] + ''
        id = []
        print ''
        while True:
            try:
                response = config.httpRequest(flist, cookie).encode('utf-8')
                html = parser(response, 'html.parser')
                for x in html.find_all(style='vertical-align: middle'):
                    find = x.find('a')
                    if '+' in str(find) or find == None:
                        continue
                    else:
                        full_name = str(find.text.encode('utf-8'))
                        if '/profile.php?id=' in str(find):
                            uid = re.findall('/?id=(.*?)&', find['href'])
                        else:
                            uid = re.findall('/(.*?)\\?fref=', find['href'])
                        if len(uid) == 1:
                            id.append({'uid': uid[0], 'name': full_name})
                        sys.stdout.write('\x1b[0;90m>>>\x1b[0;91m %s                                        \n\x1b[0;97m[\x1b[0;96m%s\x1b[0;97m] [\x1b[0;96m%s\x1b[0;97m] S e Z a R ' % (
                         full_name,datetime.now().strftime('%H:%M:%S'), len(id)))
                        sys.stdout.flush()

                if 'Lihat Teman Lain' in str(html):
                    flist = url + html.find('a', string='Lihat Teman Lain')['href']
                else:
                    break
            except KeyboardInterrupt:
                print '\n\n \x1b[0;97m [\x1b[0;91m!\x1b[0;97m] \x1b[0;91mError, Berhenti'
                break

        try:
            for filename in os.listdir('user'):
                os.remove('' + filename)

        except:
            pass

    print '\n\n\x1b[0;92mOutput \x1b[0;91m:\x1b[0;96m ' + output
    save = open(output, 'w')
    save.write(json.dumps(id))
    save.close()
    return
