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

def get_hammer_from_store():
    return Hammer()  # fallback

def C(thing):
    print(f"C: working with a {type(thing).__name__}")

def B():
    thing = A()
    if not isinstance(thing, Hammer):  # B covers for A's failure
        thing = get_hammer_from_store()
    C(thing)

B()

# Output:
# C: working with a Hammer
# (exit 0)
