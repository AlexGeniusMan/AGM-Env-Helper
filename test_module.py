from agm_env_helper.agm_env_helper.env_helper import get_env_var
import pytest

DEBUG = True


def test_env_helper():
    with open('.env', 'w') as file:
        file.write("""
VARIABLE_STR=String
VARIABLE_INT=1234
VARIABLE_FLOAT=1234.5678
""")

    with pytest.raises(ValueError):
        get_env_var(str, '', DEBUG)

    with pytest.raises(ValueError):
        get_env_var(str, 'VARIABLE_WITH_WRONG_NAME', DEBUG)

    with pytest.raises(ValueError):
        get_env_var(int, 'VARIABLE_STR', DEBUG)

    with pytest.raises(ValueError):
        get_env_var(float, 'VARIABLE_STR', DEBUG)

    with pytest.raises(TypeError):
        get_env_var(bool, 'VARIABLE_STR', DEBUG)

    assert get_env_var(int, 'VARIABLE_INT', DEBUG) == 1234
    assert type(get_env_var(int, 'VARIABLE_INT', DEBUG)) == int

    assert get_env_var(float, 'VARIABLE_FLOAT', DEBUG) == 1234.5678
    assert type(get_env_var(float, 'VARIABLE_FLOAT', DEBUG)) == float
