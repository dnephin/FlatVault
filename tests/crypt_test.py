import random
import string

from flatvault import crypt


def pytest_funcarg__key(request):
	key_length = random.randint(4, 56)
	return ''.join(random.choice(string.letters) for _ in xrange(key_length))


def test_encrypt_decrypt_small(key):
    message = "This is the message to encrypt"
    out = crypt.encrypt(message, key)
    assert message == crypt.decrypt(out, key)


def test_encrypt_decrypt_large(key):
    message = """Output FeedBack (OFB). This mode is very similar to CBC, but 
    it transforms the underlying block cipher into a stream cipher. The 
    keystream is the iterated block encryption of an Initialization Vector (IV).

    The IV is a data block to be transmitted to the receiver. The IV can be 
    made public, but it should be picked randomly.

    Reusing the same IV for encryptions done with the same key lead to 
    catastrophic cryptograhic failures."""
    out = crypt.encrypt(message, key)
    assert message == crypt.decrypt(out, key)


def test_encrypt_decrypt_zero_bytes(key):
	message = ''.join(chr(int(c)) for c in '0' * crypt.BLOCK)
	out = crypt.encrypt(message, key)
	assert message == crypt.decrypt(out, key)
