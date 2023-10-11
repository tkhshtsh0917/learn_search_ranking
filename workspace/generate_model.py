#!/usr/bin/env python

import json

from xgboost import DMatrix, train


def get_feature_names_from_feature_set():
    with open("hands_on_featureset.json") as fp:
        feature_set = json.load(fp)
    
    return list(
        feature["name"] for feature in feature_set["featureset"]["features"]
    )


feature_names = get_feature_names_from_feature_set()

params = {
    "objective": "rank:pairwise",
    "eval_metric": "ndcg",
    "tree_method": "hist",
    "grow_policy": "lossguide",
    "max_leaves": 60,
    "subsample": 0.45,
    "eta": 0.1,
    "seed": 42,
}


training_input = DMatrix(
    "hands_on_featuredata.txt.training", feature_names=feature_names
)
validation_input = DMatrix(
    "hands_on_featuredata.txt.validation", feature_names=feature_names
)

bst = train(
    params,
    training_input,
    num_boost_round=200,
    evals=[(training_input, "train"), (validation_input, "valid")],
    verbose_eval=10,
)

model = bst.get_dump(dump_format="json")

with open("hands_on_model.json", "w") as fp:
    wrapped_model = {
        "model": {
            "name": "hands_on_model.json",
            "model": {
                "type": "model/xgboost+json",
                "definition": "[" + ",".join(list(model)) + "]",
            },
        }
    }

    json.dump(wrapped_model, fp, indent=2)
    fp.write("\n")
