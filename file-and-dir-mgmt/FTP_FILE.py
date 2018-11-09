import pyftp

pyftp.ftp_host(192.168.0.1,22)

pyftp.FTP.login("root","redhat@123")

#A = filename

ftp = ftplib.FTP("192.168.234.134")
ftp.login("root", "redhat")
ftp.cwd("/root/anaconda-ks.cfg")


try:
    ftp.retrbinary("RETR " + filename ,open(i, 'wb').write)
except:
    print ("Error")
