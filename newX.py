#C:\Users\User\PycharmProjects\XqazWERTY\newX.py
from xxqazWERTY import x
import xdrlib

db = {}
x0 = x()
x1 = x()
x2 = x()
x3 = x()
x4 = x()
x5 = x()
x6 = x()
x7 = x()
x8 = x()
x9 = x()
p = xdrlib.Packer()
while True:
    print('What do you want to do with the data?')
    print('[1] Encode')
    print('[2] Encode and Decode')
    print('[3] Decode')
    print('[4] View Database')
    print('[5] Get Data from Database')
    print('[6] Save Database')
    print('[7] Break')
    Inp = input('input$ ')
    if Inp == '1':
        #pack_uint is the only one available by default. You can change this by removing the comment sign
        p.pack_uint(69)
        #p.pack_string()
        #p.pack_bytes()
        #p.pack_float()
        #p.pack_double()
        data0 = p.get_buffer()
        i = 1
        while i < 2:
            x = x0
            i +=1
        db[x] = data0
        print("Showing the Encoded State: {'%s': %s}" % (x, db[x]))

    if Inp == '2':
        # pack_uint is the only one available by default. You can change this by removing the comment sign
        p.pack_uint(69)
        # p.pack_string()
        # p.pack_bytes()
        # p.pack_float()
        # p.pack_double()
        data1 = p.get_buffer()
        i = 1
        while i < 2:
            x = x1
            i += 1
        db[x] = data1
        print("Showing the Encoded State: {'%s': %s}" % (x, db[x]))

        # unpack_uint is the only one available by default. You can change this by removing the comment sign
        u = xdrlib.Unpacker(data1)
        print('Showing the Decoded State:')
        print(u.unpack_uint())
        # print(u.unpack_string())
        # print(u.unpack_bytes())
        # print(u.unpack_float())
        # print(u.unpack_double())

    if Inp == '3':
        data2 = b'\x00\x00\x00E\x00\x00\x00E\x00\x00\x00E\x00\x00\x00E\x00\x00\x00E\x00\x00\x00E\x00\x00\x00E\x00\x00\x00E\x00\x00\x00E\x00\x00\x00E\x00\x00\x00E\x00\x00\x00E\x00\x00\x00E' #Encoded data goes here
        i = 1
        while i < 2:
            x = x2
            i += 1
        db[x] = data2
        u2 = xdrlib.Unpacker(data2)
        print("Showing the Encoded State: {'%s': %s}" % (x, db[x]))
        print('Showing the Decoded State:')
        # unpack_uint is the only one available by default. You can change this by removing the comment sign
        print(u2.unpack_uint())
        # print(u2.unpack_string())
        # print(u2.unpack_bytes())
        # print(u2.unpack_float())
        # print(u2.unpack_double())

    if Inp == '4':
        print(db)

    if Inp == '5':
        x = input('Enter key$ ')
        if x in db:
            print("Data: {'%s': %s}" % (x, db[x]))

        elif not x in db:
            print('ERROR 404 - ERR_KEY_NOT_FOUND')

    if Inp == '6':
        file_name = 'db.txt'
        file_mod = 'a+'
        save = open(file_name, file_mod)
        save.write(str(db, 'utf-8'))

    if Inp == '7':
        print('Are you sure you want to quit? Y/N')
        print('This will erase the database, we recommend that you save the databse before exiting. Forget this if you have done this already.')
        confirm = input('input$ ')
        if confirm == 'Y':
            break

        elif confirm == 'N':
            #continue loop
            print('Continuing Loop...')

        elif confirm == 'y':
            break

        elif confirm == 'n':
            #continue loop
            print('Continuing Loop...')
