import requests
import sys
import math


link = 'https://instagram.fbom12-1.fna.fbcdn.net/v/t50.16885-16/10000000_123337149018059_8710617816798797076_n.mp4?_nc_ht=instagram.fbom12-1.fna.fbcdn.net&_nc_cat=111&_nc_ohc=UIyP3Zw52AIAX9Qii0v&oe=5E9A7FFE&oh=90122e68e1ed0e7a05e194b6c5497b93'
link2 = 'https://instagram.fbom12-1.fna.fbcdn.net/v/t51.2885-15/e35/67638638_476560662900878_7219668273807769514_n.jpg?_nc_ht=instagram.fbom12-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=yj0cULqnPGUAX82CS5Y&oh=4008b6dc0bd4216ef657dd066e573e48&oe=5EC13845'


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


fileName = 'abc.mp4'
r = requests.get(link,stream=True)
if r.status_code == 200:
    with open(fileName, 'wb') as f:
        total = int(r.headers.get('content-length'))
        size = convert_size(total)
        print('Total length = {}'.format(size))
        if total is None:
            f.write(r.content)
        else:
            downloaded = 0
            for data in r.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)
                sys.stdout.write('\r[{}{}]'.format('#' * done, '.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')