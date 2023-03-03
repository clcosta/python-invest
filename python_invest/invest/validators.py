from datetime import date
from python_invest.const import PRODUCT_LIST, TIME_FRAME_LIST


def validate_args(func):
    """
    Validate the arguments passed in a function used inside a Invest class.
    The arguments the wrapper expected to validate:
        - product
        - from_date
        - to_date
        - time_frame
    """

    def wrapper(*args, **kwargs):
        product, from_date, to_date, time_frame = kwargs.values()
        if product.lower() not in PRODUCT_LIST:
            raise ValueError(
                f'Product "{product}" not in accepted. Please select a product based on {" or ".join(PRODUCT_LIST)}.'
            )
        if time_frame.lower() not in TIME_FRAME_LIST:
            raise ValueError(
                f'Time frame "{time_frame}" not in accepted. Please select a based on {" or ".join(TIME_FRAME_LIST)}.'
            )
        if not isinstance(from_date, (str, date)):
            raise TypeError(
                f'Argument from_date must be a string containning a date in format m/d/Y or date. Got a "{type(from_date)}"'
            )
        if not isinstance(to_date, (str, date)):
            raise TypeError(
                f'Argument to_date must be a string containning a date in format m/d/Y or date. Got a "{type(from_date)}"'
            )
        return func(*args, **kwargs)

    return wrapper
