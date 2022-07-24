# Project-Quantum

## Introduction

This is a <b> <i> Quantum Inspired Optimization (QIO) </i> </b> based on the <i> Modern Portfolio Theory (MPT) </i>. It performs a multi-ojective portfolio optimisation which involves selecting the best portfolio (asset distribution) out of the given set of assets such that the expected returns from the ivestment is maximised and the risk is minimized. The problem defintion is transformed mathematically so that it can be quantised, or made compatible with quantum computing.

The quantised problem makes use of <b> <i> Microsoft Azure's </i> </b> Quantum Inspired Optimizer and is solved using the <b><i> Parallel Tempering solver </i></b>. 

## Algorithm

Our objective function is a <i> Quadratic Unconstrained Binary Optimization (QUBO) </i>. QUBO is an <i><b>NP hard problem</b></i> which can be solved through quantum anneling or parallel tempering.

Parallel tempering is a computer simulation method typically used to find the lowest free energy state of a system of many interacting particles at low temperature. 

## Objective Function

This problem is classically represented as a <i> Mixed Integer Quadratic Progamming (MIQP) </i> problem as follows:

<insert image link here>

To be able to quantise the problem, it is mapped to a QUBO problem with soft constraints for added functionality. Thus the objective function used is given by the QUBO problem's hamiltonian as:

<insert image link here>
  
## Functionality and Modelling

The optimal portfolio allocation is found by maximising the expected portfolio fractional return and minimising the portfolio variance. Since an investor might also have a constraint on budget which can affect the optimal portfolio available to them, the problem defintion is subjected to a budget constraint. In order to quantize the problem, the weight of eachs stock in the portfolio is replaced by a decision vector. Consequently the budget is normalized to the stock appetite, or the number of stocks an investor can/wants to invest in and is applied as a soft constraint by making use of a slack variable. Finally in an attempt to conceptualise the optimized portfolio, the code allows for the equal distribution of an actual given budget and calcualtes the number of shares for each selected stock proportionally.
  
 
----rough points

In one time period, r∈Rn is the return vector where ri is the return on asset i. The return is the difference in price divided by the price at the beginning of the period: ri=pt+1−ptpt. Portfolio return R is given by: R=rTx.

The return vector r can be modelled as a random variable with mean E[r]=μ and covariance E[(r−μ)(r−μ)T]=Σ. It follows that the portfolio return is also a random variable with mean E[R]=μTx and variance Var[R]=xTΣx.
  
MPT assumes the investor is risk averse - meaning given the option between two portfolios with the same expected return, they will choose the one with ther least risk.


## Dataset
  
1)	D-wave’s 3 stock optimization (https://github.com/dwave-examples/portfolio-optimization)
  
2)	Kaggle’s Australian Historical Stock Prices (https://www.kaggle.com/code/ashbellett/portfolio-optimisation/notebook)
  
3)	Bombay Stock Exchange (BSE) Historical data for top 50 stocks for the last 20 years (https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.html?flag=0)

