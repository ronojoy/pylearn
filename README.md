PyLearn
=======

PyLearn is a resource for Bayesian machine learning in Python. 


### Introduction

How do we learn from experience ?   

Edwin Jaynes, in his influential [How does the brain do plausible reasoning ?](http://bayes.wustl.edu/etj/articles/brain.pdf), wrote

> One of the most familiar facts of our experience is this: that there *is* such a thing as common sense, which enables us to do plausible reasoning in a fairly consistent
way. People who have the same background of experience and the same amount
of information about a proposition come to pretty much the same conclusions as to
its plausibility. No jury has ever reached a verdict on the basis of pure deductive
reasoning. Therefore the human brain must contain some fairly deﬁnite mechanism
for plausible reasoning, undoubtedly much more complex than that required for
deductive reasoning. But in order for this to be possible, *there must exist consistent
rules for carrying out plausible reasoning, in terms of operations so deﬁnite that
they can be programmed on the computing machine which is the human brain*.

Jaynes went on to show that these "consistent rules" are just the rules of Bayesian probability theory, supplemented by Laplace's principle of indifference and, its generalization, Shannon's principle of maximum entropy. This key observation implies that a computer can be programmed to "learn", or, update probabilities based on data, in a manner that mimics the human brain. **Machine learning, then, is the creative application of Bayesian probability to problems of inference conditioned by data.** 

Given some very minimal desiderata, the rules of Bayesian probability are the only ones which conform to what, intuitively, we recognize as *rationality*.  [Rahul Siddharthan](www.imsc.res.in/~rsidd), my colleague at [The Institute of Mathematical Sciences](www.imsc.res.in), and I wrote a [short article in The Hindu](http://www.thehindu.com/sci-tech/science/article2747042.ece) about this. 

Here, I will list reading material, algorithms and their software implementation, and examples of applications of Bayesian machine learning to real-word problems. I welcome contributions - clone this repository and send me a pull request!

## Reading list

This is my reading list for Bayesian probability and its application to machine learning problems. The sections covered in this list are:

- [Classics of Bayesian probability](#classics)
- [Bayesian inference in statistical analysis]()
- [Bayesian decision theory]()
- [Bayesian risk analysis]()
- [Bayesian networks]()

### Classics of Bayesian probability
- Philosophical Essay on Probabilities - Pierre-Simon Laplace
- A Treatise on Probability - John Maynard Keynes
- Probability Theory - Harold Jeffreys
- Probability Theory : the logic of science - Edwin Jaynes

### Bayesian inference in statistical analysis
- Data analysis : a Bayesian tutorial - Devinder Sivia
- Bayesian statistics - P. M. Lee
- Bayesian inference in statistical analysis - Box and Tiao
- Bayesian data analysis - Gelman, Karlin, Stern and Rubin
