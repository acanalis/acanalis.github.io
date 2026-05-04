class Hammer:
    pass

class Screwdriver:
    pass

class Nail:
    pass

screwdriver = Screwdriver()
nail = Nail()

class HammerNotFound(Exception):
    pass

def A():
    drawers = {"screwdriver": screwdriver, "nail": nail}
    try:
        thing = drawers["hammer"]
        return thing
    except KeyError as e:
        raise HammerNotFound("Could not find hammer in any drawers.") from e

A()

# Output:
# Traceback (most recent call last):
#   ...
# KeyError: 'hammer'
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
#   ...
# HammerNotFound: Could not find hammer in any drawers.
# (exit 1)
