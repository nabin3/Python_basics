#! python3
# zigzag.py print zig-zag pattern on stdout for infinite time until it's not stopped with <ctrl -c>

import time, sys
indent = 0
indent_increasing = True

try:
    while True:
        print(' ' * indent, end='') 
        print('*' * 8)
        time.sleep(0.1)

        if indent_increasing:
            indent += 1
            if indent == 20:
                indent_increasing = False

        if not indent_increasing:
            indent -= 1
            if indent == 0:
                indent_increasing = True

except KeyboardInterrupt:
    sys.exit(0)

