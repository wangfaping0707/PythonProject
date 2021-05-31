try:
    1 / 0
except ZeroDivisionError:
    raise ValueError from None
