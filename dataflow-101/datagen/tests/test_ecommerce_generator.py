import logging
import datetime
import unittest
import json
import os
import re
from faker_schema.faker_schema import FakerSchema
from google.cloud import bigquery as bq
from google.cloud.bigquery_storage import BigQueryWriteAsyncClient


class MyTestCase(unittest.TestCase):

  @classmethod
  def setUpClass(cls) -> None:
    cls.bq_write_client = BigQueryWriteAsyncClient()

  def setUp(self):

    # Note changed default for schema_file for ease of testing.
    dir_path = os.path.dirname(os.path.realpath(''))
    schema_path = os.path.join(dir_path, 'resources')

  def test_something(self):
    self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
  unittest.main()
