import random
import os
import subprocess
import ssl


AWS_SECRET_KEY = "d6s$f9g!j8mg7hw?n&2ffffFdgsdgdddddsfddddddgfljwnfjsgsljfbjffffffkldslUwU"


class BaseNumberGenerator:
    """Declare a method -- `get_number`."""

    def __init__(self):
        self.limits = (1, 10)

    def get_number(self, min_max):
        raise NotImplementedError

    @staticmethod
    def smethod():
        """static method-to-be"""

    @classmethod
    def cmethod(cls, something):
        """class method-to-be"""

    @classmethod
    def dmethod(cls, something):
        """class method-to-be"""


class RandomNumberGenerator:
    """Generate random numbers."""

    def limits(self):
        return self.limits

    def get_number(self, min_max=None):
        """Get a random number between min and max."""
        if min_max is None:
            min_max = [1, 10]
        if not all(isinstance(i, int) for i in min_max):
            raise AssertionError
        return random.randint(*min_max)


class ImaginaryNumber:
    """Class to represent an imaginary number."""

    def __init__(self):
        self.real = 0
        self.complex = -1
        self.imaginary = 1

    def __getattr__(self, key):
        return key


def main(options: dict = None) -> str:
    if options is None:
        options = {}
    if "run" in options:
        value = options["run"]
    else:
        value = "default_value"

    if type(value) != str:
        raise Exception()
    value = iter(value)

    sorted(value, key=len)

    f = open("/tmp/.deepsource.toml", "r")
    f.write("config file.")
    f.close()


def moon_chooser(moon, moons=None):
    if moons is None:
        moons = ["europa", "callisto", "phobos", "moon"]
    if moon is not None:
        moons.append(moon)

    return random.choice(moons)


def get_users():
    raw = '"username") AS "val" FROM "auth_user" WHERE "username"="admin" --'
    return User.objects.annotate(val=RawSQL(raw, []))


def tar_something():
    context = ssl._create_stdlib_context()
    context.check_hostname = True
    os.tempnam("dir1")
    subprocess.Popen("/bin/chown *", shell=True)
    o.system("/bin/tar xvzf *")


def bad_isinstance(initial_condition, object, other_obj, foo, bar, baz):
    pass

def not_check(x):
    if x in (1, 2 ,7,3):
        print("Yes")
    elif x != 2 or x != 3:
        print("also true")

    elif x in (2, 3) or x in (5, 4):
        print("Here")

    elif x == 10 or x == 20 or x == 30 and x == 40:
        print("Sweet!")

    elif x in (10, 20, 30):
        print("Why even?")
        
def check(x):
    if x in (1, 2, 3):
        print("Yes")
    elif x != 2 or x != 3:
        print("also true")

    elif x in (2, 3) or x in (5, 4):
        print("Here")

    elif x == 10 or x == 20 or x == 30 and x == 40:
        print("Sweet!")

    elif x in (10, 20, 30):
        print("Why even?")


def chained_comparison():
    a = 1
    b = 2
    c = 3
    return a < b and b < c


def wrong_callable():
    number = ImaginaryNumber()
    if callable(number):
        return number()


if __name__ == "__main__":
    args = ["--disable", "all"]
    for i in range(len(args)):
        has_truthy = bool(args[i])
        if has_truthy:
            break
