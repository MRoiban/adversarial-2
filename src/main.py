from lle import World
from competitive_world import CompetitiveWorld
import random
import adversarial_search


def main():
    """Vous pouvez tester et débugger votre programme ici"""
    world = CompetitiveWorld(World("S0 X"))
    state = world.reset()
    adversarial_search.minimax(world, state, 1)


if __name__ == "__main__":
    main()
