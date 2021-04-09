import os, re, sys, json
from bs4 import BeautifulSoup as parser
from datetime import datetime

def main(self, cookie, url, config):
    post = raw_input('\n\x1b[0;97m [\x1b[0;91m?\x1b[0;97m] Linke Aw Postay Atawe \x1b[0;91m:\x1b[0;92m ')
    try:
        domain = post.split('//')[1].split('/')[0]
        post = post.replace(domain, 'mbasic.facebook.com')
    except IndexError:
        exit('\n  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] \x1b[0;91mLink Bakalk Naya')

    url_likes = None
    response = config.httpRequest(post, cookie).encode('utf-8')
    html = parser(response, 'html.parser')
    for x in html.find_all('a'):
        if '/ufi/reaction/profile/browser/?' in x['href']:
            url_likes = url + x['href']
            break

    if url_likes == None:
        exit('\n\x1b[0;97m  [\x1b[0;91m!\x1b[0;97m] \x1b[0;91mAw Linka Bwni Nya.')
    try:
        max = int(raw_input('\x1b[0;97m [\x1b[0;91m?\x1b[0;97m] Chand Id t Awe\x1b[0;97m[\x1b[0;96m1 \033[1;90m>>> \x1b[0;91m5000\x1b[0;97m] \x1b[0;91m:\x1b[0;92m '))
    except ValueError:
        exit('\n\x1b[0;97m  [\x1b[0;91m!\x1b[0;97m] \x1b[0;91m')

    if max == 0:
        exit('\n\x1b[0;97m  [\x1b[0;91m!\x1b[0;97m] \x1b[0;91m')
    statusStop = False
    output = 'user/likes.json'
    id = []
    print ''
    while True:
        try:
            response = config.httpRequest(url_likes, cookie).encode('utf-8')
            html = parser(response, 'html.parser')
            find = html.find_all('h3')
            for i in find:
                full_name = i.text.encode('utf-8')
                href = i.find('a')
                if '+' in str(href) or href == None:
                    continue
                else:
                    if 'profile.php?id=' in str(i):
                        uid = re.findall('\\/profile.php\\?id=(.*?)$', href['href'])
                    else:
                        uid = re.findall('\\/(.*?)$', href['href'])
                    if len(uid) == 1:
                        id.append({'uid': uid[0].replace('/', ''), 'name': full_name})
                    sys.stdout.write('\r\x1b[0;90m>>>\x1b[0;96m %s                                        \n\x1b[0;97m[\x1b[0;92m%s\x1b[0;97m] [\x1b[0;96m%s\x1b[0;97m] \033[1;91mS e Z a R\033[1;97m ' % (
                     full_name, datetime.now().strftime('%H:%M:%S'), len(id)))
                    sys.stdout.flush()
                    if len(id) == max or len(id) > max:
                        statusStop = True
                        break

            if statusStop == False:
                if 'Lihat Selengkapnya' in str(html):
                    url_likes = url + html.find('a', string='Lihat Selengkapnya')['href']
                else:
                    break
            else:
                break
        except KeyboardInterrupt:
            break

    try:
        for filename in os.listdir('user'):
            os.remove('user/' + filename)

    except:
        pass

    print '\n\n\n\x1b[0;92mFiley Like \x1b[0;91m: \x1b[0;92m ' + output +'\n\n'
    save = open(output, 'w')
    save.write(json.dumps(id))
    save.close()
    return
