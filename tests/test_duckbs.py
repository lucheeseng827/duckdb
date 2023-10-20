# test on the code in examples folder

import os
import sys

import numpy as np
import pandas as pd
import pytest

from duckdb import connect


@pytest.fixture(scope="module")
def con():
    con = connect()
    yield con
    con.close()


def test_pandas(con):
    pandas_df = pd.DataFrame({"a": [42]})
    con.register("pandas_df", pandas_df)
    result = con.execute("SELECT * FROM pandas_df").fetchall()
    assert result == [(42,)]
