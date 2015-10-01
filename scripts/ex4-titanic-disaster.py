# Naive Bayes classifier as a Bayesian network

import numpy as np
from pomegranate import *

# Passengers on the Titanic either survive or perish
passenger = DiscreteDistribution( { 'w': 0.5, 'nw': 0.5 } )

gender = ConditionalProbabilityTable(
		[[ 'w','w',1],
		 ['nw','w',0],
     ['w','nw',0],
     ['nw','nw',1]],[hardware])


# Gender, given survival data
# gender = ConditionalProbabilityTable([[ 'survive', 'male',   0.1 ],
#              [ 'survive', 'female', 0.9 ],
#              [ 'perish', 'male',    0.1 ],
# 	         [ 'perish', 'female',  0.9]], [passenger] )
#

# Class of travel, given survival data
# tclass = ConditionalProbabilityTable(
#              [[ 'survive', 'first',  0.3 ],
#              [ 'survive', 'second', 0.3 ],
#              [ 'survive', 'third',  0.6 ],
#              [ 'perish', 'first',  0.4 ],
#              [ 'perish', 'second', 0.3 ],
# 	         [ 'perish', 'third',  0.3]], [passenger] )


# State objects hold both the distribution, and a high level name.
s1 = State( passenger, name = "passenger" )
s2 = State( gender, name = "gender" )

# Create the Bayesian network object with a useful name
network = BayesianNetwork( "Titanic Disaster" )

# Add the three nodes to the network
network.add_nodes( [ s1, s2 ] )

# Add transitions which represent conditional depesndencies, where the second
# node is conditionally dependent on the first node (Monty is dependent on both guest and prize)
network.add_edge( s1, s2 )
network.add_edge( s1, s3 )
network.bake()

# The first observation is that the interpreter is not working
#first_observation = { 'interpreter' : 'nw' }

# beliefs will be an array of posterior distributions or clamped values for each state, indexed corresponding to the order
# in self.states.
#beliefs = network.forward_backward( first_observation )

# Convert the beliefs into a more readable format
#beliefs = map( str, beliefs )

# Print out the state name and belief for each state on individual lines
# What is the probability of the code being buggy ?
#print "\n".join( "{}\t{}".format( state.name, belief ) for state, belief in zip( network.states, beliefs ) )


# Repeat above steps for second observation
# Now what is the probability of the code being buggy ?
#second_observation = { 'interpreter' : 'nw', 'cursor' : 'w' }
#beliefs = network.forward_backward( second_observation )
#beliefs = map( str, beliefs )
#print "\n".join( "{}\t{}".format( state.name, belief ) for state, belief in zip( network.states, beliefs ) )
