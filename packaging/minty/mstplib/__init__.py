import os
from ctypes import cdll

def test_api1():
    # Call the library to init the mstp_agent
    dirname=os.path.dirname(__file__)
    libmstp_path=os.path.join(dirname, "libmyextn.so")
    mstp_lib = cdll.LoadLibrary(libmstp_path)
    mstp_lib.my_api("hello World")

def test_api2():
    # Call the library to init the mstp_agent
    dirname=os.path.dirname(__file__)
    libmstp_path=os.path.join(dirname, "libmyextn.so")
    mstp_lib = cdll.LoadLibrary(libmstp_path)
    mstp_lib.my_api2("hello World")

