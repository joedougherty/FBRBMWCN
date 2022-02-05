from rx import *

areacode = compose(
    digit(), exactly_n_times(3),
    OR(),
    match('('), digit(), exactly_n_times(3), then(')')
)

print(areacode) # '\\d{3}|\\(\\d{3}\\)'

separator = compose(
    spaces(), OR(), dot(), OR(), match('-')
)

separator_maybe = compose(group(separator), maybe())

print(separator) # '(\\s+|\\.|\\-)?'

prefix = compose(digit(), exactly_n_times(3))

print(prefix) # '\\d{3}'

suffix = compose(digit(), exactly_n_times(4))

print(suffix) # '\\d{4}'

phone_number_pattern = compose(
    areacode,
    separator_maybe,
    prefix,
    separator_maybe,
    suffix
)

phone_number_re = rx(phone_number_pattern)
