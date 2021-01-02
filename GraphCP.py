#Import the necessary libraries
from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod
#Declares a type variable V as variable type and D as domain type
V = TypeVar('V') # variable type
D = TypeVar('D') # domain type
#This is a Base class for all constraints
class Constraint(Generic[V, D], ABC):
    # The variables that the constraint is between
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    # This is an abstract method which must be overridden by subclasses
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...
# A constraint satisfaction problem consists of variables of type V
# that have ranges of values known as domains of type D and constraints
# that determine whether a particular variable's domain selection is valid
class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        # variables to be constrained
        #TODO: Assign variables parameter to self.variables
        self.variables: List[V] = variables 
        # domain of each variable
        #TODO: Assign domains parameter to self.domains
        self.domains: Dict[V, List[D]] = domains
        #TODO: Assign an empty dictionary to self.constraints
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        #TODO:Iterate over self.variables
        for variable in self.variables:
            self.constraints[variable] = []
            #TODO:If the variable is not in domains, then raise a LookupError("Every variable should have a domain assigned to it.")
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")
    
    #This method add constraint to variables as per their domains 
    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    # Check if the value assignment is consistent by checking all constraints
    # for the given variable against it
    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        #TODO: Iterate over self.constraints[variable]
        for constraint in self.constraints[variable]:
            #TODO: if constraint not satisfied then return False
            if not constraint.satisfied(assignment):
                return False
        #TODO: otherwise return True
        return True
    
    #This method is performing the backtracking search to find the result
    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # assignment is complete if every variable is assigned (our base case)
        if len(assignment) == len(self.variables):
            return assignment

        # get all variables in the CSP but not in the assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]

        # get the every possible domain value of the first unassigned variable
        first: V = unassigned[0]
        #TODO: Iterate over self.domains[first]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            #TODO: Assign the value
            local_assignment[first] = value
            # if we're still consistent, we recurse (continue)
            if self.consistent(first, local_assignment):
                #TODO: recursively call the self.backtracking_search method based on the local_assignment
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                # if we didn't find the result, we will end up backtracking
                if result is not None:
                    return result
        return None
#MapColoringConstraint is a subclass of Constraint class 
class MapColoringConstraint(Constraint[str, str]):
    def __init__(self, place1: str, place2: str) -> None:
        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2
    #Define the abstract method satisfied in subclass
    def satisfied(self, assignment: Dict[str, str]) -> bool:
        # If either place is not in the assignment then it is not
        # yet possible for their colors to be conflicting
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        # check the color assigned to place1 is not the same as the
        # color assigned to place2
        return assignment[self.place1] != assignment[self.place2]

#Main starts
if __name__ == "__main__":
    #Initializes the variables as per the regions of the graph
    variables: List[str] = ["BOX_1", "BOX_2", "BOX_4",
                            "BOX_3", "BOX_5", "BOX_6", "BOX_7"]
    #TODO: Initialize the domain as empty dictionary 
    domains: Dict[str, List[str]] = {}
    for variable in variables:
        #Initialize the domain of each variable
        domains[variable] = ["red", "green", "blue"]
    #Instantiate the object of CSP
    csp: CSP[str, str] = CSP(variables, domains)
    #Add constraints to the given MAP problem
    csp.add_constraint(MapColoringConstraint("BOX_1", "BOX_2"))
    csp.add_constraint(MapColoringConstraint("BOX_1", "BOX_4"))
    csp.add_constraint(MapColoringConstraint("BOX_4", "BOX_2"))
    csp.add_constraint(MapColoringConstraint("BOX_3", "BOX_2"))
    csp.add_constraint(MapColoringConstraint("BOX_3", "BOX_4"))
    csp.add_constraint(MapColoringConstraint("BOX_3", "BOX_5"))
    csp.add_constraint(MapColoringConstraint("BOX_5", "BOX_4"))
    csp.add_constraint(MapColoringConstraint("BOX_6", "BOX_4"))
    csp.add_constraint(MapColoringConstraint("BOX_6", "BOX_5"))
    csp.add_constraint(MapColoringConstraint("BOX_6", "BOX_7"))
    #Finding the solution to the problem by calling the backtracking_search() method
    solution: Optional[Dict[str, str]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)
