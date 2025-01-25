def evaluate_model(model, test_data):
    predictions = model.predict(test_data)
    accuracy = (predictions == test_data['target']).mean()
    
    from sklearn.metrics import classification_report
    report = classification_report(test_data['target'], predictions)
    
    return {
        'accuracy': accuracy,
        'report': report
    }