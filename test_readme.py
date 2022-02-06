import re

from rx import (compose, dot, digit, exactly_n_times, 
                group, match, maybe, OR, rx, spaces, then)


def test_readme_example_works_as_advertised():
    area_code = compose(
        digit(), exactly_n_times(3),
        OR(),
        match('('), digit(), exactly_n_times(3), then(')')
    )

    print(area_code) # '\\d{3}|\\(\\d{3}\\)'

    separator = compose(
        spaces(), OR(), dot(), OR(), match('-')
    )

    separator_maybe = compose(group(separator), maybe())

    print(separator_maybe) # '(\\s+|\\.|\\-)?'

    prefix = compose(digit(), exactly_n_times(3))

    print(prefix) # '\\d{3}'

    suffix = compose(digit(), exactly_n_times(4))

    print(suffix) # '\\d{4}'

    phone_number_pattern = compose(
        area_code,
        separator_maybe,
        prefix,
        separator_maybe,
        suffix
    )

    assert rx(phone_number_pattern) == re.compile('\\d{3}|\\(\\d{3}\\)(\\s+|\\.|\\-)?\\d{3}(\\s+|\\.|\\-)?\\d{4}') # True
