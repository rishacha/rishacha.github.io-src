Title: Multi-armed bandits and algorithms
Slug: mab1
Date: Sunday May 22, 2022
Category: Online Learning and Optimization
Tags: multi-armed-bandits
Author: Rishabh Chakrabarti
Summary: My cheat sheet for bandit algorithms. Ref. Lattimore and Szepesvari

### Revision for $k$-armed bandit algorithms and problem setting
|Action space   |Problem Structure|Reward Mechanism|
|---            |---|---|
|<b>Infinite v/s Finite</b><ul><li>Finite - discretized. Choose an arm from a 3-arm bandit</li><li>Infinite - continuous i.e. choose from an interval between 0 and 1</li></ul>|Will selecting an action reveal any information about an action that you did not play? If yes, the problem has structure! Otherwise, you have an unstructured bandit problem. <ul><li><b>Unstructured</b>: This just means that if I have a two-arm bandit, I cannot learn anything about arm two by playing arm one. I might know that they’re both generating rewards by Gaussian distributions, but that doesn’t give me any connection between the arms.</li><li><b>Structured</b>: A structured bandit leaks information about other arms. Example: We could have a two-arm bandit where both arms generate rewards with a Bernoulli distribution that have a single parameter. What I mean is say arm one is parameterized by $\theta$ and arm two is parameterized by $1-\theta$. There’s only one parameter to learn, underlying the whole problem, and by playing the first arm, I gain information about the other arm! <br>Covariance matrix of the arm distributions -- $cov(arms) \ne \mathbb{I}$<br> **Linear bandit model is structured**</li></ul>|**Stochastic**:Under the stochastic reward generation setting, each action corresponds to an IID reward. That is, each action has an underlying distribution that it samples from when an action is selected. __*It never changes*__, therefore the learner simply needs to explore the arm until it can properly bound the shape of the reward generating distribution.|
|**Single action v/s Combinatorial action**<ul><li>Selection of 1 action</li><li>Combinatorial - Select a Vector of actions</li></ul>|**Contextual Bandit** - External Information can be utilized about the $\mathcal{E}$ <br> *Ex* - Say you have a two-arm bandit, but the arms perform differently on different days of the week (but the same on identical days of the week). If you attack this problem with a normal bandit algorithm, the rewards will appear highly non-stationary and will harm performance. However, if you use the context (the days of the week) in the action decision process then your learner should perform much better!|**Stationary v/s Non-stationary**<ul><li>**Stationary** - Reward distributions don't shift</li><li>**Non-Stationary** - Reward distributions can shift and come at a cost to the algorithm</li></ul>|
|<b>Single arm v/s $k$-armed</b>: A bandit environment ($\mathcal{E}$) can have a single-arm yielding some reward or multi-armed ($k$ armed) setting. |**Reward Vectors** Can be sampled from a *Gaussian distribution* or a *Bernouilli distribution* |**Adversarial Bandits** <ul><li>Adversary selects the worst-case rewards given knowledge of the learning agent's policy</li><li>In such cases, randomization becomes of key-importance so that adversary cannot predict our next move</li><ul>|

-----

###### Table of Algorithms - Frequentist Regret

| Algorithm                          |Setting |Input  | Environment  | Regret|
|----------------------------|---|---|---|---|
| ETC - Explore-then-Commit  |<ul><li> $k$ arms</li><li>Every arm has a probability distribution - $P_{a_i}$ + 1-sub-gaussian </li> <li>$m=f(\Delta,n)$ </li></ul>  |<ul><li>$\Delta_i$ = sub-optimality gap between $arm_1$ and $arm_i$ = $\mu_1 - \mu_i$</li><li>$n$ - time-horizon</li></ul>   | <ul><li> Unstructured $\mathcal{E}$</li><li> Stochastic Stationary</li> <ul>|For large n <br>$R_n \le \frac{4}{\Delta} ln(n) + C$ <br><br> With doubling trick, no need for knowlede of n and $R_n \le \frac{4}{\Delta ln(2)} {(ln(n))}^2 + C_1 ln(n)$|   
| $\mathcal{E}$ - Greedy  | Same as above except, there's no $m$   |  Same as above |<ul><li> Unstructured $\mathcal{E}$</li><li> Stochastic Stationary</li> <ul>   | For large n <br>$R_n \le \frac{1}{\Delta} ln(n) + C$|  
| Elimination   |<ul><li>Phased elimination of arms, using a hypothesis test</li></ul>   |<ul><li> Only time-horizon - $n$ </li><li>$\Delta$ is unknown</li></ul> |<ul><li> Unstructured $\mathcal{E}$</li><li> Stochastic Stationary</li> <ul>   |For large n <br>$R_n \le \frac{C_2}{\Delta} ln(n) + C_1$|   
|Upper-Confidence-Bound ($\delta$)<br> Known time horizon|<ul><li>Based on principle of **optimism in the face of uncertainty**</li><li>It creates an upper confidence bound, which is an overestimation of the unknown mean</li></ul>|<ul><li> Only time-horizon - $n$ </li><li>$\Delta$ is unknown</li></ul> |<ul><li> Unstructured $\mathcal{E}$</li><li> Stochastic Stationary</li> <ul>|
|Upper-Confidence-Bound - Arbitrary/Infinite Time Horizon|Same as above|<ul><li> Time-horizon - $n$ is unknown and arbitrarily set</li><li>$\Delta$ is unknown</li></ul> |<ul><li> Unstructured $\mathcal{E}$</li><li> Stochastic Stationary</li> <ul>|
|KL - Upper-Confidence-Bound ($\delta$)<br> Known time horizon|<ul><li>Difference between UCB and KL-UCB is that Chernoff's bound is used to define the UCB in this version</li></ul>|Same as UCB|<ul><li> Unstructured $\mathcal{E}$</li><li> Stochastic Stationary</li> <ul>|
|EXP3 - Exponential weight algo for Exploit and Explore|<ul><li>Abandon all assumptions on the reward mechanisms i.e. **adversarial**</li><li>Calculate a softmax sampling distribution using action-reward observed so far</li><li>Choose randomly from this sampling distribution</li></ul>|<ul><li> Learning rate calculated from time horizon( $n$) <br> $\eta = \sqrt{\frac{log(k)}{(nk)}}$ </li></ul>|<ul><li> Unstructured $\mathcal{E}$</li><li>Adversarial</li><ul>|
|LinUCB|||<ul><li>**Contextual**</li><li>**Linear**</li><li> Structured - $\mathcal{E}$</li><li>Stochastic Stationary</li> <ul>|

------

###### Table of Algorithms - Bayesian Regret

| Algorithm                          |Setting |Input  | Environment  |   
|----------------------------|---|---|---|
|Thompson Sampling|<ul><li>Bayesian Bandit environment - ($\mathcal{E},\mathfrak{B}(\mathcal{E}),Q,P$)</li></ul>|Prior Bayesian, Conjugate  pairs|<ul><li>We don't have a fixed environment and have a distribution of environments </li></ul>|

-----


