'''This script implements a Bayesian network for the Monty Hall problem.
   See http://staff.utia.cas.cz/vomlel/mh-puzzle.html for a description'''

import numpy as np
from pomegranate import *

# The guests initial door selection is completely random
guest = DiscreteDistribution( { 'A': 1./3, 'B': 1./3, 'C': 1./3 } )

# The door the prize is behind is also completely random
prize = DiscreteDistribution( { 'A': 1./3, 'B': 1./3, 'C': 1./3 } )

    # Monty is dependent on both the guest and the prize. 
monty = ConditionalProbabilityTable(
            [[ 'A', 'A', 'A', 0.0 ],
             [ 'A', 'A', 'B', 0.5 ],
             [ 'A', 'A', 'C', 0.5 ],
             [ 'A', 'B', 'A', 0.0 ],
             [ 'A', 'B', 'B', 0.0 ],
             [ 'A', 'B', 'C', 1.0 ],
             [ 'A', 'C', 'A', 0.0 ],
             [ 'A', 'C', 'B', 1.0 ],
             [ 'A', 'C', 'C', 0.0 ],
             [ 'B', 'A', 'A', 0.0 ],
             [ 'B', 'A', 'B', 0.0 ],
             [ 'B', 'A', 'C', 1.0 ],
             [ 'B', 'B', 'A', 0.5 ],
             [ 'B', 'B', 'B', 0.0 ],
             [ 'B', 'B', 'C', 0.5 ],
             [ 'B', 'C', 'A', 1.0 ],
             [ 'B', 'C', 'B', 0.0 ],
             [ 'B', 'C', 'C', 0.0 ],
             [ 'C', 'A', 'A', 0.0 ],
             [ 'C', 'A', 'B', 1.0 ],
             [ 'C', 'A', 'C', 0.0 ],
             [ 'C', 'B', 'A', 1.0 ],
             [ 'C', 'B', 'B', 0.0 ],
             [ 'C', 'B', 'C', 0.0 ],
             [ 'C', 'C', 'A', 0.5 ],
             [ 'C', 'C', 'B', 0.5 ],
             [ 'C', 'C', 'C', 0.0 ]], [guest, prize] )  

# State objects hold both the distribution, and a high level name.
s1 = State( guest, name="guest" )
s2 = State( prize, name="prize" )
s3 = State( monty, name="monty" )

# Create the Bayesian network object with a useful name
network = BayesianNetwork( "Monty Hall Problem" )

# Add the three nodes to the network 
network.add_nodes( [ s1, s2, s3 ] )

# Add transitions which represent conditional dependencies, where the second node is conditionally dependent on the first node (Monty is dependent on both guest and prize)
network.add_edge( s1, s3 )
network.add_edge( s2, s3 )
network.bake()

observations = { 'guest' : 'A' }

# beliefs will be an array of posterior distributions or clamped values for each state, indexed corresponding to the order
# in self.states. 
beliefs = network.forward_backward( observations )

# Convert the beliefs into a more readable format
beliefs = map( str, beliefs )

# Print out the state name and belief for each state on individual lines
print "\n".join( "{}\t{}".format( state.name, belief ) for state, belief in zip( network.states, beliefs ) )

observations = { 'guest' : 'A', 'monty' : 'B' }
beliefs = map( str, network.forward_backward( observations ) )
print "\n".join( "{}\t{}".format( state.name, belief ) for state, belief in zip( network.states, beliefs ) )
