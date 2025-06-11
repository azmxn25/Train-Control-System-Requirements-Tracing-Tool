from parser import load_requirements_from_csv
from traceability import build_traceability_matrix, export_to_json

def main():
    customer_reqs = load_requirements_from_csv('data/customer_requirements.csv', 'Customer')
    system_reqs = load_requirements_from_csv('data/system_requirements.csv', 'System')
    all_reqs = customer_reqs + system_reqs

    trace_matrix = build_traceability_matrix(all_reqs)
    export_to_json(trace_matrix, 'output/traceability_matrix.json')
    print("Traceability matrix exported to output/traceability_matrix.json")

if __name__ == '__main__':
    main()
