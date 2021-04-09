import os, re, sys, json
from bs4 import BeautifulSoup as parser
from datetime import datetime

def main(self, cookie, url, config):
    ask = raw_input('\n     \x1b[0;97m    [\x1b[0;95m\xe2\x80\xa2\x1b[0;97m]\x1b[0;92m Nawek Dane : S e Z a R \x1b[0;97m[\x1b[0;95m\xe2\x80\xa2\x1b[0;97m]\n\n \x1b[0;97m[\x1b[0;91m?\x1b[0;97m] Nawek Dane \x1b[0;91m:\x1b[0;96m ')
    if ask.strip() == '':
        exit('\n  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] \x1b[0;91mTidak boleh kosong')
    try:
        max = int(raw_input('\x1b[0;97m [\x1b[0;91m?\x1b[0;97m] Chan UserName t awe [\x1b[0;93m1 \033[1;90m-> \x1b[0;96m5000\x1b[0;97m]\x1b[0;91m :\x1b[0;96m '))
    except ValueError:
        exit('\n  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] \x1b[0;91mTidak Boleh Kosong')

    if max == 0:
        exit('\n  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] \x1b[0;91mTidak boleh kosong')
    url_search = url + '/search/people/?q=' + ask
    statusStop = False
    output = '' + ask.replace(' ', '_') + ('.json').strip()
    id = []
    print ''
    while True:
        try:
            response = config.httpRequest(url_search, cookie).encode('utf-8')
            html = parser(response, 'html.parser')
            find = html.find_all('a')
            for i in find:
                name = i.find('div')
                if '+' in str(name) or name == None:
                    continue
                else:
                    full_name = str(name.text.encode('utf-8'))
                    if 'profile.php?id=' in str(i):
                        uid = re.findall('\\?id=(.*?)&', str(i))
                    else:
                        uid = re.findall('/(.*?)\\?refid=', str(i))
                    if len(uid) == 1:
                        id.append({'uid': uid[0], 'name': full_name})
                    sys.stdout.write('\x1b[0;90m>>>\x1b[0;96m %s                                        \r\n\x1b[0;97m[\x1b[0;92m%s\x1b[0;97m] [\x1b[0;96m%s\x1b[0;97m] \033[1;91mS e Z a R\033[1;97m ' % (
                     full_name, datetime.now().strftime('%H:%M:%S'),len(id)))
                    sys.stdout.flush()
                    if len(id) == max or len(id) > max:
                        statusStop = True
                        break

            if statusStop == False:
                if 'Lihat Hasil Selanjutnya' in str(html):
                    url_search = html.find('a', string='Lihat Hasil Selanjutnya')['href']
                else:
                    break
            else:
                break
        except KeyboardInterrupt:
            print '\n\n  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] \x1b[0;91mError, Berhenti'
            break

    try:
        for filename in os.listdir(''):
            os.remove('' + filename)

    except:
        pass

    print '\n\n\x1b[0;92mNawe File \x1b[0;91m:\x1b[0;96m ' + output
    save = open(output, 'w')
    save.write(json.dumps(id))
    save.close()
    return
