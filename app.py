from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd

MODEL_PATH = "aquora_water_quality_ann_4sensor.joblib"
FEATURES = ["pH", "Turbidity_NTU", "TDS_mg_L", "Temperature_C"]

app = FastAPI(
    title="Aquora Water Quality API",
    version="1.0.0",
    description="Predicts the dataset Water_Quality_Index from the four available Aquora water-quality sensors."
)

model = joblib.load(MODEL_PATH)

class WaterQualityInput(BaseModel):
    pH: float = Field(..., description="Water pH")
    Turbidity_NTU: float = Field(..., description="Turbidity in NTU")
    TDS_mg_L: float = Field(..., description="Total dissolved solids in mg/L")
    Temperature_C: float = Field(..., description="Temperature in °C")

class WaterQualityOutput(BaseModel):
    Water_Quality_Index: float

@app.get("/health")
def health():
    return {"status": "ok", "model": "aquora_water_quality_ann_4sensor"}

@app.post("/predict", response_model=WaterQualityOutput)
def predict(data: WaterQualityInput):
    try:
        x = pd.DataFrame([{
            "pH": data.pH,
            "Turbidity_NTU": data.Turbidity_NTU,
            "TDS_mg_L": data.TDS_mg_L,
            "Temperature_C": data.Temperature_C
        }], columns=FEATURES)

        y = float(model.predict(x)[0])

        return {"Water_Quality_Index": y}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
