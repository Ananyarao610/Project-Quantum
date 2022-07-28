# Project-Quantum

## Introduction

This is a <b> <i> Quantum Inspired Optimization (QIO) </i> </b> based on the <i> Modern Portfolio Theory (MPT) </i>. It performs a multi-ojective portfolio optimisation which involves selecting the best portfolio (asset distribution) out of the given set of assets such that the expected returns from the ivestment is maximised and the risk is minimized. The problem defintion is transformed mathematically so that it can be quantised, or made compatible with quantum computing.

The quantised problem makes use of  Microsoft Azure's Quantum Inspired Optimizer and is solved using the <b><i> Parallel Tempering solver </i></b>. 

## Algorithm

Our objective function is a <i> Quadratic Unconstrained Binary Optimization (QUBO) </i>. QUBO is an <i><b>NP hard problem</b></i> which can be solved through quantum anneling or parallel tempering. In our solution, we have submitted our model to the <b><i>Parallel Tempering solver of Azure Quantum.</i></b>

Parallel tempering is a computer simulation method typically used to find the lowest free energy state of a system of many interacting particles at low temperature. More specifically, parallel tempering (also known as replica exchange MCMC sampling), is a simulation method aimed at improving the dynamic properties of Monte Carlo method simulations of physical systems.

Essentially, one runs N copies of the system, randomly initialized, at different temperatures. Then, based on the Metropolis criterion one exchanges configurations at different temperatures. The idea of this method is to make configurations at high temperatures available to the simulations at low temperatures and vice versa. This results in a very robust ensemble which is able to sample both low and high energy configurations. In this way, thermodynamical properties such as the specific heat, which is in general not well computed in the canonical ensemble, can be computed with great precision.




## Functionality and Modelling

The optimal portfolio allocation is found by maximising the expected portfolio fractional return and minimising the portfolio variance. Since an investor might also have a constraint on budget which can affect the optimal portfolio available to them, the problem defintion is subjected to a budget constraint. In order to quantize the problem, the weight of eachs stock in the portfolio is replaced by a decision vector. Consequently the budget is normalized to the stock appetite, or the number of stocks an investor can/wants to invest in and is applied as a soft constraint by making use of a slack variable. Finally in an attempt to conceptualise the optimized portfolio, the code allows for the equal distribution of an actual given budget and calcualtes the number of shares for each selected stock proportionally.
  


## Objective Function

This problem is classically represented as a <i> Mixed Integer Quadratic Progamming (MIQP) </i> problem as follows:

![alt text](https://github.com/Ananyarao610/Project-Quantum/blob/main/misc/MIQP%20eq.png)

To be able to quantise the problem, it is mapped to a QUBO problem with soft constraints for added functionality. Thus the objective function used is given by the QUBO problem's hamiltonian as:

![alt text](<https://github.com/Ananyarao610/Project-Quantum/blob/main/misc/QUBO%20eq.png>)



## Dataset
  
1)	D-wave’s 3 stock optimization (https://github.com/dwave-examples/portfolio-optimization)
  
2)	Kaggle’s Australian Historical Stock Prices (https://www.kaggle.com/code/ashbellett/portfolio-optimisation/notebook)
  
3)	Bombay Stock Exchange (BSE) Historical data for top 50 stocks for the last 20 years (https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.html?flag=0)

