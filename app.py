from fastapi import FastAPI
from geos.mfo.orchestrator import MissionFlowOrchestrator
from geos.cpl.registry import ToolRegistry
from geos.observability.metrics import MetricsCollector

app = FastAPI()

registry = ToolRegistry()
metrics = MetricsCollector()
orchestrator = MissionFlowOrchestrator(
    tool_registry=registry,
    metrics=metrics
)

@app.get("/")
def root():
    return {"status": "GEOS is running"}

@app.post("/mission/run")
def run_mission(mission: dict):
    return orchestrator.run(mission)
