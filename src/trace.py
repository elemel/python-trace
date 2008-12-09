# Copyright (c) 2008 Mikael Lind
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from functools import wraps
from itertools import chain, imap, starmap
from sys import stderr


def trace(func):

    def repr_kwarg(key, value):
        return '%s=%s' % (key, repr(value))

    def repr_args(args, kwargs):
        return ', '.join(chain(imap(repr, args),
                               starmap(repr_kwarg, kwargs.iteritems())))

    @wraps(func)
    def wrapper(*args, **kwargs):
        call_repr = '%s(%s)' % (func.__name__, repr_args(args, kwargs))
        stderr.write('%s\n' % call_repr)
        result = func(*args, **kwargs)
        stderr.write('%s -> %s\n' % (call_repr, repr(result)))
        return result

    return wrapper
