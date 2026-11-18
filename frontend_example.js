# Example frontend call

const payload = {
  pH: 7.0,
  Turbidity_NTU: 2.0,
  TDS_mg_L: 300.0,
  Temperature_C: 22.0
};

const response = await fetch("http://localhost:8000/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(payload)
});

const result = await response.json();
// result.Water_Quality_Index
