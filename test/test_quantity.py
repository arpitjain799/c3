"""Unit tests for Quantity class"""

import hjson
from c3.c3objs import Quantity

amp = Quantity(value=0.0, min_val=-1.0, max_val=+1.0, unit="V")
amp_dict = {
    'value': 0.0,
    'min_val': -1.0,
    'max_val': 1.0,
    'unit': 'V',
    'symbol': '\\alpha'
}

gate_time = Quantity(
    value=5.3246e-9,
    min_val=2e-9,
    max_val=10e-9,
    unit="s",
    symbol=r"t_g"
)

matrix = Quantity(
    value=[[0, 1], [1, 0]],
    min_val=[[0, 0], [0, 0]],
    max_val=[[1, 1], [1, 1]],
    unit="",
    symbol=r"M"
)

def test_qty_asdict() -> None:
    assert amp.asdict() == amp_dict


def test_qty_write_cfg() -> None:
    print(hjson.dumps(amp.asdict()))


def test_qty_read_cfg() -> None:
    assert Quantity(**amp_dict).asdict() == amp.asdict()


def test_qty_str() -> None:
    assert str(gate_time) == "5.325 ns "


def test_qty_set() -> None:
    gate_time.set_value(7e-9)
    assert gate_time.get_value() == 7e-9


def test_qty_max() -> None:
    gate_time.set_opt_value(1.0)
    assert gate_time.get_value() == 10e-9


def test_qty_min() -> None:
    gate_time.set_opt_value(-1.0)
    assert gate_time.get_value() == 2e-9


def test_qty_get_opt() -> None:
    gate_time.set_value(6e-9)
    assert gate_time.get_opt_value() < 1e-15


def test_qty_matrix_str() -> None:
    assert str(matrix) == '0.000  1.000  1.000  0.000  '


def test_qty_matrix_set() -> None:
    matrix.set_value(
        [[1.0, 0.0],
         [0.0, 1.0]]
    )
    assert (matrix.numpy() == [[1, 0], [0, 1]]).all()


def test_qty_matrix_set_opt() -> None:
    assert (matrix.get_opt_value() == [1.,  -1.,  -1., 1.]).all()
