# https://www.codewars.com/kata/format-a-string-of-names-like-bart-lisa-and-maggie/train/python

# My second solution, better
def namelist(names):
    names = [e['name'] for e in names]
    d = {
            0: '',
            1: '{}',
            2: '{} & {}',
            3: '{}, {} & {}',
            4: ', {}, {} & {}',
         }
    return ', '.join(names[:-3]) + d[min(4,len(names))].format(*names[-3:])

# My first solution
def namelist(names):
    names = [e['name'] for e in names]
    s = ''
    s += ', '.join(names[:-2])
    if len(names) > 2:
        s += ', '
    s += ' & '.join(names[-2:])
    return s