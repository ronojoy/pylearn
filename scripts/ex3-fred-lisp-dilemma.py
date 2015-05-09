#This script implements a Bayesian network for Fred's Lisp Dilemma from 
# Korb and Nicholson's Bayesian Artifician Intelligence. 
# The problem statement is as follows:

#   Fred is debugging a LISP program. He just typed an expression to the LISP
#   interpreter and now it will not respond to any further typing. He can't see
#   the visual prompt that usually indicates the interpreter is waiting for
#   further input. As far as Fred knows, there are only two situations that
#   could cause the LISP interpreter to stop running: (1) there are problems
#   with the computer hardware; (2) there is a bug in Fred's code. Fred is
#   also running an editor in which he is writing and editing his LISP code; if
#   the hardware is functioning properly, then the text editor should still be
#   running. And if the editor is running, the editor's cursor should be
#   flashing. Additional information is that the hardware is pretty reliable,
#   and is OK about 99% of the time, whereas Fred's LISP code is often buggy,
#   say 40% of the time .
#
#   Solution contributed by k.rohini@gmail.com 
#   Comments added by rjoy@imsc.res.in

import numpy as np
from pomegranate import *

# Fred's code has bug 4 out of 10 times
code = DiscreteDistribution( { 'w': 0.6, 'nw': 0.6 } )

# The hardware works correcty 99 out 100 times
hardware = DiscreteDistribution( { 'w': 0.99, 'nw': 0.01 } )

# The interpreter state depends on both code and hardware
interpreter = ConditionalProbabilityTable(
            [[ 'w', 'w', 'nw', 0.0 ],
             [ 'w', 'nw', 'nw', 1.0 ],
             [ 'nw', 'w', 'nw', 1.0 ],
	           [ 'nw','nw','nw', 1.0],
             ['w','w','w', 1.0],
 	           ['w','nw','w',0.0],
       	     ['nw','w','w', 0.0],
             ['nw','nw','w', 0.0]], [code, hardware] )  

# The editor works if the hardware works
editor = ConditionalProbabilityTable(
		[[ 'w','w',1],
		 ['nw','w',0],
     ['w','nw',0],
     ['nw','nw',1]],[hardware])

# The cursor works if the editor works
cursor = ConditionalProbabilityTable(
		[['w','w',1],
		 ['nw','w',0],
 		 ['w','nw',0],
		 ['nw','nw',1]],[editor])

# State objects hold both the distribution, and a high level name.
s1 = State( code, name="code" )
s2 = State( hardware, name="hardware" )
s3 = State( interpreter, name="interpreter" )
s4 = State( editor,name="editor")
s5 = State ( cursor, name = "cursor")

# Create the Bayesian network object with a useful name
network = BayesianNetwork( "Freds LISP Problem" )

# Add the three nodes to the network 
network.add_nodes( [ s1, s2, s3, s4, s5 ] )

# Add transitions which represent conditional depesndencies, where the second node is conditionally dependent on the first node (Monty is dependent on both guest and prize)
network.add_edge( s1, s3 )
network.add_edge( s2, s3 )
network.add_edge(s2,s4)
network.add_edge(s4,s5)
network.bake()

# The first observation is that the interpreter is not working
first_observation = { 'interpreter' : 'nw' }

# beliefs will be an array of posterior distributions or clamped values for each state, indexed corresponding to the order
# in self.states. 
beliefs = network.forward_backward( first_observation )

# Convert the beliefs into a more readable format
beliefs = map( str, beliefs )

# Print out the state name and belief for each state on individual lines
# What is the probability of the code being buggy ? 
print "\n".join( "{}\t{}".format( state.name, belief ) for state, belief in zip( network.states, beliefs ) )


# Repeat above steps for second observation
# Now what is the probability of the code being buggy ? 
second_observation = { 'interpreter' : 'nw', 'cursor' : 'w' }
beliefs = network.forward_backward( second_observation )
beliefs = map( str, beliefs )
print "\n".join( "{}\t{}".format( state.name, belief ) for state, belief in zip( network.states, beliefs ) )
