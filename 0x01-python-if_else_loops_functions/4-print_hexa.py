#!/usr/bin/python3
for i in range(0, 99):
    if (i % 16) >= 10 and (i % 16) < 16:
        print("{} = 0x{}{}".format(i, (i // 16), chr(87 + (i % 16))))
    else:
        print("{} = 0x{}{}".format(i, (i // 16), (i % 16)))
