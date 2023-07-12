#!/usr/bin/pyhton3
def remove_char_at(str, n):
    s = str[:n] + str[n+1:]
    return s
