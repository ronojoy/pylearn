## Bayesian machine learning for business decisions

#### Ronojoy Adhikari

There is a lot of buzz in the business world today about the
potentialities of data and how it can lead to better informed business
decisions. As any buzz is borne on the shoulders of buzzwords, we are
not surprised when we encounter big data, data science,  machine
learning, random forests, decision trees, support vector machines,
naive Bayes classifiers and numerous other magic phrases of
incantation that are supposed to make the data speak. How, then, do we
separate from this multitude the wheat of what is likely to be of
long-term use from the chaff of what may merely be current fashion ?
Here I offer a point view on this question that looks outwards from
academia towards the world of business applications. 

Business decisions, as decisions elsewhere, have to taken in the face
of *uncertainty* and *complexity*. The most striking manifestation of the joint workings of these aspects appears in the ubiquitous fluctuations of the stock market : the future price of a stock is both uncertain and related in complex ways to the price of other stocks.

The human intelligence is notoriously poor at dealing with uncertainty.
Our intuitions are often misled on even the simplest of problems that
involve uncertainty. A recent example is provided by the popular Monty Hall
show. There, contestents are to guess which of three shut doors hides a 
prize. Following the contestants choice, the show host reveals a door
which does not hide the prize. The contestant is then asked : would
they alter their initial choice ? A room full of people presented with this choice are usually evenly split between retaining the initial choice of door and altering it. Both choices are passionately held as correct and has led to many bytes of exchange in the internet.  A careful mathematical analysis is required to show that the chance of winning this prize is higher for those who choose to alter their initial choice - it always makes better sense to switch. 

Uncertainty in the real world presents itself in a far more complex
forms than the binary choice of the Monty Hall show.  In such situations, the
human intuition is even more prone to error. However, decisions have to be taken and must be taken reliably. 

In the past two decades there have been scientific breakthroughs in the
construction of algorithms that allow computers to reason reliably in
the face of uncertainty and complexity. The 2011 Turing Award in
computer science, the equivalent of a Nobel Prize, went to Judea
Pearl, one of the key figures of the "reasoning revolution". (Pearl is the father of the late journalist Daniel Pearl and has started a foundation in his memory.)

Pearl's work allows computers to go beyond just reasoning : it allows for the
automatic discovery of causal connections between factors. The
hopeless despair contained in the the adage "correlation does not
imply causation" has now been replaced by an optimism that problems
deemed intractable within conventional statistics are now within the
grasp of a solution. Research in this area is very interdisciplinary,
bringing together physicists, computer scientists, engineers, and
statisticians. I will refer to the area collectively as Bayesian
machine learning.

How does Bayesian machine learning differ from conventional statistics
and why should you, the business decision maker, care ? The short
answer is that Bayesian methods take the view of specific case studies
while conventional methods take the view of general purpose black
boxes. A conventional statistical analysis takes your problem and fits
it to the solution : a one size fits all approach. Machine learning
tools such as the popular scikits-learn package provide these solutions
as black boxes, ready to receive data and output numbers. However, as
Richard Hamming, another Turing laureate, had famously said, "the purpose of computing is insight, not
numbers". This is where Bayesian machine learning methods score : they
build a solution out of your specific problem and provide you with a level of insight that conventional statistical methods are unable to do. Without going into  technical details, Bayesian machine learning methods are like
lego blocks - a small set  of components are assembled together to
build a solution that best fits the requirement of your problem.

The Bayesian revolution swept through many scientific disciplines,
beginning in physics, reaching over to biology and medicine, and now, engineering
and computer science. It is only now beginning to make its presence
felt in the world of business and, when combined with the unprecedented amount of data that is becoming available, is certaing to revolutionize business practice.  The following give a flavour of the enormous excitement surrounding the area. The MIT Technology Review had included Bayesian machine learning in its list of 10 technologies that will change the 21st century. Big players like Microsoft, Amazon and Google have invested heavily in machine learning platforms. Infer.net and Azure ML from Microsoft, AWS ML from Amazon, and the many Bayesian algorithms that are used in the Google products that we use daily are the outcome of this investment. 

Bill Gates was one of the earliest to spot the potential of Bayesian machine learning technology and his prescient remark, now more than a decade old, was that Microsoft's competitive advantage lay in their "expertise in Bayesian networks". With hindsight, we now understand why this should be : the power of human beings to integrate disparate pieces of uncertain evidence is limited. Computers, teethed with Bayesian machine learning algorithsm, have no such limitations. Thus, they can aid us in spotting patterns that we will miss, in segregating categories we may easily conflate, and in being better and smarter at arriving at decisions in a complex and uncertain world. A business that ignores this technology will do so at its own peril!

At Value From Data, an initiative between Future Focus Infotech and
the Institute of Mathematical Sciences, we are trying to bring the 
expertise of Bayesian machine learning to businesses in India to enhance their competitiveness internationally.