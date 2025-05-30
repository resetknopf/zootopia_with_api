from typing import Any, Dict, List
from data_fetcher import fetch_data


def load_template(file_path: str) -> str:
    """Load HTML template from a file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def serialize_animal(animal: Dict[str, Any]) -> str:
    """Convert a single animal's data into an HTML snippet."""
    name = animal.get("name", "Unknown")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    animal_type = characteristics.get("type")
    distinctive_feature = characteristics.get("distinctive_feature")
    locations = animal.get("locations", [])

    animal_data = '<li class="cards__item">'
    animal_data += f'<div class="card__title">{name}</div>'
    animal_data += '<ul>'
    if diet:
        animal_data += f'<li class="card__text"><strong>Diet:</strong> {diet}</li>'
    if locations:
        animal_data += f'<li class="card__text"><strong>Location:</strong> {locations[0]}</li>'
    if animal_type:
        animal_data += f'<li class="card__text"><strong>Type:</strong> {animal_type}</li>'
    if distinctive_feature:
        animal_data += (
            f'<li class="card__text"><strong>Distinctive feature:</strong> '
            f'{distinctive_feature}</li>'
        )
    animal_data += '</ul></li>'

    return fix_encoding_issues(animal_data)


def fix_encoding_issues(text: str) -> str:
    """Fix common encoding issues in the text."""
    return text.replace("’", "'")


def write_template(text: str) -> bool:
    """Write the final HTML content to a file."""
    try:
        with open("animals.html", "w", encoding="utf-8") as handle:
            handle.write(text)
        return True
    except Exception as e:
        print(f"Failed to write file: {e}")
        return False


def main() -> None:
    """Main entry point of the script."""
    animal_name = input("Please enter an animal name: ").strip().lower()
    animals = fetch_data(animal_name)

    if not animals:
        output = f'<h2>The animal "{animal_name}" does not exist.</h2>'
    else:
        output = ''.join(serialize_animal(entry) for entry in animals)

    template = load_template("animals_template.html")
    final_output = template.replace("__REPLACE_ANIMALS_INFO__", output)

    if write_template(final_output):
        print("File written successfully")
    else:
        print("Error writing file")


if __name__ == "__main__":
    main()
