import re
import urllib.request

def getHtml(url):
    try:
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        return html
    except:
        # traceback.print_exc()
        print('The URL you requested could not be found')
        return 'Html'

def BlogStyleDetection(url):
    html = getHtml(url)
    reg = 'http://static.tumblr.com/qexbavb/ZpSodrpj0/main-min.css'
    defaultStylere = re.compile(reg)
    detection = re.findall(defaultStylere, html)

    if detection:
        print('Default theme')
        return True
    else:
        print('Using personal theme!')
        return False

if __name__ == '__main__':
    select = 'N'
    while not(select == 'Y'):
        URL = input('Input url: ')
        BlogStyleDetection(URL)
        select = input("Do you want to Quit? [Y/N]")