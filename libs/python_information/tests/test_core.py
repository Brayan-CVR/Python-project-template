import pytest
from python_information import print_details_about_python, ParametersError


class TestPythonInformation:
    """_summary_
    """    
    def test_valid_usage(self):
        """_summary_
        """        
        assert print_details_about_python(detailed=True) is None
        assert print_details_about_python(detailed=False) is None
        assert print_details_about_python() is None

    def test_invalid_usage(self):
        """_summary_
        """        
        with pytest.raises(ParametersError):
            print_details_about_python(detailed="Hola")

        with pytest.raises(ParametersError):
            print_details_about_python(detailed="1.3256")

        with pytest.raises(ParametersError):
            print_details_about_python(detailed=3.1416)
