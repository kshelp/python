# pyspark 설치
# D:\dev\workspace\python>pip install pyspark

from operator import add
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .getOrCreate()

    lines = spark.read.text("test.txt").rdd.map(lambda r: r[0])
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)
    output = counts.collect()
    
    for (word, count) in output:
        print("%s: %i" % (word, count))

    spark.stop()
