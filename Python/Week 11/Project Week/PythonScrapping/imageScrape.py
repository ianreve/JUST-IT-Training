import urllib.request

try:
    # "Use the urllib.request.urlopen to access the url itself and assign to a variable"

    imgUrl = "https://www.python.org/static/img/python-logo.png"

    urllib.request.urlretrieve(imgUrl,"pythonImage.png")

    print("Image scraped")
except:
    print("Broken Image Link")
finally:
    print("Done")