"""Leakage-aware anomaly detection utilities."""

from sklearn.ensemble import IsolationForest

def fit_isolation_forest(X, contamination=0.05, random_state=42):
    model = IsolationForest(
        contamination=contamination,
        random_state=random_state,
        n_estimators=300
    )
    labels = model.fit_predict(X)
    scores = -model.score_samples(X)
    return model, labels, scores
