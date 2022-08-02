import os                              
import numpy as np
from numpy import number                    
import pandas as pd                     
import matplotlib.pyplot as plt  
import math
from typing import List
from azure.quantum.optimization import Term, SlcTerm
from statistics import variance



def return_terms(mu,n):
    """Calculates the Terms for the return component of the cost function

    Parameters
    ----------
    mu : np.array
        Expected return of each stock 
    n : integer
        Number of stocks
        
    Returns
    -------
    terms: list
        List of Terms associated with the return component of the cost function
    """
    
    terms=[]
    
    for i in range(0,n):
        
        terms.append(Term(c=-1*mu[i] , indices=[i]))
    print("Number of terms in return: ", len(terms))
    return terms



def risk(sigma,n,risk_aversion):
    
    """Calculates the Terms for the risk component of the cost function

    Parameters
    ----------
    sigma : np.array
        Covariance matrix of the dataset 
    n : integer
        Number of stocks
    risk_aversion: integer
        Risk aversion parameter
        
    Returns
    -------
    terms: list
        List of Terms associated with the risk component of the cost function
    """
    
    terms=[]
    
    for i in range(0,n):
        for j in range(0,n):
            terms.append(Term(c= sigma[i][j] * (risk_aversion/2) , indices=[i,j]))
    print("Number of terms in risk: ", len(terms))
    return terms





def budget_constraint(penalty_weight,n,b):
    
    '''
      Calculates the Terms for the normalized budget constraint

        Parameters
        ----------
        penalty_weight : integer
            Lagrange multiplier to penalise the stocks that don't obey the constraint 
        n : integer
            Number of stocks
        b : integer
            Normalized budget / stock appretite must be less than n

        Returns
        -------
        slc: list
            List of SlcTerms associated with the penalty constraint
        
    '''

    terms=[]
    for i in range(0,n):
        terms.append(Term(c= 1 , indices=[i]))
    terms.append(Term(c=-b, indices=[]))
    slc = []
    slc.append(SlcTerm(
            terms,
            c=1
        ))
    return slc




def find_risk(selected_stocks,n, result,sigma):
    
    '''Calculates the risk for the optimised portfolio
    
    Parameters
    ----------
    B: float
        budget to be equally invested

    Returns
    -------
    risk_perc: float
        percetnage risk value of the optimised portfolio with given budget
    '''

    w = 1/len(selected_stocks)
    var=0
    for i in range(0,n):
        for j in range(0,n):
            t = (w * result[str(i)])* (w * result[str(j)]) * sigma[i][j]
            var+=t
    risk = var**0.5
    risk_perc = risk * 100
    return risk_perc




def find_expected_daily_return(mu, selected_stocks, index_prices_selected):
    
    '''
    Calculates the expected return for the optimised portfolio
    
    Parameters
    ----------
    None

    Returns
    -------
    expected_dialy_roi: float
        Expected daily return on inverstment of the optimised portfolio
    
    '''
    expected_daily_roi=0
    number_stocks = len(selected_stocks)
    w = 1/ number_stocks
    for i in range(0,number_stocks):
        t = w * mu[index_prices_selected[i]]
        expected_daily_roi+=t
    return expected_daily_roi

def distributed_budget(B, arr, cp, index_prices_selected):
    
    '''
    Distributes the budget equally among all stocks to calculate the number of shares of each stock

    Parameters-
        B - Budget to be invested
        arr- List of strings representing selected stocks 
        cp - A numpy matrix representing the current prices

    Returns-
        shares - list containing number of shares of each stock to select
        
    '''

    shares=[]
    distribution = B/len(arr)  

    for i in range(len(arr)):
        numberOfShares = math.floor(distribution/cp[index_prices_selected[i]])   
        shares.append(numberOfShares)
        print(arr[i], " : " ,shares[i]," shares")
    return shares