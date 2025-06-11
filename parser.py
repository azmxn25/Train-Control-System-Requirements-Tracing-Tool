import csv
from typing import List
from models import Requirement


def normalize_parent_id(value: str) -> str:
    """
    Normalize the parent ID value from the CSV to either a valid string or None.
    """
    if not value:
        return None
    normalized = value.strip().lower()
    return None if normalized in ('', 'null', 'none') else value.strip()


def load_requirements_from_csv(filepath: str, category: str) -> List[Requirement]:
    """
    Loads and parses requirements from a CSV file into a list of Requirement objects.

    :param filepath: Path to the CSV file.
    :param category: Category label (e.g., 'Customer', 'System').
    :return: List of parsed Requirement objects.
    """
    requirements = []

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row_num, row in enumerate(reader, start=1):
            try:
                req_id = row['ID'].strip()
                description = row['Description'].strip()
                parent_id = normalize_parent_id(row.get('ParentID', ''))

                requirement = Requirement(
                    id=req_id,
                    description=description,
                    parent_id=parent_id,
                    category=category
                )
                requirements.append(requirement)

            except KeyError as e:
                print(f"[ERROR] Missing expected column in row {row_num}: {e}")
            except Exception as e:
                print(f"[ERROR] Failed to parse row {row_num}: {e}")

    return requirements
