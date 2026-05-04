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
    except KeyError as e:
        print(f"Could not find Hammer: {e}")  # pollutes stdout
        return None

A()

# Output:
# Could not find Hammer: 'hammer'
# (exit 0)
