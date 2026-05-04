import sys

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
        sys.exit(1)  # crashes silently, no traceback, no stack trace

A()

# Output:
# (no output, exit 1)
