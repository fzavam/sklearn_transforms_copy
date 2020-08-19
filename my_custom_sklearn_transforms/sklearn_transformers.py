from sklearn.base import BaseEstimator, TransformerMixin


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

class preprocessamento_1(BaseEstimator):

    def __init__(self):
        pass

    def fit(self, documents, y=None):
        return self

    def transform(self, x_dataset):
      # Winsorizando ("encapsulando") as notas entre 0 e 10.
        lim_inf_1 = len(x_dataset[x_dataset['NOTA_DE']==0.0])/len(x_dataset)
        lim_sup_1 = len(x_dataset[x_dataset['NOTA_DE']> 10.0])/len(x_dataset)
        x_dataset['NOTA_DE'] = winsorize(x_dataset['NOTA_DE'], limits=[lim_inf_1, lim_sup_1] )

        lim_inf_2 = len(x_dataset[x_dataset['NOTA_EM']==0.0])/len(x_dataset)
        lim_sup_2 = len(x_dataset[x_dataset['NOTA_EM']> 10.0])/len(x_dataset)
        x_dataset['NOTA_EM'] = winsorize(x_dataset['NOTA_EM'], limits=[lim_inf_2, lim_sup_2] )

        lim_inf_3 = len(x_dataset[x_dataset['NOTA_MF']==0.0])/len(x_dataset)
        lim_sup_3 = len(x_dataset[x_dataset['NOTA_MF']> 10.0])/len(x_dataset)
        x_dataset['NOTA_MF'] = winsorize(x_dataset['NOTA_MF'], limits=[lim_inf_3, lim_sup_3] )

        lim_inf_4 = len(x_dataset[x_dataset['NOTA_GO']==0.0])/len(x_dataset)
        lim_sup_4 = len(x_dataset[x_dataset['NOTA_GO']> 10.0])/len(x_dataset)
        x_dataset['NOTA_GO'] = winsorize(x_dataset['NOTA_GO'], limits=[lim_inf_4, lim_sup_4] )

      # Usando a coluna MATRICULA que é irrelevante para somar os valores da reprovação
        x_dataset['MATRICULA'] = x_dataset['REPROVACOES_DE'] + x_dataset['REPROVACOES_EM'] + x_dataset['REPROVACOES_MF'] + x_dataset['REPROVACOES_GO']

      # Preenchendo as notas faltantes pela média das outras notas do aluno
        x_dataset['NOTA_GO'] = x_dataset['NOTA_GO'].fillna(x_dataset[['NOTA_DE', 'NOTA_EM', 'NOTA_MF']].mean(axis=1))
        x_dataset['NOTA_DE'] = x_dataset['NOTA_DE'].fillna(x_dataset[['NOTA_GO', 'NOTA_EM', 'NOTA_MF']].mean(axis=1))
        x_dataset['NOTA_EM'] = x_dataset['NOTA_EM'].fillna(x_dataset[['NOTA_DE', 'NOTA_GO', 'NOTA_MF']].mean(axis=1))
        x_dataset['NOTA_MF'] = x_dataset['NOTA_MF'].fillna(x_dataset[['NOTA_DE', 'NOTA_EM', 'NOTA_GO']].mean(axis=1))
        
        return x_dataset
