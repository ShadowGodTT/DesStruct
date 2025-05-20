"""
Default values for IN file sections when the corresponding parameter is 'NA' in the CSV.
Each key corresponds to a parameter name, and the value is the default IN file line to use.
"""

DEFAULT_LINES = {
    # Example defaults - replace with your actual default values
    "PARAMETER_01": "DEFAULT_LINE_01",
    "PARAMETER_02": "DEFAULT_LINE_02",
    # Add more defaults as needed
}

def get_default_line(parameter: str) -> str:
    """
    Get the default IN file line for a given parameter.
    Returns the default line if it exists, otherwise returns an empty string.
    """
    return DEFAULT_LINES.get(parameter, "") 