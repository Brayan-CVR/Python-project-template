class ParametersError(TypeError):
    """_summary_

    Args:
        Exception (_type_): _description_
    """

    def __init__(
        self,
        original_error=None,
        message="Error at input parameters type.",
    ):
        """_summary_

        Args:
            original_error (_type_, optional): _description_. Defaults to None.
            message (str, optional): _description_. Defaults to "Unexpected error getting the Python information.".
        """
        self.original_error = original_error  # Save the original exception
        self.message = message
        super().__init__(f"{self.message} Error original: {str(self.original_error)}.\n")
