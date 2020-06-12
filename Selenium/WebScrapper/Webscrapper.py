import  os  , re , csv , sys 
import requests , argparse
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd 
import socket

class TextColor:
    Yellow = '\x1b[1;33;40m'
    White = '\x1b[5;37;40m'
    Green = '\x1b[1;32;40m'
    Error = '\x1b[0;37;41m'
    Red = '\x1b[1;31;40m'
    End = '\x1b[0m'


class Webscrapper:

    VERSION =  1.0

    def __init__(self):
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.downloadPath = self.scriptDir + os.sep + 'downloads'
        if not os.path.exists(self.downloadPath):
            os.mkdir(self.downloadPath)
    
    def createSession(self,arque):
        self.arque = arque
        self.session = requests.session()
        self.session.headers.update(
                {
                    'Accept':'*/*',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language':'en-US,en;q=0.8',
                    'Connection':'keep-alive',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'
                })
        if self.arque['type'] == 'dark':
            try :
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex(('127.0.0.1',9150))
                print('\n[ INFO ] = Checking port 9150 ')
                if result == 0 :
                    print ("\n[ INFO ] = Port open ")
                else:
                    print ('\n[ WARNING ] =  Please launch TOR BROWSER first and try gain')
                    sock.close()
                    quit()
                self.session.proxies =  {}
                self.session.proxies['http'] = 'socks5h://127.0.0.1:9150'
                self.session.proxies['https'] = 'socks5h://127.0.0.1:9150'
            except Exception as e:
                print('\n[ Error ] = {}'.format(e))
            
    def fetch(self,url,ouputfile):
        r = self.session.get(url)
        if r.status_code == 200:
            print('\n[ INFO ] : Fetching url  = {} , Status = {} '.format(url , r.status_code ))
            soup = BeautifulSoup(r.content, 'html5lib')
            
            if isinstance(ouputfile[0],str) and len(ouputfile.strip()) > 3 :
                ouputfile = ''.join(o for o in ouputfile  if o.isalpha())
            else:
                ouputfile = soup.find('title').get_text()
                ouputfile = ''.join(o for o in ouputfile  if o.isalpha())

            ouputfile = self.downloadPath + os.sep + ouputfile
            textPath = ouputfile + '.txt'
            
            if self.argue['urls'] :
                extractedLinks = p[]
                links = soup.find_all('a')
                for l in links:
                    title = l.get_text()
                    url = l.get('href')
                    extractedLinks.append({'title':title,'url':url})

            if self.argue['photo']:
                extractedLinks = []
                imgTags = soup.find_all('img')
                for img in imgTags:
                    if img.get('alt'):
                        title = 'Image link  ' + str ( img.get('alt') ) 
                    else:
                        title = 'Image link '
                    url = img.get('src')
                    extractedLinks.append({'title':title,'url':url})

            if self.argue['video']:
                extractedLinks = []
                videoUrls = soup.find_all('video')
                for video in videoUrls:
                    url = video.get('src')
                    extractedLinks.append({'title':title,'url':url})
                self.writeText(path=textPath,data=videoUrls,msg='Videos')

            text = soup.find('body').get_text().replace('\n\n','\n')
            emails = ''
            phones = ''
            if text :
                if and self.arque['email']:
                    emails = re.findall('\S+@\S+', text)
                    self.writeText(path=textPath,data=emails,msg='Emails')
                if self.arque['phone']:
                    phones = re.findall('\\+?(?:\\s*?\\d{3,15}\\-*?)+',text)
                    self.writeText(path=textPath,data=phones,msg='Potential Phone numbers')
                if self.arque['raw']:
                    self.writeText(path=textPath,data=text,msg='Webpage RAW DATA',loop=False)

        else:
            print('\n[ WARNING ] : Server returned  {} , Could not access webpage {}  '.format(r.status_code,url))


    def writeText(self,path,data,msg,loop=True):
        with open(path,'a' , encoding='utf-8') as textFile :
            print('\n[ INFO ] : Writing {}  textfile {}'.format( msg ,  path))
            textFile.writelines('\n================= {} ========================\n'.format(msg))
            if loop:
                for d in data:
                    textFile.write(d)
                    textFile.write('\n')
                textFile.writelines('\n\n')
            else:
                textFile.writelines(data)
                

   
if __name__ == '__main__':
    print(TextColor.Red + 
    """
     _   _  _       _     
    | || || |     | |    
    | || || | ____| | _  
    | ||_|| |/ _  ) || \ 
    | |___| ( (/ /| |_) )
    \______|\____)____/ 
    """
    + TextColor.End)
    print('\n========== scrapper version {} ==========\n'.format(Webscrapper.VERSION))

    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--type",  required=True, help=" Determines type of web scraping dark or white")
    ap.add_argument("-i", "--input", required=True, help="Input file name to read from")

    ap.add_argument("-r", "--raw",    type=bool , help="Scarpe Webpage raw text ")
    ap.add_argument("-u", "--urls",   type=bool , help="Scrape all urls")
    ap.add_argument("-a", "--all",    type=bool , help="Scarpe Everything")
    ap.add_argument("-e", "--email",  type=bool , help="Extract possbile email addresses")
    ap.add_argument("-vi", "--video",  type=bool , help="extract video links")
    ap.add_argument("-p", "--photo",  type=bool , help="extract photo links")
    ap.add_argument("-m", "--mobile", type=bool , help="Extract possbile phone numbers")
    
    args = vars(ap.parse_args())
    # print(args['type'] , args['input'] , args['version'])
    webscrapper = Webscrapper()
    webscrapper.createSession(argus = args)
    
    inputFile = argue['input']
    if not os.path.exists(inputFile):
        print('\n[ WARNING ] : File does not exists {}'.format(inputFile))
        quit()
    csvFile = pd.read_csv(inputFile,dtype=str,encoding='utf-8')
    for keywords in csvFile.values:
        if isinstance(keywords[1],str) and 'http' in keywords[1] :
            webscrapper.fetch(url=keywords[1] , ouputfile= keywords[0])
        else:
            print('\n[ WARNING ] : Invalid format url {}'.format(keywords[1]))