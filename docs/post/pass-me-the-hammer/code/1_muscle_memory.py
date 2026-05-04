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
    thing = drawers["hammer"]  # raises KeyError
    return thing

def B():
    thing = A()  # KeyError propagates up
    print(f"B: got {thing}")

B()

# Output:
# Traceback (most recent call last):
#   ...
# KeyError: 'hammer'
# (exit 1)
