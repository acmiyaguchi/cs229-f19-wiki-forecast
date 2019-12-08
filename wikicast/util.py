import numpy as np
import pandas as pd
from .data import rmse, mape


def summarize(model_name, y, y_pred, trial_id=1):
    """Return a dictionary of results"""
    return {
        "mape": mape(y, y_pred),
        "rmse": rmse(y, y_pred),
        "name": model_name,
        "trial_id": trial_id,
    }


def run_train_predict(model, train, validate, test, features_list=[]):
    test_X = np.hstack([train[:, validate.shape[1] :], validate])
    z = np.hstack([train] + features_list)
    model.fit(z, validate)
    z = np.hstack([test_X] + features_list)
    return model.predict(z)


def run_ablation(name, model, train, validate, test, features_dict, trial_id=-1):
    results = []

    # run all
    pred = run_train_predict(model, train, validate, test, list(features_dict.values()))
    results.append(summarize(name, test, pred, trial_id=trial_id))

    # run without a single feature
    for feature_name in features_dict.keys():
        features_list = [v for k, v in features_dict.items() if k != feature_name]
        pred = run_train_predict(model, train, validate, test, features_list)
        results.append(
            summarize(f"{name}: without {feature_name}", test, pred, trial_id=trial_id)
        )
    return results


def write_search_results(search, output, verbose=True):
    df = pd.DataFrame(search.cv_results_).sort_values("rank_test_rmse")
    df.to_csv(output)
    if verbose:
        params = [c for c in df.columns if c.startswith("param_")]
        view_cols = [
            "mean_test_rmse",
            "mean_test_mape",
            "rank_test_rmse",
            "rank_test_mape",
            "mean_fit_time",
        ] + params
        print(df[view_cols])
    return df
