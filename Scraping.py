import urllib2

if __name__ == '__main__':
    file="downloaded_file.html"
    url="http://python.org/"
    response=urllib2.urlopen(url)
    fh=open(file,'w')
    fh.write(response.read())
    fh.close()

