from agm_env_helper.agm_env_helper.env_helper import get_env_var
import pytest

DEBUG = True


def test_env_helper():
    with open('.env', 'w') as file:
        file.write("""
VARIABLE_STR=String
VARIABLE_INT=1234
VARIABLE_FLOAT=1234.5678
VARIABLE_BOOL_1=True
VARIABLE_BOOL_2=true
VARIABLE_BOOL_3=1
VARIABLE_BOOL_4=False
VARIABLE_BOOL_5=false
VARIABLE_BOOL_6=0
""")

    with pytest.raises(ValueError):
        get_env_var(str, '', DEBUG)

    with pytest.raises(ValueError):
        get_env_var(str, 'VARIABLE_WITH_WRONG_NAME', DEBUG)

    with pytest.raises(ValueError):
        get_env_var(int, 'VARIABLE_STR', DEBUG)

    with pytest.raises(ValueError):
        get_env_var(float, 'VARIABLE_STR', DEBUG)

    # with pytest.raises(TypeError):
    #     get_env_var(bool, 'VARIABLE_STR', DEBUG)

    with pytest.raises(TypeError):
        get_env_var('lol', 'VARIABLE_STR', DEBUG)

    assert get_env_var(int, 'VARIABLE_INT', DEBUG) == 1234
    assert type(get_env_var(int, 'VARIABLE_INT', DEBUG)) == int

    assert get_env_var(float, 'VARIABLE_FLOAT', DEBUG) == 1234.5678
    assert type(get_env_var(float, 'VARIABLE_FLOAT', DEBUG)) == float

    assert get_env_var(bool, 'VARIABLE_BOOL_1', 1) is True
    assert type(get_env_var(bool, 'VARIABLE_BOOL_1', 1)) == bool

    assert get_env_var(bool, 'VARIABLE_BOOL_2', 1) is True
    assert type(get_env_var(bool, 'VARIABLE_BOOL_2', 1)) == bool

    assert get_env_var(bool, 'VARIABLE_BOOL_3', 1) is True
    assert type(get_env_var(bool, 'VARIABLE_BOOL_3', 1)) == bool

    assert get_env_var(bool, 'VARIABLE_BOOL_4', 1) is False
    assert type(get_env_var(bool, 'VARIABLE_BOOL_4', 1)) == bool

    assert get_env_var(bool, 'VARIABLE_BOOL_5', 1) is False
    assert type(get_env_var(bool, 'VARIABLE_BOOL_5', 1)) == bool

    assert get_env_var(bool, 'VARIABLE_BOOL_6', 1) is False
    assert type(get_env_var(bool, 'VARIABLE_BOOL_6', 1)) == bool
