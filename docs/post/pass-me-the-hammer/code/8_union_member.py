import logging
import sys

class Hammer:
    pass

class Screwdriver:
    pass

class Nail:
    pass

screwdriver = Screwdriver()
nail = Nail()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR, stream=sys.stdout)

def A():
    drawers = {"screwdriver": screwdriver, "nail": nail}
    try:
        thing = drawers["hammer"]
        return thing
    except KeyError as e:
        logger.error(f"Could not find Hammer: {e}")
        return None

A()

# Output:
# ERROR:__main__:Could not find Hammer: 'hammer'
# (exit 0)
