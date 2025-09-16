# hello.py
# run this with python to print a short message

import sys
IN_COLAB = 'google.colab' in sys.modules

if IN_COLAB:
    print("You need to run this on your own computer.")
    sys.exit(1)

print("Hello! You are running Python {} on platform '{}'.".format(
    sys.version, sys.platform))
