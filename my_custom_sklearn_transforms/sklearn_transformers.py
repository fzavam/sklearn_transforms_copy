
from sklearn.base import BaseEstimator, TransformerMixin
from scipy.stats.mstats import winsorize
import pandas as pd

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

# Nota máxima e mínima entre 0 e 10:   
class MaxMinNota(BaseEstimator, TransformerMixin):

    def __init__(self):
        return
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
  
        lim_inf_1 = len(data[data['NOTA_DE']==0.0])/len(data)
        lim_sup_1 = len(data[data['NOTA_DE']> 10.0])/len(data)
        data['NOTA_DE'] = winsorize(data['NOTA_DE'], limits=[lim_inf_1, lim_sup_1] )

        lim_inf_2 = len(data[data['NOTA_EM']==0.0])/len(data)
        lim_sup_2 = len(data[data['NOTA_EM']> 10.0])/len(data)
        data['NOTA_EM'] = winsorize(data['NOTA_EM'], limits=[lim_inf_2, lim_sup_2] )

        lim_inf_3 = len(data[data['NOTA_MF']==0.0])/len(data)
        lim_sup_3 = len(data[data['NOTA_MF']> 10.0])/len(data)
        data['NOTA_MF'] = winsorize(data['NOTA_MF'], limits=[lim_inf_3, lim_sup_3] )

        lim_inf_4 = len(data[data['NOTA_GO']==0.0])/len(data)
        lim_sup_4 = len(data[data['NOTA_GO']> 10.0])/len(data)
        data['NOTA_GO'] = winsorize(data['NOTA_GO'], limits=[lim_inf_4, lim_sup_4] )

        return data

# Soma das reprovações, usando a coluna MATRICULA:
class SomaReprov(BaseEstimator, TransformerMixin):

    def __init__(self):
        return
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
                     
        data['MATRICULA'] = data['REPROVACOES_DE'] + data['REPROVACOES_EM'] + data['REPROVACOES_MF'] + data['REPROVACOES_GO']
        
        return data
        
# Substituindo números faltantes pela média:
class MedNotas(BaseEstimator, TransformerMixin):

    def __init__(self):
        return
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
              
        data['NOTA_GO'] = data['NOTA_GO'].fillna(data[['NOTA_DE', 'NOTA_EM', 'NOTA_MF']].mean(axis=1))
        data['NOTA_DE'] = data['NOTA_DE'].fillna(data[['NOTA_GO', 'NOTA_EM', 'NOTA_MF']].mean(axis=1))
        data['NOTA_EM'] = data['NOTA_EM'].fillna(data[['NOTA_DE', 'NOTA_GO', 'NOTA_MF']].mean(axis=1))
        data['NOTA_MF'] = data['NOTA_MF'].fillna(data[['NOTA_DE', 'NOTA_EM', 'NOTA_GO']].mean(axis=1))
        
        return data


