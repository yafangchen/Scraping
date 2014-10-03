import urllib2

def url2file(url, filename):
    """Scrape content from url, and save to filename

    Retrieve content from url, save to file.

    Args:
        url: a string of website. e.g. http://google.com
        filename: the absolute name of file.

    Returns:
        None

    Raises:
        IOError: An error occurred accessing file.
        HTTPError: An error occurred accessing url.
    """
    pass

if __name__ == '__main__':
    file="downloaded_file.html"
    url="http://python.org/"
    response=urllib2.urlopen(url)
    fh=open(file,'w')
    fh.write(response.read())
    fh.close()

