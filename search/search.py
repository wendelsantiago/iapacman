
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state
        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state
        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take
        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
  
    startState = problem.getStartState()
    visitados = []
    fringe = util.Stack()
    fringe.push((startState, ()))

    while not fringe.isEmpty():
        noAtual = fringe.pop()
        estadoAtual = noAtual[0]
        ideiaAtual = noAtual[1]

        if problem.isGoalState(estadoAtual):
            return list(ideiaAtual)

        if not estadoAtual in visitados:
            visitados.append(estadoAtual)
            paths = problem.getSuccessors(estadoAtual)

            for path in paths:
                novaIdeia = list(ideiaAtual)
                novaIdeia.append(path[1])
                proximoNo = (path[0], tuple(novaIdeia))
                
                if not path[0] in visitados:
                    fringe.push(proximoNo)

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    startState = problem.getStartState()
    visitados = []
    fringe = util.Queue()
    fringe.push((startState, ()))

    while not fringe.isEmpty():
        noAtual = fringe.pop()
        estadoAtual = noAtual[0]
        ideiaAtual = noAtual[1]

        if problem.isGoalState(estadoAtual):
            return list(ideiaAtual)

        if not estadoAtual in visitados:
            visitados.append(estadoAtual)
            paths = problem.getSuccessors(estadoAtual)

            for path in paths:
                novaIdeia = list(ideiaAtual)
                novaIdeia.append(path[1])
                proximoNo = (path[0], tuple(novaIdeia))

                if not path[0] in visitados:
                    fringe.push(proximoNo)

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    startState = problem.getStartState()
    visitados = []
    fringe = util.PriorityQueue()
    fringe.push((startState, ()), 0)

    while not fringe.isEmpty():
        noAtual = fringe.pop()
        estadoAtual = noAtual[0]
        ideiaAtual = noAtual[1]

        if problem.isGoalState(estadoAtual):
            return list(ideiaAtual)

        if not estadoAtual in visitados:
            visitados.append(estadoAtual)
            paths = problem.getSuccessors(estadoAtual)

            for path in paths:
                novaIdeia = list(ideiaAtual)
                novaIdeia.append(path[1])
                proximoNo = (path[0], tuple(novaIdeia))
                cost = problem.getCostOfActions(novaIdeia)

                if not path[0] in visitados:
                    fringe.push(proximoNo, cost)

    util.raiseNotDefined()




def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    startState = problem.getStartState()
    visitados = []
    fringe = util.PriorityQueue()
    fringe.push((startState, ()), 0)

    while not fringe.isEmpty():
        noAtual = fringe.pop()
        estadoAtual = noAtual[0]
        ideiaAtual = noAtual[1]

        if problem.isGoalState(estadoAtual):
            return list(ideiaAtual)

        if not estadoAtual in visitados:
            visitados.append(estadoAtual)
            paths = problem.getSuccessors(estadoAtual)
            
            for path in paths:
                novaIdeia = list(ideiaAtual)
                novaIdeia.append(path[1])
                proximoNo = (path[0], tuple(novaIdeia))
                cost = problem.getCostOfActions(novaIdeia) + heuristic(path[0], problem)

                if not path[0] in visitados:
                    fringe.push(proximoNo, cost)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
