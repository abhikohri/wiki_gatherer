from bs4 import BeautifulSoup
from urllib.request import urlopen
import os


print("""This Tool is used for gathering information about anything from wikipedia""")
query = input("enter your object:")
print("https://en.wikipedia.org/wiki/" + query)

def gatherer(input):
    http = urlopen("https://en.wikipedia.org/wiki/" + input)
    b_h = BeautifulSoup(http, 'html.parser')
    s =b_h.get_text()
    if not os.path.exists(input):
        print("creating directory" + input)
        os.makedirs(input)

        file = input + "/info.txt"

        if not os.path.isfile(file):
            print("file created" + file + ".txt")
            write_file(file, s)

def write_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()




gatherer(query)
