from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

folder = Path(__file__).resolve().parent
df = pd.read_csv(folder / "grid_preview_50.csv")
df["mw_1"] = pd.to_numeric(df["mw_1"], errors="coerce")
df["q_year"] = pd.to_numeric(df["q_year"], errors="coerce")
valid = df.dropna(subset=["mw_1", "q_year"]).copy()
valid = valid[valid["mw_1"] >= 0].copy()
X = np.column_stack([np.log1p(valid["mw_1"]), valid["q_year"]])
model = IsolationForest(n_estimators=200, contamination=0.10, random_state=42)
valid["anomaly_flag"] = model.fit_predict(X) == -1
valid["anomaly_score"] = model.decision_function(X).round(5)
cols = ["q_id", "q_status", "state", "type_clean", "mw_1", "q_year", "anomaly_flag", "anomaly_score"]
valid[cols].to_csv(folder / "grid_ml_results.csv", index=False)
print(f"Analyzed {len(valid)} records; flagged {valid.anomaly_flag.sum()} unusual observations")
print(valid.loc[valid.anomaly_flag, cols].to_string(index=False))
