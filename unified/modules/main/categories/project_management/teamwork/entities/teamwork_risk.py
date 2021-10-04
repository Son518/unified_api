from dataclasses import dataclass

@dataclass
class TeamworkRisk():

    id: str = None
    source: str = None
    probability: str = None
    probability_value: str = None
    impact: str = None
    impact_value: str = None
    result: str = None
    impact_cost: str = None
    impact_performance: str = None
    impact_schedule: str = None
    mitigation_plan: str = None
    status: str = None
    project_id: str = None
    created_date: str = None
    updated_date: str = None