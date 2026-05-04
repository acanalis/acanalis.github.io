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
        return "I don't have a hammer :)"

def C(thing):
    if not isinstance(thing, Hammer):
        raise TypeError(f"C needs a Hammer, got {thing!r}")
    print(f"C: working with a {type(thing).__name__}")

def B():
    thing = A()  # returns the note string
    C(thing)     # TypeError: at least the message hints at what went wrong

B()

# Output:
# Traceback (most recent call last):
#   ...
# TypeError: C needs a Hammer, got "I don't have a hammer :)"
# (exit 1)
