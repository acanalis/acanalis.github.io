class Hammer:
    pass

class Screwdriver:
    pass

class Nail:
    pass

screwdriver = Screwdriver()
nail = Nail()

def A():
    drawers = {"screwdriver": screwdriver, "nail": nail}
    try:
        thing = drawers["hammer"]
        return thing
    except KeyError:
        return None
    # also returns None if you just use `pass` in the except block!

def C(thing):
    if not isinstance(thing, Hammer):
        raise TypeError(f"C needs a Hammer, got {thing!r}")
    print(f"C: working with a {type(thing).__name__}")

def B():
    thing = A()  # returns None
    C(thing)     # TypeError: real error was in A, but blame lands on C

B()

# Output:
# Traceback (most recent call last):
#   ...
# TypeError: C needs a Hammer, got None
# (exit 1)
