import logging

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

beam_options = PipelineOptions()

with  beam.Pipeline() as p:
  rows = p | "Read blablabl" >> beam.io.ReadFromText()


def run(argv=None):
  pass


if __name__ == "__main__":
  logging.getLogger().setLevel(logging.INFO)
  run()
