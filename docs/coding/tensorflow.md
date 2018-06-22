---
title: Tensorflow
# sidebar: auto
# sidebarDepth: 2
---

# Tensorflow ML
I needed to learn about tensorflow, so I started about learning about what goes on within Tensorflow. This is the course I started with

## Hello?

### Framing?

Basic framework -> Supervised machine learning. 

Label $y$ is what we're trying to predict.
Features are input variables that describe our data $x_i$. 
$$\{ x_1,x_2, ...,x_n\}$$
Example is one piece of data i.e. x

Labelled example -> $\{x,y\}$. We have both, so we use this for training
Unlabelled example -> $\{x,?\}$. We have feature information but not the result

Model is used to map $x$ to $y$. There's model **training or learning** (uses labelled examples) and model inference i.e. applying the model to unlabelled examples.

### [Regression vs Classification](https://developers.google.com/machine-learning/crash-course/framing/ml-terminology)


**Regression** 
A regression model predicts continuous values. For example, regression models make predictions that answer questions like the following:

* What is the value of a house in California?* What is the probability that a user will click on this ad?

**Classification**
A classification model predicts discrete values. For example, classification models make predictions that answer questions like the following:

* Is a given email message spam or not spam?
* Is this an image of a dog, a cat, or a hamster?

### Linear Regression

![Regression](assets/regression.png)

How do we know if the above predicted line is correct or not? We need to think of regression as a problem of minimizing the loss function. 

**Choosing a convenient loss function**

$L_2$ Loss for a given example is also called squared error. 

i.e. Square of distance between prediction and label

= (observation - prediction)$^2$  
= ${(y-y')}^2$

**Defining $L_2$ loss over the entire dataset**

$$L_2Loss = \sum_{{(x,y)}\in D}^{} {(y-prediction(x))^2}$$

Where $\Sigma$ : Summing over the total dataset
$D$ : Sometimes useful to average over all the examples in the dataset , so a divide by $\frac{1}{||D||}$

#### Visualizing Loss function

![](https://developers.google.com/machine-learning/crash-course/images/LossSideBySide.png)

The left one is the loss function and the right is the regression line.

### Reducing Loss

Choosing model parameters to minimize the loss.

**Hyperparameters** are the configuration settings used to tune how the model is trained. 

How do we minimize the loss or see how the loss changes? 

We take the derivative of the loss function with respect to the weights and biases

For example ${(y-y)}^2$

* Easy to compute and convex

So, we repeatedly take steps in the direction that minimizes loss.

* These steps are called **Gradient Steps** (but they're really negative Gradient steps)
* Thus, this process is called **Gradient Descent**.

It's an iterative approach :

![](assets/iterative.png)

Data comes in, we compute the gradient of the loss function. The negative gradient tells us where to move to reduce the loss

**Where to start the weights?**