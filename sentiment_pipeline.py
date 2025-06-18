from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline
from pyspark.sql.functions import when

spark = SparkSession.builder \
    .appName("Sentiment Analysis") \
    .enableHiveSupport() \
    .getOrCreate()

df = spark.sql("SELECT review_body, star_rating FROM amazon_reviews WHERE star_rating IN (1,2,4,5)")
df = df.withColumn("label", when(df.star_rating >= 4, 1).otherwise(0))

tokenizer = Tokenizer(inputCol="review_body", outputCol="words")
remover = StopWordsRemover(inputCol="words", outputCol="filtered")
hashingTF = HashingTF(inputCol="filtered", outputCol="rawFeatures", numFeatures=10000)
idf = IDF(inputCol="rawFeatures", outputCol="features")

lr = LogisticRegression(featuresCol="features", labelCol="label")
pipeline = Pipeline(stages=[tokenizer, remover, hashingTF, idf, lr])

train, test = df.randomSplit([0.8, 0.2], seed=42)
model = pipeline.fit(train)
predictions = model.transform(test)
predictions.select("label", "prediction", "probability").show(10)

spark.stop()
