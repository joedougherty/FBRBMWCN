import re   


def rx(*patterns):
    return re.compile(r''.join([p for p in patterns]))


def compose(*patterns):
    return r''.join(patterns)


def match(value):
    return f'{re.escape(value)}'


then = match


def anything_but(value):
    return f'[^{re.escape(value)}]*'


def something_but(value):
    return f'[^{re.escape(value)}]+'


def any_of(value):
    return f'[{re.escape(value)}]'


char_class = any_of


def char_range(start, end):
    return f'{start}-{end}'


def start_of_line():
    return '^'


def end_of_line():
    return '$'


def word():
    return r'\w+'


def digit():
    return r'\d'


def something():
    return '.+'


def anything():
    return '.*'


# Modifiers
# https://docs.python.org/3/howto/regex.html#matching-characters
# https://thepythonguru.com/python-regular-expression/#basic-patterns-used-in-regular-expression

def between_n_and_m_times(n, m):
    return '{' + str(n) + ',' + str(m) + '}'


def between_n_and_m_times_lazy(n, m):
    return '{' + str(n) + ',' + str(m) + '}?'


def exactly_n_times(n):
    return f'{ {n} }'


def maybe():
    return '?'


def one_or_more_times():
    return '+'


def OR():
    return r'|'


def zero_or_more_times():
    return '*'


# Some common character patterns
# https://thepythonguru.com/python-regular-expression/#basic-patterns-used-in-regular-expression

def linebreak():
    return r'(?:(?:\n)|(?:\r\n))'


def space():
    return r'\s'


def tab():
    return r'\t'


def word_boundary():
    return r'\b'


# Grouping
# https://docs.python.org/3/howto/regex.html#grouping

def group(*patterns):
    return f'({compose(*patterns)})'


def named_group(name, *patterns):
    return f'(?P<{name}>{compose(*patterns)})'


def non_capturing_group(*patterns):
    return f'(?:{compose(*patterns)})'


# Lookaheads
# https://docs.python.org/3/howto/regex.html#lookahead-assertions

def followed_by(value):
    return f'(?={re.escape(value)})'


def not_followed_by(value):
    return f'(?!{re.escape(value)})'
    

# Lookbehinds
# https://docs.python.org/3/library/re.html

def preceded_by(value):
    return f'(?<={re.escape(value)})'


def not_preceded_by(value):
    return f'(?<!{re.escape(value)})'


# Derived Patterns

def dot():
    return match('.')


def dots():
    return compose(dot(), one_or_more_times())


def spaces():
    return compose(space(), one_or_more_times())

