
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os


print("""\n\n\n This Tool is used for gathering information about anything from wikipedia\n\n\n""")
query = input("enter your object:")
new_arc = ""


for i in query:
    if i == ' ':
        i = "_"
    new_arc = new_arc + i
print("https://en.wikipedia.org/wiki/" + new_arc)

http = urlopen("https://en.wikipedia.org/wiki/" + new_arc)
b_h = BeautifulSoup(http, 'html.parser')

def gatherer(input):
    s =b_h.get_text()
    s_2 = b_h.find("h1",{"class":"firstHeading"}).get_text()
    print(s_2)

    directory_create(input)
    file = input + "/"+ s_2 +".txt"
    if not os.path.isfile(file):
        print("file created " + file)



    o1(new_arc)
def write_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()

def directory_create(inp):
    if not os.path.exists(inp):
        print("creating directory " + inp)
        os.makedirs(inp)

def o1(o1input):
    main_list = ""
    second = ""


    for c in b_h.find_all():
        if len(main_list) > 0:
            for z in main_list:
                z = BeautifulSoup(z, "html.parser")
                if c.get_text() == z.get_text():
                    break
        for jong in b_h.find_all("h2"):

            if c == jong:
                
                name = new_arc + "/" + str(c.get_text()) + ".txt"

                f = open(name, "w")

                f.write(str(c.get_text()) + "\n\n")
                main_list = main_list + c.get_text()





            else:
                if len(main_list) == 0:
                    break
                
                for q in second:
                    if c == q:
                        
                        break

                for kim in b_h.find_all("p"):
                    
                    if c == kim:
                        
                        f.write(c.get_text())
                        second = second + c.get_text()
                        
                        for o2 in b_h.find_all("h2"):
                            o2 = str(o2)
                            if c == o2:
                                f.close()
                                
                                break





gatherer(new_arc)
