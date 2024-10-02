from typing import Optional
from competitive_env import CompetitiveEnv, S, A
from math import inf
from icecream import ic




def minimax(mdp: CompetitiveEnv[A, S], state: S, max_depth: int) -> Optional[A]:
    """
    1. When need to check which agent is playing: min or max
    2.
    """
    if max_depth == 0 or mdp.is_final(state):
        return 1 # heuristic
    
    if state.current_agent == 0:
        state.value = -inf
        ic(mdp.available_actions(state))
        for child in mdp.available_actions(state):
            state.value = max(state.value, minimax(mdp, child, max_depth-1))
    else:
        state.value = +inf
        for child in mdp.available_actions(state):
            state.value = min(state.value, minimax(mdp, child, max_depth-1))
    
    return state.value


def alpha_beta(mdp: CompetitiveEnv[A, S], state: S, max_depth: int) -> Optional[A]:
    return None


def expectimax(mdp: CompetitiveEnv[A, S], state: S, max_depth: int) -> Optional[A]:
    return None
