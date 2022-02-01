import urllib.request
import urllib.error


try:
    # " use the urllib.request. access the url itself and asssign to a variable"
    webURL = urllib.request.urlopen("https://www.python.org")

    readContent = webURL.read()
    
    file1 = open("PythonScraping/website1.html", "wb") # wb = write binary
    file1.write(readContent) 

except urllib.error.HTTPError:
    raise("Web page not found")

finally:
    webURL.close()
    file1.close()