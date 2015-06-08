from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)

import daft

pgm = daft.PGM([5,4], origin=[1.15, 0.65])
pgm.add_node(daft.Node("survived", r"survived", 4, 4, aspect=1.8))
pgm.add_node(daft.Node("age", r"age", 2, 2, aspect=1.2, observed=True))
pgm.add_node(daft.Node("gender", r"gender", 3, 2, aspect=2.1, observed=True))
pgm.add_node(daft.Node("class", r"class", 4.5, 2, aspect=2.4, observed=True))
pgm.add_node(daft.Node("embark", r"embark", 6, 2, aspect=2.4, observed=True))
pgm.add_node(daft.Node("name", r"name", 3, 1, aspect=2.4, observed=True))
pgm.add_edge("survived", "age")
pgm.add_edge("survived", "gender")
pgm.add_edge("survived", "class")
pgm.add_edge("survived", "embark")
pgm.add_edge("age", "name")
pgm.add_edge("gender", "name")
pgm.render()
pgm.figure.savefig("titanic.pdf")
pgm.figure.savefig("titanic.png", dpi=150)
