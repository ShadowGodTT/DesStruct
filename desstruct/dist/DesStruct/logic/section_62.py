from .section_61 import generate_section_61

def generate_section_62(excel_dict, defaults):
    return generate_section_61(excel_dict, defaults).replace("LEFT", "RIGHT") 