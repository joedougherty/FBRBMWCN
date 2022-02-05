FBRBMWCN
--------

Function-Based Regex Builder Module Without a Clever Name

WHAT
----

A tool to help interactively develop regexes. 


Example
=======

In the US, a phone number can be composed of:


- **area code**: three digits, possibly wrapped with parentheses
- **separator**: space(s), dash, dot, or non-existent
- **prefix**: three digits
- **separator**: space(s), dash, dot, or non-existent
- **suffix**: four digits


.. code-block:: python
    
    from rx import *

    areacode = compose(
        digit(), exactly_n_times(3),
        OR(),
        find('('), digit(), exactly_n_times(3), then(')')
    )

    print(areacode) # '\\d{3}|\\(\\d{3}\\)'

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

    rx(phone_number_pattern) == re.compile('\\d{3}|\\(\\d{3}\\)(\\s+|\\.|\\-)?\\d{3}(\\s+|\\.|\\-)?\\d{4}') # True
