#!/usr/bin/env python3

import fileinput
file_name = input("> ")
print(''.join(reversed(list(fileinput.input(file_name)))))
