import struct
import binascii

values = (1, 'ab', 2.7)
s = struct.Struct('I 2s f')

pack_data = s.pack(*values)

print(binascii.hexlify(pack_data))