import os, sys
try:
    __import__("V").Main()
except Exception as e:
    exit(str(e))