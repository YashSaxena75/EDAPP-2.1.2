import getpass
import uuid, random, progressbar, os
newpath = r'C:\Arb'
if not os.path.exists(newpath):
    os.makedirs(newpath)

if os.path.exists(newpath):
    if not os.path.exists(r"C:\Arb\passw.txt"):
        f = open(r"C:\Arb\passw.txt", "a+")
        f.write('0')
        f.close()
    if not os.path.exists(r"C:\Arb\ans.txt"):
        g = open(r"C:\Arb\ans.txt", "a+")
        g.write('0')
        g.close()
    if not os.path.exists(r"C:\Arb\log.txt"):
        h = open(r"C:\Arb\log.txt", "a+")
        h.close()
def p():
    print(Fore.GREEN + """
  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
( E | N | C | R | Y | P | T | I | O | N | D | E | C | R | Y | P | T | I | O | N )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
                                                                                                       """)
    print(Style.RESET_ALL)
def auth():
    print(Fore.RED + "αυтнσя ηαмε:үαsн sαxεηα(нυм4ησ!∂_н473я)")
    print(Style.RESET_ALL)

import colorama, time
from colorama import Fore, Style
colorama.init()
import os
x = uuid.getnode()
c = str(x)
p()
auth()
def ran():
    h = open(r'C:\Arb\log.txt', 'r')
    v = h.readline(len(c))
    if (len(v)) == len(c):
        print("Already Registered!")

    else:
        t = random.randrange(0, 5000000000000)
        print("Registering u now....")
        f = open(r'C:\Arb\log.txt', 'a')
        f.write(c)
        f.write("\n")
        f.write(str(t))
        f.write("\n")
        f.close()
ran()

import ctypes
import random
import secrets
import string
import datetime
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
def mail():
    c = True
    while c:
        try:
            fromaddr = "cyberbot1502@gmail.com"
            toaddr = "cyberbot1502@gmail.com"
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Log file"
            body = "Logger"
            msg.attach(MIMEText(body, 'plain'))
            filename = "log.txt"
            attachment = open(r"C:\Arb\log.txt", "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename=%s" % filename)
            msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(fromaddr, "Hexadecimalqwertyuiop")
            text = msg.as_string()
            s.sendmail(fromaddr, toaddr, text)
            print("Mail Sent!")
            c = False
        except Exception:
            time.sleep(5)
            print("No Internet please try Again!")
            c = True

    s.quit()
x = datetime.datetime.now()

cur = x.strftime("%x")
curr = str(cur)

alphabet = string.ascii_letters + string.digits
ran1 = ''.join(secrets.choice(alphabet) for i in range(9))
f = ''.join(random.sample(string.ascii_lowercase, 9))
def prnt():
    print("""                      

                                     1.encrypt the text
                                     2.Decrypt the text



                                                                                           """)
def bar():
    progress = progressbar.ProgressBar()
    for i in progress(range(12)):
        time.sleep(0.1)
k = ''
import os
import sys
import time
print("Just For Security Purpose Answer a Question")
print("\n\n")
def Pet():
    l = open(r'C:\Arb\log.txt', 'r')
    h = l.readlines()
    print(Fore.LIGHTGREEN_EX + "Your REG.ID is:", h[1])
    print(Style.RESET_ALL)
    time.sleep(5)
    h = open(r"C:\Arb\log.txt")
    h.close()
    print("Default Pet name is:NULL", "Please change this to your pet name for security Purpose!")
    # petn = getpass.getpass(prompt='What is your pet name>>')
    petn = input("Pet name>")
    li = len(petn)
    p = None
    while li != 0:
        j = open(r"C:\Arb\ans.txt", "w")
        j.write('1')
        j.close()
        nl = len(f)
        l = open(r"C:\Arb\ans.txt", "a")
        l.write(str(nl))
        l.close()
        j = open(r"C:\Arb\ans.txt", "a")
        j.write(f)
        j.close()
        while p != 0:
            for i in petn:
                j = ord(i)
                a = petn.index(i)
                if i.strip():
                    if j >= 97 and j <= 109 or j >= 65 and j <= 77:
                        j = j + 13
                        p = open(r"C:\Arb\ans.txt", "a")
                        p.write(chr(j))
                        li = li - 1
                        p = 0

                    elif j >= 110 and j <= 122 or j >= 78 and j <= 90:
                        j = j - 13
                        p = open(r"C:\Arb\ans.txt", "a")
                        p.write(chr(j))
                        li = li - 1
                        p = 0

                    elif j == 32:
                        p = open(r"C:\Arb\ans.txt", "a")
                        p.write(chr(j))
                        li = li - 1
                        p = 0
                else:
                    print("can't leave this field blank!")
                    time.sleep(4)
                    p = 1
                    sys.exit(0)

    c = open(r"C:\Arb\ans.txt")
    x = c.readlines()
    c.close()
    g = open(r"C:\Arb\ans.txt", "r+")
    for line in x:
        g.write(line[1:])
        g.truncate()
h = open(r"C:\Arb\ans.txt", "r")
if (os.path.getsize(r"C:\Arb\ans.txt") == 1) or (os.path.getsize(r"C:\Arb\passw.txt") == 1):
    Pet()

else:
    print("As u have completed the Security Question So proceeding further!")
    time.sleep(4)
    os.system("cls")
    auth()

x = int(input("enter 0 to set ur new password and 1 to continue with the old one:"))
cho = None
if x == 1:
    st = ""
    count = 0
    # pas = getpass.getpass(prompt='Enter Your Password here>')
    pas = input("Enter ur pass>")
    d = open(r"C:\Arb\passw.txt", "r")
    f = d.read()
    d.close()
    li = len(f)
    v = 0
    randlen = int(f[0])
    for i in range(li):
        if v <= randlen:
            v = v + 1
        else:
            st = st + f[i]
    li = len(st)
    while li != 0:
        str = ""
        for i in st:
            j = ord(i)
            if j >= 119 and j <= 122 or j >= 87 and j <= 90:
                j = j - 22
                str = str + chr(j)
                li = li - 1

            elif j >= 97 and j <= 118 or j >= 65 and j <= 86:
                j = j + 4
                str = str + chr(j)
                li = li - 1

            elif j == 32:
                str = str + chr(32)
                li = li - 1

            elif j >= 48 and j <= 57:
                str = str + chr(j)
                li = li - 1
    if pas == str:
        print("Password verified successfuly...")
        os.system("cls")
        auth()
        count = 1

    elif pas != str:
        print(Fore.RED + "Wrong Password!", "If forget ur password then change it in next run!Thank You!")
        print(Style.RESET_ALL)
        time.sleep(5)
        li = 0
        sys.exit(0)

    FILE_ATTRIBUTE_HIDDEN = 0x02

    rett = ctypes.windll.kernel32.SetFileAttributesW(r'C:\Arb\passw.txt',
                                                     FILE_ATTRIBUTE_HIDDEN)
    rettt = ctypes.windll.kernel32.SetFileAttributesW(r'C:\Arb\ans.txt',
                                                      FILE_ATTRIBUTE_HIDDEN)

s = open(r"C:\Arb\passw.txt", "r")
u = s.read()
l = len(u)

if x == 0:
    FILE_ATTRIBUTE_HIDDEN = 0x80

    rett = ctypes.windll.kernel32.SetFileAttributesW(r'C:\Arb\passw.txt',
                                                     FILE_ATTRIBUTE_HIDDEN)
    rettt = ctypes.windll.kernel32.SetFileAttributesW(r'C:\Arb\ans.txt',
                                                      FILE_ATTRIBUTE_HIDDEN)
    if os.path.exists(newpath):
        f = open(r"C:\Arb\passw.txt", "w+")
        f.write('0')
        f.close()
    if l == 1:
        f = open(r"C:\Arb\passw.txt", "r")
        g = f.read()
        print("Default Password is:", g, " change this to your password,for security reasons you know very well!")
        # pasn = getpass.getpass(prompt='Enter Your new Password here>>>')
        pasn = input("Enter ur new pass>>")
        nl = len(ran1)
        print("Please note down this password and REG.ID becuase u need this for login purpose")
        li = len(pasn)
        p = open(r"C:\Arb\passw.txt")
        x = p.readlines()
        p.close()
        g = open(r"C:\Arb\passw.txt", "r+")
        i = list(pasn)
        u = i.index(i[0])
        for line in x:
            g.write(line[1:u])
            g.truncate()
        g.close()
        l = open(r"C:\Arb\passw.txt", "a")
        l.write(str(nl))
        l.close()
        e = open(r"C:\Arb\passw.txt", "a")
        e.write(ran1)
        e.close()
        while li != 0:
            for i in pasn:
                j = ord(i)
                if j >= 97 and j <= 100 or j >= 65 and j <= 68:
                    j = j + 22
                    f = open(r"C:\Arb\passw.txt", "a")
                    f.write(chr(j))
                    f.close()
                    li = li - 1

                elif j >= 101 and j <= 122 or j >= 69 and j <= 90:
                    j = j - 4
                    n = open(r"C:\Arb\passw.txt", "a")
                    n.write(chr(j))
                    n.close()
                    li = li - 1

                elif j == 32:
                    d = open(r"C:\Arb\passw.txt", "a")
                    d.write(chr(j))
                    d.close()
                    li = li - 1

                elif j >= 48 and j <= 57:
                    s = open(r"C:\Arb\passw.txt", "a")
                    s.write(chr(j))
                    s.close()
                    li = li - 1

        time.sleep(2)
        print("Please Restart the tool now...")

        time.sleep(3)
        sys.exit(0)
        count = 0

    else:
        b = None
        while b != 0:
            st = ""
            q = int(input("Forget Password??, No problem enter 1 here to set a new password:"))
            if q == 1:
                nl = len(ran1)
                nll = str(nl)
                # a =getpass.getpass(prompt='Enter Your Pet name to verify it is u>>>>')
                a = input("Pet name to verify it is u:")
                d = open(r"C:\Arb\ans.txt", "r")
                f = d.read()
                d.close()
                li = len(f)
                v = 0
                b = 0
                randlen = int(f[0])
                for i in range(li):
                    if v <= randlen:
                        v = v + 1
                    else:
                        st = st + f[i]
                li = len(st)

                while li != 0:
                    str = ""
                    for i in st:
                        j = ord(i)
                        if j >= 97 and j <= 109 or j >= 65 and j <= 77:
                            j = j + 13
                            str = str + chr(j)
                            li = li - 1
                        elif j >= 110 and j <= 122 or j >= 78 and j <= 90:
                            j = j - 13
                            str = str + chr(j)
                            li = li - 1

                        elif j == 32:
                            str = str + chr(j)
                            li = li - 1

                print("Verifying from database")
                i = input("Enter ur REG.ID for verification:")
                q = open(r'C:\Arb\log.txt', 'r')
                g = q.readlines()
                x = g[1].rstrip('\n')
                time.sleep(10)
                if str == a and i == x:
                    print("You are Verified....")
                    j = open(r"C:\Arb\passw.txt", "w")
                    j.write('1')
                    j.close()
                    p = open(r"C:\Arb\passw.txt", "a")
                    # pasnn=getpass.getpass(prompt='Enter Your new password>>>>')
                    pasnn = input("Enter ur new pass>")
                    li = len(pasnn)
                    p = open(r"C:\Arb\passw.txt")
                    x = p.readlines()
                    p.close()
                    l = open(r"C:\Arb\passw.txt", "a")
                    l.write(nll)
                    l.close()
                    e = open(r"C:\Arb\passw.txt", "a")
                    e.write(ran1)
                    e.close()

                    while li != 0:
                        for i in pasnn:
                            j = ord(i)
                            if j >= 97 and j <= 100 or j >= 65 and j <= 68:
                                j = j + 22
                                f = open(r"C:\Arb\passw.txt", "a")
                                f.write(chr(j))
                                f.close()
                                li = li - 1

                            elif j >= 101 and j <= 122 or j >= 69 and j <= 90:
                                j = j - 4
                                n = open(r"C:\Arb\passw.txt", "a")
                                n.write(chr(j))
                                n.close()
                                li = li - 1

                            elif j == 32:
                                d = open(r"C:\Arb\passw.txt", "a")
                                d.write(chr(j))
                                d.close()
                                li = li - 1

                            elif j >= 48 and j <= 57:
                                s = open(r"C:\Arb\passw.txt", "a")
                                s.write(chr(j))
                                s.close()
                                li = li - 1

                    p = open(r"C:\Arb\passw.txt")
                    x = p.readlines()
                    p.close()
                    g = open(r"C:\Arb\passw.txt", "r+")
                    for line in x:
                        g.write(line[1:])
                        g.truncate()

                    print("Changing the password")

                    bar()
                    print("Password Changed Successfuly,Restart the app to use it")
                    time.sleep(3)
                    sys.exit(0)

                else:
                    print(Fore.RED + "Security Check Failed!!Exiting,Try again")
                    print(Fore.LIGHTBLUE_EX + "Contact Admin to know ur REG.ID")
                    print(Style.RESET_ALL)

                    time.sleep(3)
                    sys.exit(0)
            else:
                print("Wrong Choice !")
                b = 1

            count = 0

    FILE_ATTRIBUTE_HIDDEN = 0x02

    rett = ctypes.windll.kernel32.SetFileAttributesW(r'C:\Arb\passw.txt',
                                                     FILE_ATTRIBUTE_HIDDEN)
    rettt = ctypes.windll.kernel32.SetFileAttributesW(r'C:\Arb\ans.txt',
                                                      FILE_ATTRIBUTE_HIDDEN)
def bashenc():
    q = open(r"C:\Arb\log.txt", "a")
    q.write("In function bashenc at:" + curr)
    q.write(' ')
    q.write("\n")
    q.close()

    s = input("Enter the message to Encrypt:")
    s1 = ""
    for k in s:
        j = ord(k)
        if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
            s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))

        elif j >= 48 and j <= 57:
            # print(chr(j), end="")
            s1 += chr(j)


        elif j >= 33 and j <= 47:
            s1 += chr(j)


        elif j >= 58 and j <= 64:
            # print(chr(j), end="")
            s1 += chr(j)


        elif j >= 91 and j <= 96:
            # print(chr(j), end="")
            s1 += chr(j)

        elif j >= 123 and j <= 126:
            # print(chr(j), end="")
            s1 += chr(j)


        else:
            s1 += k

    print(Fore.CYAN + "Encrypted message is:")
    print(s1)
    print(Style.RESET_ALL)
    q = open(r"C:\Arb\log.txt", "a")
    q.write("Successful execution of bashenc() at :" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
def bashdec():
    q = open(r"C:\Arb\log.txt", "a")
    q.write("In function bashdec at:" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
    s = input("Enter the message to Decrypt:")
    s1 = ""
    for k in s:
        j = ord(k)
        if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
            s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))

        elif j >= 48 and j <= 57:
            s1 += chr(j)


        elif j >= 33 and j <= 47:
            s1 += chr(j)


        elif j >= 58 and j <= 64:
            s1 += chr(j)


        elif j >= 91 and j <= 96:
            s1 += chr(j)


        elif j >= 123 and j <= 126:
            s1 += chr(j)


        else:
            s1 += k

    print(Fore.CYAN + "Decrypted message is:", s1)
    print(Style.RESET_ALL)
    q = open(r"C:\Arb\log.txt", "a")
    q.write("Successful execution of bashdec() at :" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
def rotenc():
    q = open(r"C:\Arb\log.txt", "a")
    q.write("In function rotenc at:" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
    s = ""
    j = None
    s = input("Enter ur string here to encrypt:")
    li = len(s)
    print(Fore.CYAN + "Encrypted message is:", end="")
    print(Style.RESET_ALL)
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if j >= 97 and j <= 109 or j >= 65 and j <= 77:
                j = j + 13
                print(chr(j), end="")
                li = li - 1

            elif j >= 110 and j <= 122 or j >= 78 and j <= 90:
                j = j - 13
                print(chr(j), end="")
                li = li - 1

            elif j == 32:
                print(chr(j), end="")
                li = li - 1

            elif j >= 48 and j <= 57:
                print(chr(j), end="")
                li = li - 1

            elif j >= 33 and j <= 47:
                print(chr(j), end="")
                li = li - 1

            elif j >= 58 and j <= 64:
                print(chr(j), end="")
                li = li - 1

            elif j >= 91 and j <= 96:
                print(chr(j), end="")
                li = li - 1

            elif j >= 123 and j <= 126:
                print(chr(j), end="")
                li = li - 1

    q = open(r"C:\Arb\log.txt", "a")
    q.write("Successful execution of rotenc() at :" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
def rotdec():
    q = open(r"C:\Arb\log.txt", "a")
    q.write("In function rotdec at:" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
    s = ""
    s = input("Enter the encrypted string to decrypt it:")
    li = len(s)
    print(Fore.CYAN + "Decrypted message is:", end="")
    print(Style.RESET_ALL)
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if j >= 97 and j <= 109 or j >= 65 and j <= 77:
                j = j + 13
                print(chr(j), end="")
                li = li - 1

            elif j >= 110 and j <= 122 or j >= 78 and j <= 90:
                j = j - 13
                print(chr(j), end="")
                li = li - 1

            elif j == 32:
                print(chr(j), end="")
                li = li - 1

            elif j >= 48 and j <= 57:
                print(chr(j), end="")
                li = li - 1

            elif j >= 33 and j <= 47:
                print(chr(j), end="")
                li = li - 1

            elif j >= 58 and j <= 64:
                print(chr(j), end="")
                li = li - 1

            elif j >= 91 and j <= 96:
                print(chr(j), end="")
                li = li - 1

            elif j >= 123 and j <= 126:
                print(chr(j), end="")
                li = li - 1

    q = open(r"C:\Arb\log.txt", "a")
    q.write("Successful execution of rotdec() at :" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
def rot22enc():
    q = open(r"C:\Arb\log.txt", "a")
    q.write("In function rot22enc at:" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
    s = ""
    j = None
    s = input("Enter ur string here to encrypt:")
    li = len(s)
    print(Fore.CYAN + "Encrypted message is:", end="")
    print(Style.RESET_ALL)
    print("\n")
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if j >= 97 and j <= 100 or j >= 65 and j <= 68:
                j = j + 22
                print(chr(j), end="")
                li = li - 1

            elif j >= 101 and j <= 122 or j >= 69 and j <= 90:
                j = j - 4
                print(chr(j), end="")
                li = li - 1

            elif j == 32:
                print(" ", end="")
                li = li - 1

            elif j >= 48 and j <= 57:
                print(chr(j), end="")
                li = li - 1

            elif j >= 33 and j <= 47:
                print(chr(j), end="")
                li = li - 1

            elif j >= 58 and j <= 64:
                print(chr(j), end="")
                li = li - 1

            elif j >= 91 and j <= 96:
                print(chr(j), end="")
                li = li - 1

            elif j >= 123 and j <= 126:
                print(chr(j), end="")
                li = li - 1

    q = open(r"C:\Arb\log.txt", "a")
    q.write("Successful execution of rot22enc() at :" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
def rot22dec():
    q = open(r"C:\Arb\log.txt", "a")
    q.write("In function rot22dec at:" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
    s = ""
    s = input("Enter the encrypted string to decrypt it:")
    li = len(s)
    print("\n", Fore.CYAN + "Decrypted message is:", end="")
    print(Style.RESET_ALL)
    print("\n")
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if j >= 119 and j <= 122 or j >= 87 and j <= 90:
                j = j - 22
                print(chr(j), end="")
                li = li - 1

            elif j >= 97 and j <= 118 or j >= 65 and j <= 86:
                j = j + 4
                print(chr(j), end="")
                li = li - 1

            elif j == 32:
                print(" ", end="")
                li = li - 1

            elif j >= 48 and j <= 57:
                print(chr(j), end="")
                li = li - 1

            elif j >= 33 and j <= 47:
                print(chr(j), end="")
                li = li - 1

            elif j >= 58 and j <= 64:
                print(chr(j), end="")
                li = li - 1

            elif j >= 91 and j <= 96:
                print(chr(j), end="")
                li = li - 1

            elif j >= 123 and j <= 126:
                print(chr(j), end="")
                li = li - 1

    q = open(r"C:\Arb\log.txt", "a")
    q.write("Successful execution of rot22dec() at :" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
def simenc():
    q = open(r"C:\Arb\log.txt", "a")
    q.write("In function simenc at:" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
    s = ""
    s = input("Enter the string to encrypt here:")
    li = len(s)
    print(Fore.CYAN + "Encrypted message is:", end="")
    print(Style.RESET_ALL)
    print("\n")
    for i in s:
        j = ord(i)
        if j == 32:
            print(chr(j), end="")
            li = li - 1

        elif j >= 48 and j <= 57:
            print(chr(j), end="")
            li = li - 1

        elif j >= 33 and j <= 47:
            print(chr(j), end="")
            li = li - 1

        elif j >= 58 and j <= 64:
            print(chr(j), end="")
            li = li - 1

        elif j >= 91 and j <= 96:
            print(chr(j), end="")
            li = li - 1

        elif j >= 123 and j <= 126:
            print(chr(j), end="")
            li = li - 1

        else:
            j = j + 1
            print(chr(j), end="")
            li = li - 1
    q = open(r"C:\Arb\log.txt", "a")
    q.write("Successful execution of simenc() at :" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
def simdec():
    q = open(r"C:\Arb\log.txt", "a")
    q.write("In function simdec at:" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
    s = ""
    s = input("Enter the encrypted string here to decrypt it:")
    li = len(s)
    print(Fore.CYAN + "Decrypted message is:", end="")
    print(Style.RESET_ALL)
    print("\n")
    for i in s:
        j = ord(i)
        if j == 32:
            print(chr(j), end="")
            li = li - 1

        elif j >= 48 and j <= 57:
            print(chr(j), end="")
            li = li - 1

        elif j >= 33 and j <= 47:
            print(chr(j), end="")
            li = li - 1

        elif j >= 58 and j <= 64:
            print(chr(j), end="")
            li = li - 1

        elif j >= 91 and j <= 96:
            print(chr(j), end="")
            li = li - 1

        elif j >= 123 and j <= 126:
            print(chr(j), end="")
            li = li - 1

        else:
            j = j - 1
            print(chr(j), end="")
            li = li - 1
    q = open(r"C:\Arb\log.txt", "a")
    q.write("Successful execution of simdec() at :" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
def cenc():
    q = open(r"C:\Arb\log.txt", "a")
    q.write("In function cenc at:" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
    s = "abcdefghijklmnopqrstuvwxyz"
    print("Current working string is:", s)
    k = input("Input a single word key u want to use for encryption:")
    if len(k) > 1:
        print("App Crashed!Sending report to the developer!")
        g = open(r"C:\Arb\log.txt", "a")
        g.write("App crashed while executing cenc() at:" + curr)
        g.write("\n")
        mail()
        time.sleep(5)
        sys.exit(0)

    i = ord(k)
    s = s.replace(k, '')
    s = k + s
    print("Now string is:", s)
    t = input("Enter the string to Encrypt here:")
    li = len(t)
    print(Fore.CYAN + "Encrypted message is:", end="")
    print(Style.RESET_ALL)
    while li != 0:
        for n in t:
            j = ord(n)
            if j == ord('a'):
                j = i
                print(chr(j), end="")
                li = li - 1

            elif n > 'a' and n <= k:
                j = j - 1
                print(chr(j), end="")
                li = li - 1

            elif n > k:
                print(n, end="")
                li = li - 1

            elif ord(n) == 32:
                print(chr(32), end="")
                li = li - 1

            elif j >= 48 and j <= 57:
                print(chr(j), end="")
                li = li - 1

            elif j >= 33 and j <= 47:
                print(chr(j), end="")
                li = li - 1

            elif j >= 58 and j <= 64:
                print(chr(j), end="")
                li = li - 1

            elif j >= 91 and j <= 96:
                print(chr(j), end="")
                li = li - 1

            elif j >= 123 and j <= 126:
                print(chr(j), end="")
                li = li - 1

    q = open(r"C:\Arb\log.txt", "a")
    q.write("Successful execution of cenc() at :" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
def cdec():
    q = open(r"C:\Arb\log.txt", "a")
    q.write("In function cdec at:" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
    h = ""
    c = ''
    s = "abcdefghijklmonpqrstuvwxyz"
    t = input("Enter the Encrypted String to Decrypt it here:")
    k = input("Enter the key you used earlier during encryption:")
    if len(k) > 1:
        print("App Crashed!Sending report to the developer!")
        g1 = open(r"C:\Arb\log.txt", "a")
        g.write("App crashed while executing cenc() at:" + curr)
        g.write("\n")
        mail()
        time.sleep(5)
        sys.exit(0)

    s = s.replace(k, '')
    s = k + s
    i = ord(k)
    li = len(t)
    print(Fore.CYAN + "Decrypted message is:", end="")
    print(Style.RESET_ALL)
    for j in t:
        p = ord(j)
        if j > k:
            print(j, end="")

        elif j < k:
            if j == ' ':
                print(' ', end="")

            else:
                if p >= 48 and p <= 57:
                    print(chr(p), end="")
                    li = li - 1

                elif p >= 33 and p <= 47:
                    print(chr(p), end="")
                    li = li - 1

                elif p >= 58 and p <= 64:
                    print(chr(p), end="")
                    li = li - 1

                elif p >= 91 and p <= 96:
                    print(chr(p), end="")
                    li = li - 1

                elif p >= 123 and p <= 126:
                    print(chr(p), end="")
                    li = li - 1

                else:
                    j = chr(ord(j) + 1)
                    print(j, end="")

        elif j == k:
            print('a', end="")

    q = open(r"C:\Arb\log.txt", "a")
    q.write("Successful execution of cdec() at :" + curr)
    q.write(' ')
    q.write("\n")
    q.close()
def delay_print(s):
    for c in s:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.1)
os.system("cls")
auth()

if count == 1:
    # os.system(r"C:\Arb\cartoon.exe")
    choice = None
    p()
    delay_print("This Script Can Encrypt Ur Message In a Different Manner So That No Third Person Can Read It!")
    print("\n\n\n")
    choice = int(input("\nEnter 1 to start encryption and decryption process and 0 to exit the program:"))
    if choice == 0:
        delay_print("Thanks for using me!")
        mail()
        time.sleep(3)
        sys.exit(0)

    bar()

    while choice != 0:
        print("""

                   1.Atbash Encryption
                   2.Rot13
                   3.Rot22
                   4.Simple Encryption(add 1)
                   5.caesar(with ur key for only small alphabets)
                   6.Send Feedback to the Developer
                   7.Exit The program 

                                               """)

        c = 0
        ch = None
        c = int(input("Please Choose ur encryption Method from the following techniques listed above:"))
        if c == 6:
            fromaddr = "cyberbot1502@gmail.com"
            toaddr = "cyberbot1502@gmail.com"  # acmditu@gmail.com
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            sub = input("Subject of Mail:")
            bod = input("Body of the mail!:")
            msg['Subject'] = sub
            body = bod
            msg.attach(MIMEText(body, 'plain'))
            p = MIMEBase('application', 'octet-stream')
            text = msg.as_string()
            c = True
            while c:
                try:
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.ehlo()
                    s.starttls()
                    s.login(fromaddr, "Hexadecimalqwertyuiop")
                    s.sendmail(fromaddr, toaddr, text)
                    c = False
                    print("Mail Sent!")
                except Exception:
                    time.sleep(5)
                    print("No Internet please try Again!")
                    c = True

            s.quit()

        if c == 7:
            FILE_ATTRIBUTE_HIDDEN = 0x1

            # rett = ctypes.windll.kernel32.SetFileAttributesW(r'C:\log.txt',
            # FILE_ATTRIBUTE_HIDDEN)
            delay_print("Thanks for using me!")
            mail()
            sys.exit()

        if c == 1:
            while ch != 0:
                prnt()
                f = int(input("Enter ur choice what to do now:"))
                if f == 1:
                    bashenc()
                if f == 2:
                    bashdec()
                ch = int(input("\nWant to do some more encryption-decryption task on Atbash then enter 2 otherwise 0:"))

        elif c == 2:
            hc = None
            while hc != 0:
                prnt()
                f = int(input("Enter ur choice what to do now:"))
                if f == 1:
                    rotenc()
                if f == 2:
                    rotdec()

                hc = int(input("\nTo do some more task in ROT13 enter 4 otherwise 0:"))
                print("\n")

        elif c == 3:
            cc = None
            while cc != 0:
                prnt()
                f = int(input("Enter ur choice what to do now:"))
                if f == 1:
                    rot22enc()
                if f == 2:
                    rot22dec()

                cc = int(input("\nTo do more task in ROT22 enter 4 otherwise 0:"))
                print("\n")

        elif c == 4:
            g = None
            while g != 0:
                prnt()
                f = int(input("Enter ur choice what to do now:"))
                if f == 1:
                    simenc()

                if f == 2:
                    simdec()

                g = int(input("\nTo do more task in Simple method enter 5 otherwise 0:"))

        elif c == 5:
            i = None
            while i != 0:
                prnt()
                g = int(input("Enter ur choice what to do now:"))
                if g == 1:
                    cenc()
                if g == 2:
                    cdec()

                i = int(input("\nTo do more task in caesor keyed enter 6 otherwise 0:"))


else:
    print(Fore.RED + "Wrong Password!please change ur password if u forget it in next run")
    print(Style.RESET_ALL)

time.sleep(4)
