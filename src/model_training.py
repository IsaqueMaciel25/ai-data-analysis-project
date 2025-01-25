class ModelTrainer:
    def __init__(self, model, X_train, y_train):
        self.model = model
        self.X_train = X_train
        self.y_train = y_train

    def train_model(self):
        self.model.fit(self.X_train, self.y_train)

    def save_model(self, filename):
        import joblib
        joblib.dump(self.model, filename)