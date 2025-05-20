from typing import Dict
from ..defaults import get_default_line

def generate_section(data_dict: Dict[str, str]) -> str:
    """
    Generate section 02 of the IN file.
    This is a sample section - replace with your actual section 02 logic.
    """
    # Example parameter names - replace with your actual parameters
    param1 = data_dict.get("SECTION_02_PARAM1", "NA")
    param2 = data_dict.get("SECTION_02_PARAM2", "NA")
    param3 = data_dict.get("SECTION_02_PARAM3", "NA")
    
    # Use default values if parameters are "NA"
    if param1 == "NA":
        param1 = get_default_line("SECTION_02_PARAM1")
    if param2 == "NA":
        param2 = get_default_line("SECTION_02_PARAM2")
    if param3 == "NA":
        param3 = get_default_line("SECTION_02_PARAM3")
    
    # Format the section content
    section_content = f"""* Section 02 - Another Sample Section
{param1}
{param2}
{param3}
"""
    return section_content 