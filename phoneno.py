#!/usr/bin/python3
import os
import binascii


def main():
    f=open("/dev/random",'rb') # /dev/randomを開く
    while(1):
        randomdata=f.read(1) # 1バイトの完全乱数の読み出し
        randomhex=binascii.hexlify(randomdata) #１６進の文字列に変換
        randomint=int(randomhex,16) # 整数に変換
        i='0123456789 '
        n=randomint/256*len(i)
        print(i[n],end='')
    f.close() # /dev/randomを閉じる
    return

if __name__=='__main__':
	main()
	exit(0)

