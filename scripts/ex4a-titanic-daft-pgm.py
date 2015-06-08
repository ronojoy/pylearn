from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)

import daft

# instantiate a pgm object
pgm = daft.PGM([6,4], origin=[0, 1])


# create the nodes
survived = daft.Node("survived", r"survived", 4, 4, aspect = 1.8)
age = daft.Node("age", r"age", 2, 3, aspect = 1.8)
gender = daft.Node("gender", r"gender", 3, 3, aspect = 1.8, observed=True)
tclass = daft.Node("class", r"class", 4, 3, aspect = 1.8,observed=True)
embark = daft.Node("embark", r"embark", 5, 3, aspect = 1.8, observed=True)
name = daft.Node("name", r"name", 3, 2, aspect = 1.8, observed=True)

# add the nodes to pgm object
pgm.add_node(survived)
pgm.add_node(age)
pgm.add_node(gender)
pgm.add_node(tclass)
pgm.add_node(embark)
pgm.add_node(name)

# add edges between nodes
pgm.add_edge("survived", "age")
pgm.add_edge("survived", "gender")
pgm.add_edge("survived", "class")
pgm.add_edge("survived", "embark")
pgm.add_edge("age", "name")
pgm.add_edge("gender", "name")
pgm.render()
pgm.figure.savefig("titanic.pdf")
pgm.figure.savefig("titanic.png", dpi=150)
