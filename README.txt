AQUORA WATER QUALITY MODEL HANDOFF

Files
-----
aquora_water_quality_ann_4sensor.joblib
    Complete trained sklearn Pipeline. This is the model artifact.
    It already contains imputation + StandardScaler + ANN.

train_model.py
    Reproduces the final model training/export procedure.

inference.py
    Loads the .joblib model and predicts Water_Quality_Index from four inputs.

feature_and_model_info.txt
    Feature order, preprocessing, ANN architecture, results, and constraints.

requirements.txt
    Python dependencies.

Input order
-----------
pH
Turbidity_NTU
TDS_mg_L
Temperature_C

Output
------
Water_Quality_Index (continuous numeric prediction)

Threshold
---------
No Safe/Unsafe or contamination threshold exists in the current project.

Current physical-sensor constraint
-----------------------------------
The deployed/current configuration uses only the four available sensors.
Extra dataset parameters are future work for possible sensor expansion.
