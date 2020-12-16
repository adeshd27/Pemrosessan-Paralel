def node1():
    import paramiko
    import sys
    import time
    from getpass import getpass
    Covid77 = getpass()

    while(True):
        tunnel = paramiko.SSHClient()
        tunnel.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        tunnel.connect("192.168.43.149", 22, "rafii", Covid77)
        stdin, stdout, stderr = tunnel.exec_command("python3 hitung.py \n")
        p = tunnel.get_transport().open_session()
        p.invoke_shell()

        print("\nNode 1 192.168.43.149 rafii")
        print("Node 2 192.168.43.88 Tidak Terhubung")

        menu =str(input("1 = Lingkaran\n2 = Persegi\n3 = Segitiga\n4 = Keluar\nPilih Bangun Yang Akan di Proses : "))
        if(menu=="1"):
            r = str(input("Masukkan Nilai Jari-jari : "))
            p.send("python3 hitung.py \n")
            p.send(menu+"\n")
            p.send(r+"\n")
            time.sleep(1)
            output = p.recv(65535)
            print(output.decode("ascii"))
        elif(menu=="2"):
            s = str(input("Masukkan Nilai Sisi : "))
            p.send("python3 hitung.py \n")
            p.send(menu+"\n")
            p.send(s+"\n")
            time.sleep(1)
            output = p.recv(65535)
            print(output.decode("ascii"))
        elif(menu=="3"):
            a = str(input("Masukkan Nilai Alas : "))
            b = str(input("Masukkan Sisi B : "))
            c = str(input("Masukkan Sisi C : "))
            t = str(input("Masukkan Nilai Tinggi : "))
            p.send("python3 hitung.py \n")
            p.send(menu+"\n")
            p.send(a+"\n")
            p.send(b+"\n")
            p.send(c+"\n")
            p.send(t+"\n")
            time.sleep(1)
            output = p.recv(65535)
            print(output.decode("ascii"))
        else:
            print("Program Selesai.")
            
        pilihan = input("Apakah Masih Ingin Melanjutkan Program ?[y/n]")
        if(pilihan=="y"):
            print("Silahkan Pilih Kembali Node")
            menunode()
        elif(pilihan=="n"):
            print("program selesai")
            break
            
        line = stdout.readlines()
        line1 = stderr.readlines()
        for i in line:
            print(i)
        for i in line1:
            print(i)
    tunnel.close()
  

def node2():
    import paramiko
    import sys
    import time
    from getpass import getpass
    Lingga123 = getpass()

    while(True):
        tunnel = paramiko.SSHClient()
        tunnel.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        tunnel.connect("192.168.43.88", 22, "rafii", Lingga123)
        stdin, stdout, stderr = tunnel.exec_command("python3 hitung.py \n")
        p = tunnel.get_transport().open_session()
        p.invoke_shell()

        print("\nNode 1 192.168.43.149 Tidak Terhubung")
        print("Node 2 192.168.43.88 yuda")

        menu =str(input("1 = Lingkaran\n2 = Persegi\n3 = Segitiga\n4 = Keluar\nPilih Bangun Yang Akan di Proses : "))
        if(menu=="1"):
            r = str(input("Masukkan Nilai Jari-jari : "))
            p.send("python3 hitung.py \n")
            p.send(menu+"\n")
            p.send(r+"\n")
            time.sleep(1)
            output = p.recv(65535)
            print(output.decode("ascii"))
        elif(menu=="2"):
            s = str(input("Masukkan Nilai Sisi : "))
            p.send("python3 hitung.py \n")
            p.send(menu+ "\n")
            p.send(s+"\n")
            time.sleep(1)
            output = p.recv(65535)
            print(output.decode("ascii"))
        elif(menu=="3"):
            a = str(input("Masukkan Nilai Alas : "))
            b = str(input("Masukkan Nilai Sisi B : "))
            c = str(input("Masukkan Nilai Sisi C : "))
            t = str(input("Masukkan Nilai Tinggi : "))
            p.send("python3 hitung.py \n")
            p.send(menu +"\n")
            p.send(a+"\n")
            p.send(b+"\n")
            p.send(c+"\n")
            p.send(t+"\n")
            time.sleep(1)
            output = p.recv(65535)
            print(output.decode("ascii"))
        else:
            print("Program Selesai.")
                    
        pilihan = input("Apakah Masih Ingin Melanjutkan Program ?[y/n]")
        if(pilihan=="y"):
            print("Silahkan Pilih Kembali Node")
            menunode()
        elif(pilihan=="n"):
            print("Terima Kasih")
            break
            
        line = stdout.readlines()
        line1 = stderr.readlines()
        for i in line:
            print(i)
        for i in line1:
            print(i)
    tunnel.close()

def bareng():
    import paramiko
    import sys
    import time
    import socket
    from getpass import getpass
    Covid77 = getpass()
    Lingga123 = getpass()

    tunnel = paramiko.SSHClient()
    tunnel.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        tunnel.connect("192.168.43.149", 22, "rafii", Covid77)
        print("\nNode 1 192.168.43.149 Rafii")
        pin1=1
    except (socket.gaierror, socket.timeout):
        print("\nNode 1 192.168.43.149 Tidak Terhubung")
        pin1=0

    tunnel1 = paramiko.SSHClient()
    tunnel1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        tunnel1.connect("192.168.43.88", 22, "rafii", Lingga123)
        print("Node 2 192.168.43.88 Yuda")
        pin2=1
    except (socket.gaierror, socket.timeout):
        print("Node 2 192.168.43.88 Tidak Terhubung")
        pin2=0

    while(pin1==1 and pin2==1):
        while(True):
            stdin, stdout, stderr = tunnel.exec_command("python3 hitung.py \n")
            p = tunnel.get_transport().open_session()
            p.invoke_shell()

            stdin, stdout, stderr = tunnel1.exec_command("python3 hitung.py \n")
            o = tunnel1.get_transport().open_session()
            o.invoke_shell()
            menu =str(input("1 = Lingkaran\n2 = Persegi\n3 = Segitiga\n4 = Keluar\nPilih Bangun Yang Akan di Proses : "))
            if(menu=="1"):
                r = str(input("Masukkan Nilai Jari-jari : "))
                p.send("python3 hitung.py \n")
                p.send(menu+"\n")
                p.send(r+"\n")
                time.sleep(1)
                output = p.recv(65535)
                print("Node 1 192.168.43.149")
                print(output.decode("ascii"))

                print("--------------------------------------------")

                o.send("python3 hitung.py \n")
                o.send(menu+"\n")
                o.send(r+"\n")
                time.sleep(1)
                output = o.recv(65535)
                print("Node 2 192.168.43.88")
                print(output.decode("ascii"))
            elif(menu=="2"):
                s = str(input("Masukkan Nilai Sisi : "))
                p.send("python3 hitung.py \n")
                p.send(menu+ "\n")
                p.send(s+"\n")
                time.sleep(1)
                output = p.recv(65535)
                print("Node 1 192.168.43.149")
                print(output.decode("ascii"))

                print("--------------------------------------------")

                o.send("python3 hitung.py \n")
                o.send(menu+ "\n")
                o.send(s+"\n")
                time.sleep(1)
                output = o.recv(65535)
                print("Node 2 192.168.43.88")
                print(output.decode("ascii"))
            elif(menu=="3"):
                a = str(input("Masukkan Nilai Alas : "))
                b = str(input("Masukkan Nilai Sisi B : "))
                c = str(input("Masukkan Nilai Sisi C : "))
                t = str(input("Masukkan Nilai Tinggi : "))
                p.send("python3 hitung.py \n")
                p.send(menu +"\n")
                p.send(a+"\n")
                p.send(b+"\n")
                p.send(c+"\n")
                p.send(t+"\n")
                time.sleep(1)
                output = p.recv(65535)
                print("Node 1 192.168.43.149")
                print(output.decode("ascii"))

                print("--------------------------------------------")

                o.send("python3 hitung.py \n")
                o.send(menu +"\n")
                o.send(a+"\n")
                o.send(b+"\n")
                o.send(c+"\n")
                o.send(t+"\n")
                time.sleep(1)
                output = o.recv(65535)
                print("Node 2 192.168.43.88")
                print(output.decode("ascii"))
            else:
                print("Program Selesai.")
                menunode()

        tunnel.close()
        tunnel1.close()            

def menunode():
    print("\nNode 1 192.168.43.149 Tidak Terhubung")
    print("Node 2 192.168.43.88 Tidak Terhubung")
    print("Keluar = Q")
  
    pilih = input("Pilih Node Yang Ingin Menjalankan Program = ")
    if(pilih=="1"):
        node1()
    elif(pilih=="2"):
        node2()
    elif(pilih=="1,2"):
        bareng()
    elif(pilih=="q"or"Q"):
        print("terima kasih")
    else:
        print("Pilihan Tidak Ada.Silahkan Pilih Lagi")
        menunode()
menunode()