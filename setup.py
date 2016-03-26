try:
    from setuptools import setup
    assert setup
except ImportError:
    from distutils.core import setup

setup(
    name="FlatVault",
    version="0.2",
    provides=["flatvault"],
    author="Daniel Nephin",
    author_email="dnephin@gmail.com",
    url="http://github.com/dnephin/FlatVault",
    description='Encrypt flat files.',
    packages=['flatvault'],
    install_requires=['pycrypto'],
    entry_points={
        "console_scripts": ["flatvaultedit= flatvault.main:main"]
    },
)
