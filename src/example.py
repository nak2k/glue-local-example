from pyspark import SparkContext
from awsglue.context import GlueContext

import common.debug  # noqa: F401

sc = SparkContext()
glueContext = GlueContext(sc)

print("Hello, World!")
