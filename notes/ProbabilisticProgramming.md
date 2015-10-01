# Probabilistic Programming in Python

[TOC]

## Introduction

### An invitation to probability

- Uncertainty in the real world : from Tycho Brahe to Laplace. Tycho Brahe -> Kepler (generalization -> from facts to knowledge ; specific to the general); Kepler - Newton (causal explanation - forces cause motion; the gravitational force varies as inverse square of distance; Newton -> Laplace (uncertainty in the real world - knowledge of the world is imprecise and incomplete)

- Historical excursion shows how we reason about the world : Reasoning about the world : Deductive logic : From Aristotle - Boole - Lovelace | Inductive logic : From Bernoulli - Laplace - Gibbs - Jaynes | Beyond formal logic : can something be A and not A ? Dialectical reasoning under uncertainty is an unexplored area in machine intelligence.  

- Epistemic uncertainty and ontological uncertainty; Quantum mechanics "God does not play dice"

> Researchers have long modeled the behavior of agents using
logic, but logical models are a poor choice for dealing with
the uncertainty of the real world. For dealing with inherent
uncertainty and with incomplete knowledge, probabilistic
models are better. - Ramsey and Pfeffer

### Causality, deduction and induction

- Causal models of the world; effects have causes; effects precede causes
- Reasoning from cause to effect : deduction (running a programme)
- Reasoning from effect to probable cause : induction (running a programme backwards)
- Bayes theorem : the F=ma of inductive inference. 
- Practical example : is this a fair coin ? data, model, and inference. 

### Complexity and its simplification

The world and its map 

- Chains of causality
- Structuring and decomposition of probability distributions. 
- Graphical models as a representation of structure
- Causality in structure determination

Graphical models have served us well for two decades. (List all graphical model toolkits). However, they are tedious to build and maintain. 

### Modularity and reuse

> As models grow large, it becomes important to be able to build them easily and to reuse the parts - but considered as programming languages, the techniques used to build probabilistic models are weak. - Ramsey and Pfeffer


###  The need for a new programming paradigm

> Darpa PPAML programme attempts the following :
- Dramatically increase the number of people who can successfully build machine learning applications;
- Make machine learning experts radically more effective;
- Enable new applications that are inconceivable today.

## Probabilistic programming

Probabilistic programming : 

> Probabilistic Programming is a way of defining probabilistic models by overloading the operations in standard programming language to have probabilistic meanings. The goal is to specify probabilistic models in a compact manner for human communication and in a precise manner for automatic inference. - Minka and Winn

### Design principles

- **1. Probability distributions** - elementary random primitives; Expressions are probability distributions not numbers. Method for sampling from a probability distribution


- **2. Conditionalization** : "The power of probabilistic programming doesn’t come from merely specifying probabilistic primitives however, as that can be easily done with standard programming languages (e.g. rand). Instead it is their ability to condition on observations (or functions thereof). For example, we can write something like the following program: (Al Quraishi)


- **3. Separation of model from inference** : [Infer.net blog](http://blogs.msdn.com/b/infernet_team_blog/archive/2011/09/30/the-separation-of-model-and-inference.aspx) quote : "The Infer.NET API provides a way of declaratively describing a model, and the Infer.NET compiler generates the code that runs inference on the model." The advantages of separating model from inference are 

 - **Transparency**: model assumptions are stated clearly in declarative code and not conflated with the, often complex, inference code. 
 - **Consistency**: the model, once declared, can be used repeatedly for distinct tasks like learning parameters or making predictions
 - **Flexibility**: the same model can be used with different inference algorithms.
 - **Maintainability**: since model declaration is localised, changes and improvements to the model can be made easily. 

 This is analogous to separating the ode specification from the solution method in ode solvers. The ode is the (deterministic) model of the world, the solver is a way of answering a (deterministic) query from the model.

### Probabilistic Programming in Python

- [Lea](https://bitbucket.org/piedenis/lea) - discrete probability distributions in Python from Pierre Denis
- [Pomegranate](https://github.com/jmschrei/pomegranate) - graphical models, inference and learning from J Schreiber
- [BayesPy](http://www.bayespy.org/) - variational inference on exponential families from Jaakko Luttinen et al
- [PyMC3](https://pymc-devs.github.io/pymc3/getting_started/) - state of the art MCMC probabilistic programming system by Salvatier, Wiecki, Fonnesbeck et al 

### When should you use probabilistic programming ? 

- Comparison of black box and open box methods (Indian astronomy versus Newtonian orbit calculations - mention quote)
- "The purpose of computing is insight, not numbers"
- Standard machine learning problem - better off with Scikits-Learn
- Cutting edge problem without predefined solution - give PPS a try

## Learning resources

### Blog posts
- [The state of probabilistic programming](https://moalquraishi.wordpress.com/2015/03/29/the-state-of-probabilistic-programming/) by Mohammed AlQuraishi (2015)
- [What is probabilistic programming?](http://www.pl-enthusiast.net/2014/09/08/probabilistic-programming/) by Michael Hicks of PL-Enthusiast (2014)
- [What is probabilistic programming?](http://radar.oreilly.com/2013/04/probabilistic-programming.html) by Beau Cronin (2013)
- [Why probabilistic programming matters](https://plus.google.com/u/0/+BeauCronin/posts/KpeRdJKR6Z1) by Beau Cronin (2013)
- [Why probabilistic programming matters](http://zinkov.com/posts/2012-06-27-why-prob-programming-matters/) by Rob Zinkov (2012)


### Slidedecks

- [Probabilistic programming in sports analytics](http://london.pydata.org/schedule/presentation/5/) by Peadar Coyle (2015)
- [Probabilistic programming in Python with PyMC3](http://www.slideshare.net/PyData/probabilistic-programming-in-python-with-pymc3-john-salvatier) by John Salvatier
- [Probabilistic programming : Why, What, How, When](http://www.slideshare.net/salesforceeng/probabalistic-programming-why-what-how-when) by Beau Cronin
- [Stan : A Probabilistic Programming Language](http://www.slideshare.net/dlebauer/daniel-lee-stan) by Daniel Lee
- [Probabilistic programming](conferences.inf.ed.ac.uk/bayes250/slides/winn.pdf) by John Winn (2011)

### Online discussions

- [Hacker News](https://news.ycombinator.com/item?id=9363496) discussion on AlQureishi's article on the [The state of probabilistic programming](https://moalquraishi.wordpress.com/2015/03/29/the-state-of-probabilistic-programming/).


### Ipython notebooks

- [Probabilistic programming and Bayesian methods for Hackers](http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/) by Cam Davidson Pilon and collaborators


### Textbooks
- [Practical probabilistic programming](http://www.manning.com/pfeffer/) by Avi Pfeffer

## Research resources

### Research groups

- [Probabilistic programming for advanced machine learning](http://ppaml.galois.com/wiki/) - Darpa funded programme 2013 - 2017
- [Oxford Probabilistic Programming Reading Group](http://www.robots.ox.ac.uk/~perov/reading_groups/probprob2013/) - contains pointers to research, programming languages, and software
- [Probabilistic-Programming.Org](http://probabilistic-programming.org/wiki/Home) - from Daniel Roy
### References

- [Design and Implementation of Probabilistic Programming Languages](http://dippl.org/) - Goodman and Stuhmuller (2015)
- [Probabilistic programming as spreadsheet queries](http://research.microsoft.com/apps/pubs/default.aspx?id=231027) by Gordon et al (2014)
- [Probabilistic programming]() by Rajamani et al (2014)
- [Probabilistic programming concepts](http://arxiv.org/abs/1312.4328) - Raedt and Kimmig (2013)
- [An agenda for probabilistic programming](http://research.microsoft.com/en-us/projects/fun/agendaforprobabilisticprogramming.pdf) by Andrew Gordon (2013)


## Code

### Probabilistic programming languages

- BUGS
- STAN (no discrete random variables)
- PyMC3
- Infer.net
- BayesPy (only exponential families)


**Darpa PPAML project funded**
- Venture
- Figaro
- [BLOG](http://bayesianlogic.github.io/) - Stuart Russel / UC Berkeley
- Church
- Haruku 
- Chimple / Dimple


###  Probabilistic models

- [Repository of models](http://forestdb.org/)

### Applications
- [Tabular](http://research.microsoft.com/en-us/downloads/0052e599-2f39-423d-8a55-798d5ce421cd/) - Knowledge discovery in spreadsheets

### Rough Quotes

> It is remarkable that a science which began with the consideration of games of chance should have become the most important object of human knowledge - Laplace, 1812

> A very senior Microsoft developer who moved to Google told me that Google works and thinks at a higher level of abstraction than Microsoft. "Google uses Bayesian filtering the way Microsoft uses the if statement," he said. -Joel Spolsky


### Software stack

 - Pandas data frame
 - Seaborn (for plotting)