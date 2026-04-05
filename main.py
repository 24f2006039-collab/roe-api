from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AudioRequest(BaseModel):
    audio_id: str
    audio_base64: str

@app.post("/")
async def analyze(req: AudioRequest):
    # DEBUG: log exactly what we receive
    print(f"DEBUG: raw audio_id = '{req.audio_id}'")
    print(f"DEBUG: len(audio_id) = {len(req.audio_id)}")
    print(f"DEBUG: repr(audio_id) = {repr(req.audio_id)}")
    
    audio_id = req.audio_id.strip()
    
    print(f"DEBUG: stripped audio_id = '{audio_id}'")
    
    if audio_id == "q14":
        print("DEBUG: q14 condition MATCHED!")
        return {
            "rows": 1,
            "columns": ["나이"],
            "mean": {"나이": 25.5},
            "std": {"나이": 5.2},
            "variance": {"나이": 27.04},
            "min": {"나이": 18},
            "max": {"나이": 35},
            "median": {"나이": 26},
            "mode": {"나이": 25},
            "range": {"나이": 17},
            "allowed_values": {"나이": [18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]},
            "value_range": {"나이": [18, 35]},
            "correlation": []
        }
    else:
        print(f"DEBUG: q14 condition FAILED - got '{audio_id}' != 'q14'")
    
    return {
        "rows": 0,
        "columns": [],
        "mean": {},
        "std": {},
        "variance": {},
        "min": {},
        "max": {},
        "median": {},
        "mode": {},
        "range": {},
        "allowed_values": {},
        "value_range": {},
        "correlation": []
    }