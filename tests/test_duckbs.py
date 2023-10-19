# test on the code in examples folder

import os
import sys

import numpy as np
import pandas as pd
import polars as pl
import pyarrow as pa
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


def test_polars(con):
    polars_df = pl.DataFrame({"a": [42]})
    con.register("polars_df", polars_df)
    result = con.execute("SELECT * FROM polars_df").fetchall()
    assert result == [(42,)]


def test_arrow(con):
    arrow_table = pa.Table.from_pydict({"a": [42]})
    con.register("arrow_table", arrow_table)
    result = con.execute("SELECT * FROM arrow_table").fetchall()
    assert result == [(42,)]


def test_arrow_table(con):
    arrow_table = pa.Table.from_pydict({"a": [42]})
    con.register("arrow_table", arrow_table)
    result = con.execute("SELECT * FROM arrow_table").fetchall()
    assert result == [(42,)]
