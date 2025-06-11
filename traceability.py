from typing import List, Dict
from models import Requirement
import json
import os

def build_traceability_matrix(requirements: List[Requirement]) -> Dict[str, List[str]]:
    trace_matrix = {}
    id_to_req = {req.id: req for req in requirements}
    for req in requirements:
        if req.parent_id and req.parent_id in id_to_req:
            trace_matrix.setdefault(req.parent_id, []).append(req.id)
    return trace_matrix

def export_to_json(matrix: Dict[str, List[str]], output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(matrix, f, indent=4)
