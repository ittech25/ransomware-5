def change(filename, cryptoFn, block_size = 16):
    with open(filename, 'r+b') as _file:
        raw_Value = _file.read(block_size)
        while raw_Value:
            cipher_value = cryptoFn(raw_Value)
            #compara tamanho do bloco cifrado e plano
            if len(raw_Value) != len(cipher_value):
                raise ValueError('O valor cifrado tem tamanho diferente plano')

            _file.seek(-len(raw_Value), 1)
            _file.write(cipher_value)
            raw_Value = _file.read(block_size)
