import string
import random
import qrcode

if __name__ == "__main__":
    # s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # s3 = string.digits
    # s4 = string.punctuation

    # a = string.printable #extra security purpouse

    # print(a)

    s = []
    # s.extend(list(s1))
    s.extend(list(s2))
    # s.extend(list(s3))
    # s.extend(list(s4))
    # s.extend(list(a))

    random.shuffle(s)
    # print(s)
    # amount = int(input("no. of digits:- \n"))

    password = "".join(s[0:20])
    # print(password)
    main_pwd = f"{password[0:5]}-{password[5:10]}-{password[10:15]}-{password[15:20]}"
    # print(password)
    print(main_pwd)
    
    # generating qr code 
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(main_pwd)
    qr.make(fit=True)
    im = qr.make_image(fill = "black", back_color = "white")
    im.show()
