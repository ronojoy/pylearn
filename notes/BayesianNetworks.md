## Reading list

### Books

- Probabilistic reasoning in intelligent systems - J. Pearl (1988)
- Probabilist reasoning in expert systems - R. E. Neapolitan (1990)
- Learning Bayesian networks - R. E. Neapolitan (1992)
- An introduction to Bayesian networks - Jensen (1996)
- Graphical models - Lauritzen (1996)

### Papers

- Bayesian networks basics - Jensen 


## What are Bayesian networks ?

Parsimonious representations of joint probabilities that exploit conditional independences of variables.

"The belief network is a well-known graphical structure for representing independences in a joint probability distribution" - Neapolitan and Kenevan

##  Inference algorithms

Given the network, what is the probability distribution on the nodes when a subset takes on prescribed values.


## Learning algorithms

Parameter learning and structure learning.

##  Applications of Bayesian networks


## Naive Bayes and Tree augmented Bayes classifiers

- [Stackoverflow](https://stackoverflow.com/questions/14916351/learning-and-using-augmented-bayes-classifiers-in-python) question and answer on TAN Bayes classifier.

- [Customer churn prediction](http://content.iospress.com/articles/intelligent-data-analysis/ida00625) with Bayesian network classifiers


### Medical applications

- Medical applications (Heckerman)
- QMR-DT project (medical)
- Alarm Network for monitoring ICU patients
- Pathfinder (now Intellipath)
- Munin
- Promedas

### Non-medical applications

Hailfinder is a well-known system for forecasting severe summer hail in northeastern Colorado [2]. The BN is shown in Figure 5.3. Again, the number of values for each node is shown next to the node name in parentheses. The GEMS (Generator Expert Monitoring System) [195] project is an example of a system where BNs succeeded when a rule-based system did not [162].Vista [111] is a decision-theoretic system used at NASA Mission Control Center in Houston. It uses Bayesian networks to interpret live telemetry and provide advice on possible failures of the space shuttle’s propulsion systems. Vista recommends actions of the highest expected utility, taking into account time criticality.BNs have been used in a number of user modeling applications: software users in the Lumiere system [112], players in an adventure game [4] and various student models in intelligent tutoring systems [50, 49, 108, ?, ?] (see also 􏰐11.3).Oil price forecasting is an application that has been modeled with an ordinary BN [3] and with a DBN [63]. Other early DBN applications included robot navigation and map learning [70] (see also 􏰐4.6.1), monitoring robot vehicles [207, 208] and traffic monitoring in both [225] and the BATmobile project for monitoring an au- tomated vehicle traveling on a freeway [85]. A fragment of the BATmobile DBN is shown in Figure 5.4. The number of values for each node is shown in parenthe- ses, the inter-slice arcs are shown in thicker solid lines, while the intra-slice arcs are thinner. The intraslice arcs for 􏰊 􏰤 􏰥 are the same as for 􏰊 and hence omitted. The observation nodes are shaded.
BNs have been used for biological applications such as modeling the biological processes of a water purification plant [131] and for deciding on the amount of fungi- cides to be used against attack of mildew in wheat [126]. More recently there has been much interest in using BNs for ecological applications [80, 163, 26, 183, 13].

Bayesian networks have been successfully applied to create consistent probabilistic representations of uncertain knowledge in diverse fields such as medical diagnosis (Spiegelhalter et al., 1989), image recognition (Booker & Hota, 1986), language understanding (Charniak & Goldman, 1989a, 1989b), search algorithms (Hansson & Mayer, 1989), and many others. Heckerman et. al. (1995b) provides a detailed list of recent applications of Bayesian Networks. (http://www.pr-owl.org/index.php)



## Software

## Listings
- http://ksvanhorn.com/bayes/free-bayes-software.html (Great!)
- http://www.pa.icar.cnr.it/IDAschool/lectures/Bayesian.html

### Non-commercial

- aGrum
- http://jbnc.sourceforge.net/#References
- libpgm (very basic)
- pgmpy (very basic)

### Commercial

- Hugin
- Bayesia
- Netica
- Lumina

### Network repositories

- bnlearn http://www.bnlearn.com/bnrepository/
- Norsys Netica 

##### APIs

- Netica API
- Bayesia API
- Hugin API


## People

- Ron Kohlavi

## Presentations
- https://prezi.com/zjety6y7cwd9/bayesian-networks-1/ (nice example on doping)


## Software design

A modern object-oriented, parallel-scalable software system for Bayesian networks representation, inference and learning is missing. The ideal system should be implemented in C++, with bindings to other languages, with a graphical front-end to accompany it. Strategy should be to study the APIs of all popular commercial software and re-implement by ourselves. Since APIs do not have a copyright, this  should be good!
