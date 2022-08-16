def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(2000)
fib(0)
print(fib)
print(fib(0))


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# ask_ok('정말 끝내길 원하세요?')
# ask_ok('정말 끝내길 원하세요?', 2)
# ask_ok('정말 끝내길 원하세요?', 2, '자, 예나 아니요로만 답하세요!')

i = 5

def f(arg=i):
    print(arg)


i = 6
f()  # 5


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# Output:
# It's very runny, sir.
# It's really very, VERY runny, sir.
# ----------------------------------------
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch

def standard_arg(arg):
    print(arg)


def post_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(post_only, /, standard, *, kwd_only):
    print(post_only, standard, kwd_only)


standard_arg(2)

standard_arg(arg=2)

post_only_arg(1)

try:
    # TypeError: post_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
    post_only_arg(arg=1)
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")

try:
    # TypeError('kwd_only_arg() takes 0 positional arguments but 1 was given'), type(err)=<class 'TypeError'>
    kwd_only_arg(3)
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")

kwd_only_arg(arg=3)

try:
    # TypeError('combined_example() takes 2 positional arguments but 3 were given'), type(err)=<class 'TypeError'>
    combined_example(1, 2, 3)
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")

combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)

try:
    # TypeError("combined_example() got an unexpected keyword argument 'pos_only'"), type(err)=<class 'TypeError'>
    combined_example(pos_only=1, standard=2, kwd_only=3)
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")

print(list(range(3, 6)))
args = [3, 6]

print(list(range(*args)))


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
print(f(1))


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations: ", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


f('spam')
