#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
In this exercise, you will implement an algorithm to find an approximate 
solution for the 3-CNF problem, that is, the problem of finding a satisfying 
assignment for a logical sentence of the form
(P∨Q∨¬S)∧(R∨T∨¬P)∧(R∨T∨¬S).
∨ == or
∧ == and
¬ == not

The GSAT algorithm is an instance of a class of algorithms called Local Search 
Algorithms, which explore the state space of boolean assignments to variables 
by considering a locally optimal, or greedy change to that assignment.

3-CNF formulas are in CNF form, and each clause contains exactly 3 literals. 
The GSAT algorithm starts with a random truth assignment to the symbols, and 
then tries to find a satisfying assignment by changing one truth value at
a time. The symbol to be changed is selected such that the maximum number of 
clauses is satisfied after each step. If there are multiple variables that 
satisfy the same number of clauses, the decision between them is arbitrary.

Since the trajectory of the state (the truth assignments to each variable in 
each step of the algorithm) depends heavily on the initial state, the 
algorithm is restarted several times with different initial states.

The algorithm performance is influenced by two important parameters: 
C, the number of clauses, 
N, the number of proposition symbols.
"""

# '''
"""
For this exercise, 3-CNFs are represented as a LIST of clauses, where each 
clause consists of two sets: 
- The first one contains the indices of the variables in the clause that 
  are nonnegated; 
- the second one the indices for the variables that appear negated.
The state is simply a list of boolean 
values, of length N
(P∨Q∨¬S)∧(R∨T∨¬P)∧(R∨T∨¬S).
"""

state = [False, False, True, True, False]

# variables in the order (P, Q, R, S, T)
problem = [
           ({0, 1}, {3, }), # clause 1 {index 0 and 1 are nonnegated}, {3 appears negated}
           ({2, 4}, {0, }), # clause 2
           ({2, 4}, {3, })  # clause 3
           ]

#(P∨Q∨¬S)∧(R∨T∨¬P)∧(R∨T∨¬S)
#problem is ((P==0)∨(Q==1)∨(not S==3)) and ((R==2)∨(T==4)∨(P==0)) and ((R==2)∨(T==4)∨(S==3)))

"""
Which complexity class does the problem of satifisbility of 3-CNF formulas 
belong to? Select the most concise answer. Return a string from your function.
"""
def three_cnf_complexity():
    # return 'very, very hard'
    return 'NP-Complete'

"""
How many evaluations have to be made in every step of the algorithm 
(assuming that the satisfiability of a clause can be checked in 1 step)? 
Return a sympy function in the variables N and C.
"""
'''
from sympy import var
var('N C')
def gsat_step_complexity(N, C):
    # return N + C / 2.17 
    return C
'''


"""
Is this algorithm complete? Return True or False (as bool values)
"""
def gsat_complete():
    # return None
    return False

"""
Generate random instances of 3-CNF problems, given the number of 
clauses n_clauses and the number of variables n_vars. 
Note that the representation of the positive and negative literals for 
each clause as sets does not allow clauses like P∧P∧Q. Your random problems 
should always have 3 different literals in the set representation.

(P∨Q∨¬S)∧(R∨T∨¬P)∧(R∨T∨¬S).
(P, Q, R, S, T)
"""
# '''
import random
def generate_random_problem(n_vars, n_clauses):
    # problem = None
    n_vars = n_vars -1 # because starting from 0
    problem = []    # empty list of clauses
    for x in range(n_clauses):  # loop through number of wanted clauses
        myClause = ()   # tuple containing positive and negative literals
        myIndexSet = set()
        myAppearSet = set()
        while len(myIndexSet) < 2:
            if len(myAppearSet) < 1:
                myRandomNumber = random.randint(0, n_vars)
                myAppearSet.add(myRandomNumber)

            myRandomNumber = random.randint(0, n_vars)
            if myRandomNumber not in myAppearSet:
                myIndexSet.add(myRandomNumber)

        myClause += (myIndexSet, myAppearSet)
        problem.append(myClause)
    # problem = [
    #       ({0, 1}, {3, }),    # clause 1 {index 0 and 1 are nonnegated}, {3 appears negated}
    #       ({2, 4}, {0, }),    # clause 2
    #       ({2, 4}, {3, })     # clause 3
    #       ]
    return problem
# done!
# '''
"""
Can you think of a simple way to simplify the problem in cases where clauses 
are tautological?
Write a function that simplifies the problem accordingly.
"""
testproblem=[
    ({0,1},{3,}),
    ({2,4},{2,}),
    ({0,4},{4,}),
    ({3,1},{1,}),
    ({0,1},{1,})
]

def simplify_three_cnf(problem):
    '''
    simplified_problem = None
    tautologicals = []
    for aClause in problem:
        empty = aClause[0].intersection(aClause[1])

        if empty:
            tautologicals.append(aClause)
    
    #simplified_problem = (problem - tautologicals)
    #for thing in tautologicals:
    #    problem.remove(thing)
    
    return problem
    '''

    i=0
    for x in problem:
        doubles = x[0].intersection(x[1])
        #tautologicals.append(doubles)
        
        for element in doubles:
            problem.pop(i)
        i += 1
    return problem
# done!
# simplify_three_cnf(problem=testproblem)

"""
Write a function that generates the initial state for a 3-CNF SAT problem. 
It should be truly random, so that calling it multiple times gives 
different results.
"""
import random
def get_initial_state(n_vars, n_clauses):
    '''
    possibilities = [True, False]
    myInitialState = []
    for x in range(n_vars):
        myInitialState.append(random.choice(possibilities))
    return myInitialState
    '''
    return [bool(random.randint(0, 1)) for x in range(n_vars)]

# done!

"""
Now, write a function that evaluates the truth value of a single clause, and 
returns whether it is satisfied:
(P∨Q∨¬S)∧(R∨T∨¬P)∧(R∨T∨¬S).
(P, Q, R, S, T)
"""
def eval_clause(state, clause):
    # all(a_list)# logical and
    # any(a_list)# logical or
    '''
    selectedList = []
    for element in list(clause[0]):
        selectedList.append(state[element])
    for element in list(clause[1]):
        selectedList.append(not state[element])
    
    return any(selectedList)
    '''
    return any([state[e] for e in clause[0]]+[not state[e] for e in clause[1]])
    # return (any([state[element]] for element in list(clause[0])) or any([state[element]] for element in list(clause[1])))

# done!



"""
Building on this, add a function that evaluates the truth value of a 
whole 3-CNF formula problem given the state:
"""
def eval_three_cnf(problem, state):
    # aList = []
    # for aClause in problem:
    #     aList.append(eval_clause(state=state, clause=aClause))
    # return all(aList)

    return all([eval_clause(state=state, clause=aClause) for aClause in problem])

# done!

"""
Write a function that checks if a solution, i.e. a state that satisfies all 
clauses, has been found. 
The function should return the Boolean value True if the algorithm is done, 
and False otherwise.
"""
def am_i_done(problem, state):
    return eval_three_cnf(problem=problem, state=state)
# done!


"""
Write a function that runs one chain of GSAT for a given maximum number of 
iterations max_iter. It should return the best encountered state and whether 
the algorithm succeeded in finding a satisfying assignment or not, and it 
should return as early as possible.
"""
'''
# orginal
import copy
def run_gsat_chain(problem, state, max_iter):
    stateBest = state
    wirklichBeste = 0
    wirklichStateBeste = state
    success = False
    
    for _ in xrange(max_iter):
        #stateTemp = copy.deepcopy(stateBest)
        stateTemp = [element for element in stateBest]
        thisBestIter = 0
        
        for stateI in xrange(len(state)):
            stateTemp[stateI] = not stateTemp[stateI]
            gefunden = 0
            
            for x in problem:#xrange(len(problem)):
                if eval_clause(stateTemp, x):
                    gefunden = gefunden + 1
                    success = True
                    if gefunden == len(problem):
                        return stateTemp, True
            if gefunden > beste:
                thisBestIter = gefunden
                stateBest= copy.deepcopy(stateTemp)
            
            stateTemp[stateI] = not stateTemp[stateI]
        
        if(beste>wirklichBeste):
            wirklichStateBeste = stateBest

    final_state = wirklichStateBeste
    return final_state, success
'''

import copy
def run_gsat_chain(problem, state, max_iter):
    stateBest = state
    globalBestIter = 0
    wirklichStateBeste = state
    success = False
    
    for unimportant in range(max_iter):
        stateTemp = stateBest[:]
        thisBestIter = 0
        
        for stateI in xrange(len(state)):
            stateTemp[stateI] = not stateTemp[stateI] # flip element stateI
            localFound = 0 # how much clauses are satisfied
            
            # check all clauses of the problem with the current state list
            for aClause in problem:
                if eval_clause(state=stateTemp, clause=aClause):
                    localFound += 1 # increase number of satisfied clauses
                    success = True

            # if current state list satisfied all clauses in the problem
            if localFound == len(problem):
                return stateTemp, True
            
            # if this state satisfies more than the best until now
            if localFound > thisBestIter:
                thisBestIter = localFound
                stateBest = stateTemp[:]

            stateTemp[stateI] = not stateTemp[stateI] # undo flip element
        
        if(thisBestIter > globalBestIter):
            globalBestIter = thisBestIter
            wirklichStateBeste = stateBest

    final_state = wirklichStateBeste
    return final_state, success
#'''
"""
Now, write a function that generates an initial state in n_vars variables for 
the multiple chains (at most max_n_chains of them), runs each of the chains, 
and returns success (as a Boolean variable) and a satisfying assignment 
if there was one, or else the best assignment that was found.
"""
'''
# orginal
import random
def run_gsat(problem, max_iter, n_vars, max_n_chains):
    satisfying_assignment = None
    for x in xrange(max_n_chains):
        state = get_initial_state(n_vars,None)
        (final_state, success) = run_gsat_chain(problem, state, max_iter)
        if success:
            satisfying_assignment = final_state
    
    return success, satisfying_assignment

C, N = 4, 10
run_gsat(
    problem=simplify_three_cnf(generate_random_problem(N, C)), 
    max_iter=10, 
    n_vars=N, 
    max_n_chains=10)
'''
'''
"""
Experiment! Generate random problems of different sizes by varying C and N 
for your assignment function and use the timing functions of python to check 
the runtimes of the algorithm for different problems, and determine what 
feasible values for max_iter and max_n_chains could be. Make a plot of 
typical runtimes and their statistics (np.mean and np.median can be useful here) 
versus the algorithm parameters.

Timing a function works like so:

def foo():
    pass

import timeit
timeit.timeit(foo)
"""
import timeit
def foo():
    pass

timeit.timeit(foo)
'''

if __name__ == '__main__':
    # someProblem = generate_random_problem(n_vars=5, n_clauses=3)
    # print someProblem
    # # print someProblem[0][0]

    # someState = get_initial_state(n_vars=5, n_clauses=None)
    # print someState

    # print eval_clause(state=[True, True, False, True, False], clause=({1, 2}, {3, }))

    # print eval_three_cnf(problem = [({0, 1}, {3, }),({2, 4}, {0, }),({2, 4}, {3, })], state=[True, True, False, True, False])
    # print am_i_done(problem = [({0, 1}, {3, }),({2, 4}, {0, }),({2, 4}, {3, })], state=[True, True, False, True, False])

    import time
    now = time.time()
    C, N = 4, 10
    for x in range(10000):
        run_gsat_chain(
            problem=simplify_three_cnf(generate_random_problem(n_vars=N, n_clauses=C)), 
            state=get_initial_state(N, C), 
            max_iter=100)
    print "%s" %(time.time()-now)



