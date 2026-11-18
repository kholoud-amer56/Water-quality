AQUORA WATER QUALITY — UI HANDOFF
======================================

Purpose
-------
This package contains the final deployable water-quality model interface for
the current Aquora hardware configuration.

CURRENT PHYSICAL INPUTS
-----------------------
Only these four sensors are required:
1. pH
2. Turbidity_NTU
3. TDS_mg_L
4. Temperature_C

MODEL
-----
ANN / scikit-learn MLPRegressor.
The trained model is stored in:
    aquora_water_quality_ann_4sensor.joblib

IMPORTANT:
The .joblib file contains the FULL preprocessing pipeline:
    median imputation -> StandardScaler -> ANN

A separate scaler/preprocessor file is NOT required.

OUTPUT
------
The model returns:
    Water_Quality_Index

This is a continuous numeric prediction.

There is currently NO:
- Safe/Unsafe threshold
- contamination classification
- Leak/No-Leak classification
- automatic alarm decision
- hardcoded WQI status

Do not add a threshold in the UI unless the project team later agrees on and
documents a scientifically justified threshold.

API
---
The included app.py exposes:

GET /health

POST /predict

POST /predict request JSON:
{
  "pH": 7.0,
  "Turbidity_NTU": 2.0,
  "TDS_mg_L": 300.0,
  "Temperature_C": 22.0
}

POST /predict response JSON:
{
  "Water_Quality_Index": <numeric prediction>
}

Run:
    pip install -r requirements_api.txt
    uvicorn app:app --host 0.0.0.0 --port 8000

Then the UI can send:
    POST http://<backend-host>:8000/predict

The browser/front-end should NOT try to execute the .joblib file directly.
Use the Python API/backend unless the team later decides to manually port the
ANN and preprocessing to another runtime.

UI DISPLAY RECOMMENDATION
-------------------------
Show the four current sensor readings:
- pH
- Turbidity
- TDS
- Temperature

Show the model output:
- Water Quality Index (numeric)

Optional wording:
"AI-estimated Water Quality Index"

Avoid presenting the value as an independently validated contamination result.

PROJECT CONTEXT
---------------
The research experiment showed that additional water-quality parameters available
in the dataset can improve WQI estimation. Those parameters are NOT current
hardware inputs and are therefore future sensor-expansion work.

The current UI/model is intentionally restricted to the four available sensors.

SCIENTIFIC SCOPE
----------------
The model estimates the existing dataset's Water_Quality_Index.
It should not be described as independent contamination detection.
