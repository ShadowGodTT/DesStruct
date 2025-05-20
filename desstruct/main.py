import csv
from pathlib import Path
from generator import generate_in_file

def read_specifications(csv_path: str) -> dict:
    """
    Read Infinit Excel.csv and convert it to a dictionary.
    Returns a dictionary where keys are Parameters and values are Values.
    Handles whitespace in headers.
    """
    data_dict = {}
    with open(csv_path, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        # Normalize headers
        reader.fieldnames = [h.strip() for h in reader.fieldnames]
        print(f"CSV Headers: {reader.fieldnames}")  # Debug print
        for row in reader:
            param = row.get('Parameter') or row.get('Parameter'.strip())
            value = row.get('Value') or row.get('Value'.strip())
            if param is not None:
                data_dict[param.strip()] = value.strip() if value is not None else ''
    return data_dict

def main():
    # Get the directory where main.py is located
    current_dir = Path(__file__).parent
    
    # Define input and output file paths
    csv_path = current_dir / 'Infinit Excel.csv'
    output_path = current_dir / 'DESCTRL.IN'
    
    # Read specifications and generate IN file
    try:
        data_dict = read_specifications(csv_path)
        in_content = generate_in_file(data_dict)
        
        # Write the generated content to DESCTRL.IN
        with open(output_path, 'w') as f:
            f.write(in_content)
            
        print(f"Successfully generated {output_path}")
        
    except FileNotFoundError:
        print(f"Error: {csv_path} not found")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 