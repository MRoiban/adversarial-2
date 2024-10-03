from typing import Optional
from competitive_env import CompetitiveEnv, S, A
from competitive_world import CompetitiveWorld, CWorldState
from math import inf
from icecream import ic
from copy import deepcopy
import matplotlib.pyplot as plt
from lle import World, Action

DISPLAY = True

def display_world(w: World):
    if DISPLAY:
        plt.imshow(w.get_image())
        plt.axis("off")
        plt.show()

def getChildren(mdp: CompetitiveWorld, state:S):
    children: list[CompetitiveWorld] = []
    cState = CWorldState(
            value=state.value,
            current_agent=state.current_agent,
            world_state=mdp.world.get_state(),
        )
    for action in mdp.available_actions(cState):
        transitionWorld = CompetitiveWorld(mdp.world)
        transitionState = transitionWorld.step(state, action)
        transitionWorld.world.set_state(transitionState.world_state)
        children.append((action, transitionWorld))
        
    return children

def closest_exit(mdp:CompetitiveWorld, state: S):
    agent = mdp.world.agents_positions[state.current_agent]
    best_distance = +inf
    current_exit = None
    distanceA = agent[0] + agent[1]
    for ex in mdp.world.exit_pos:
        distanceE = ex[0] + ex[1]; distance = abs(distanceE - distanceA)
        if best_distance > distance:
            best_distance = distance
            current_exit = ex
    return [current_exit, best_distance]

def closest_gem(mdp:CompetitiveWorld, state: S):
    agent = mdp.world.agents_positions[state.current_agent]
    best_distance = +inf
    current_gem = None
    distanceA = agent[0] + agent[1]
    for gem in mdp.world.gems.keys():
        distanceE = gem[0] + gem[1]; distance = abs(distanceE - distanceA)
        if best_distance > distance:
            best_distance = distance
            current_gem = gem
    return [current_gem, best_distance] if current_gem != None else [(0,0), 0]
    
def is_gem(gem, agent):
    return 1 if gem == agent else 0

def is_exit(ex, agent):
    return 1 if ex == agent else 0

def minimax(mdp: CompetitiveWorld, state: S, max_depth: int, depth=None) -> Optional[A]:
    action = Action(4)
    if depth == None:
        if state.current_agent != 0:
            raise ValueError
        depth = max_depth
        
    if depth == 0 or (mdp.is_final(state) and (mdp.world.gems_collected == len(mdp.world.gems))):
        ex = closest_exit(mdp, state)
        gem = closest_gem(mdp, state)
        agent = mdp.world.agents_positions[state.current_agent]
        mdp.world.gems.items()
        return [(ex[0][0] + ex[0][1]) + 
                is_exit(ex[0], agent) - 
                ex[1] + (gem[0][0] + gem[0][1]) + 
                is_gem(gem[0], agent) - 
                gem[1], 
                action]

    if state.current_agent == 0:
        state.value = -inf
        for action, child in getChildren(mdp, state):
            state.current_agent = 1
            maxi = minimax(child, state, max_depth, depth-1)
            state.value = max(state.value, maxi[0])
            if depth < max_depth:
                return [state.value, action]
            
    else:
        state.value = +inf
        for action, child in getChildren(mdp, state):
            state.current_agent = 1
            mini = minimax(child, state, max_depth, depth-1)
            state.value = min(state.value, mini[0])
            if depth < max_depth:
                return [state.value, action]
    
    return action


def alpha_beta(mdp: CompetitiveEnv[A, S], state: S, max_depth: int) -> Optional[A]:
    return None


def expectimax(mdp: CompetitiveEnv[A, S], state: S, max_depth: int) -> Optional[A]:
    return None
