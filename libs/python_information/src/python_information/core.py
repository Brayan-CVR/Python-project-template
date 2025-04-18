import sys
import platform

# Custom exceptions.
from .exceptions import ParametersError


def print_details_about_python(detailed: bool = False) -> None:
    """_summary_

    Args:
        detailed (bool, optional): _description_. Defaults to False.

    Raises:
        ParametersError: _description_
    """    
    # Input variables validation.
    if not isinstance(detailed, bool):
        raise ParametersError(original_error=TypeError)

    # Main process.
    print(f"Python Version: {sys.version.split()[0]}")
    print(f"Installation path: {sys.executable}")

    if detailed:
        print("\nDetailed information:")
        print(f"Compiler: {platform.python_compiler()}.")
        print(f"Implementation: {platform.python_implementation()}.")
        print(f"Build: {platform.python_build()}.")
        print(f"System: {platform.system()} {platform.release()}.\n")
