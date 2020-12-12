import base64, zlib, re

ban = """
   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
   ||                                                  ||
   ||    Title:  Miladworkshop.ir - Decoder            ||
   ||    Version: 1.0(Encoder v4.0)                    ||
   ||    Auther: Unk9vvner, BiskooitPedar              ||
   ||    Telegram Id: @Unk9vvner,@Doctor_mosadegh      ||
   ||                                                  ||
   ||    D3D S3C: @D3DS3C_Team                         ||
   ||    Biskooit Pedar: @BiskooitPedar                ||
   ||                                                  ||
   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n\n"""
   
def decode():
    fl = input("\033[93m[?] Please enter the path of encoded file: \033[97m")
    with open(fl,'r') as ofl:
        ofl = ofl.read()
        ifl = ofl
        for i in range(3):
            ifl = base64.b64decode(re.search(r'\("[^\?].+?(?="\))',ifl.replace('\n','')).group()[2:]).decode()
        ifl = base64.b64decode([x for x in re.finditer(r'\(\"[^\?].+?(?=\"\))',ifl)][1].group()[2:]).decode()
        ifl = base64.b64decode([x for x in re.finditer(r'\(\"[^\?].+?(?=\"\))',ifl)][-1].group()[2:]).decode()
        print("\033[96m[+] Decoded:\033[97m\n")
        print(zlib.decompress(base64.b64decode([x for x in re.finditer(r'\(\"[^\?].+?(?=\"\))',ifl)][-1].group()[2:]), -zlib.MAX_WBITS).decode()+'\n')

if(len(__import__("sys").argv) > 1):
    decode()
else:
    for x in ban:
        print('\033[96m' + x, end='', flush=True)
        __import__('time').sleep(0.002)
    decode()
