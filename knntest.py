

class KNN:
    
    def __init__(self,k):
        self.k=k

    def fit(self,X,y):
        self.X_train=X
        self.y_train=y