import importlib
from typing import Dict
import os
from defaults import DEFAULT_LINES

def get_section_files() -> list:
    """
    Get a sorted list of section files from the logic directory.
    Handles both single and double-digit section numbers.
    """
    logic_dir = os.path.dirname(os.path.abspath(__file__)) + "/logic"
    section_files = []
    
    for file in os.listdir(logic_dir):
        if file.startswith("section_") and file.endswith(".py"):
            # Extract section number
            section_num = file[8:-3]  # Remove 'section_' prefix and '.py' suffix
            try:
                # Convert to integer for proper sorting
                if section_num.isdigit():
                    section_files.append((int(section_num), file))
                elif section_num.endswith('a'):  # Handle special case like section_1a
                    base_num = int(section_num[:-1])
                    section_files.append((base_num + 0.5, file))  # Place after base number
            except ValueError:
                continue
    
    # Sort by section number and return filenames
    return [f[1] for f in sorted(section_files)]

def generate_in_file(data_dict: Dict[str, str]) -> str:
    """
    Generate the complete IN file content by calling all section generators.
    Returns the concatenated string of all section outputs.
    """
    sections = []
    
    # Get sorted list of section files
    section_files = get_section_files()
    
    # Import and call each section generator
    for section_file in section_files:
        try:
            # Import the section module
            module_name = f"logic.{section_file[:-3]}"  # Remove .py extension
            section_module = importlib.import_module(module_name)
            
            # Get the section number from the filename
            section_num = section_file[8:-3]  # Remove 'section_' prefix and '.py' suffix
            
            # Call the section's generate function with the correct name
            generate_func = getattr(section_module, f"generate_section_{section_num}")
            section_content = generate_func(data_dict, DEFAULT_LINES)
            sections.append(section_content)
            
        except ImportError:
            print(f"Warning: Could not import {module_name}")
        except AttributeError:
            print(f"Warning: {module_name} does not have generate_section_{section_num} function")
        except Exception as e:
            print(f"Error in {module_name}: {str(e)}")
    
    # Join all sections with newlines
    return "\n".join(sections) 