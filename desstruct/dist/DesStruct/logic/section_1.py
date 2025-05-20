def generate_section_1(excel_dict, defaults):
    """
    Generate Section 1 of the DesStruct IN file.
    This section contains job description information.
    
    Args:
        excel_dict (dict): Dictionary containing Excel data
        defaults (dict): Dictionary containing default values
        
    Returns:
        str: Formatted section 1 text
    """
    job_number = excel_dict.get("Proposal Id", defaults.get("Job Number", "0000"))
    building_name = excel_dict.get("Project", defaults.get("Building Name", "Unnamed"))
    engineer = excel_dict.get("Design Engineer", defaults.get("Design Engineer", "N/A"))
    
    return f"""*(1) JOB DESCRIPTION:
    Job #: {job_number}
    Building Name: {building_name}
    Design Engineer: {engineer}""" 