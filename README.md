# Project-Quantum

## Introduction

This is a <b> <i> Quantum Inspired Optimization (QIO) </i> </b> to select the best portfolio (asset distribution) out of the given set of assets such that the returns from the ivestment is maximised and the risk is minimized. The strategy used for optimization is the Mean Variance Optimization where the optimal risk-adjusted portfolio that lies on the efficient frontier is found. 

The problem is submitted to Microsoft azure's Quantum Inspired Optimizer and solved using the <b><i> Parallel Tempering solver </i></b>.


## Algorithm
Our objective function is a Quadratic Unconstrained Binary Optimization (QUBO). QUBO is an <i><b>NP hard problem</b></i>. 

## Objective Function

The optimal portfolio allocation is found by maximising the expected portfolio fractional return and minimising the portfolio variance. This becomes a mixed-integer quadratic programming problem. 


----rough points

In one time period, r∈Rn is the return vector where ri is the return on asset i. The return is the difference in price divided by the price at the beginning of the period: ri=pt+1−ptpt. Portfolio return R is given by: R=rTx.

The return vector r can be modelled as a random variable with mean E[r]=μ and covariance E[(r−μ)(r−μ)T]=Σ. It follows that the portfolio return is also a random variable with mean E[R]=μTx and variance Var[R]=xTΣx.



## Budget Constraint



## Dataset
