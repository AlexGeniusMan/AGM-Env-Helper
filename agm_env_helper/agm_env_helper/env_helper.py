import os

from dotenv import load_dotenv

import time

load_dotenv()


def print_var(var_name, var_value):
    # if
    print(var_name, var_value)


def get_env_var(var_type, var_name, debug):
    """
    Get variable from environment

    :param var_type: str, int or float
    :param var_name: environment variable name, string
    :param debug: decide to print environment variable value to output or not, bool
    :return: environment variable value
    """

    var_value = os.getenv(var_name)
    if var_value is None:
        raise ValueError(f"ERROR: {var_name} env variable type is None.")

    if debug:
        if len(var_name) > 39:
            var_name_for_print = var_name[0:18] + '...' + var_name[-18:]
        else:
            var_name_for_print = var_name
        if len(var_value) > 39:
            var_value_for_print = var_value[0:18] + '...' + var_value[-18:]
        else:
            var_value_for_print = var_value
        print(f"{'{:39s}'.format(var_name_for_print)} {var_value_for_print}")

    try:
        if var_type not in (str, int, float):
            raise TypeError
        return var_type(var_value)
    except ValueError:
        raise ValueError(
            f"ERROR: {var_name} env variable type is wrong. Type must be {var_type}. Current value: '{var_value}'")
    except TypeError:
        raise TypeError(
            f"ERROR: 'var_name' parameter is wrong. Parameter must be <class 'str'>, <class 'int'> or <class 'float'>.")
