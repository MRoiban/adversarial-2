from lle import World, Action
from competitive_world import CompetitiveWorld

import random
import adversarial_search


def main():
    """Vous pouvez tester et débugger votre programme ici"""
    world = CompetitiveWorld(
        World(
            """
        .  L1W
        S0 S1
        X  X
        """
        )
    )
    # state = world.reset()
    # transitionState = world.step(state, Action(1))
    # world.world.set_state(transitionState.world_state)
    print(adversarial_search.minimax(world, world.reset(),4))


if __name__ == "__main__":
    main()
