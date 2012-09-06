"""
Encrypt and decrypt.
"""

from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack


MODE = Blowfish.MODE_OFB
BLOCK = Blowfish.block_size


def get_padding(source_length, block_size=BLOCK):
    bytes     	= block_size - source_length % block_size
    return pack('b' * bytes, *range(bytes))


def strip_padding(source):
	return source.rsplit(chr(0), 1)[0]


def encrypt(source, key):
    assert 4 <= len(key) <= 56
    iv                 	= Random.new().read(BLOCK)
    cipher             	= Blowfish.new(key, MODE, iv)
    source_length		= len(source)
    padding            	= get_padding(source_length)
    return iv + cipher.encrypt(source + padding)


def decrypt(source, key):
    assert 4 <= len(key) <= 56
    bs 					= BLOCK
    iv, source         	= source[:bs], source[bs:]
    cipher             	= Blowfish.new(key, MODE, iv)
    return strip_padding(cipher.decrypt(source))