from pyspark.sql import SQLContext
from pyspark.ml.feature import StandardScaler
from pyspark.ml.clustering import KMeans, KMeansModel
from pyspark.mllib.linalg import DenseVector

def read_from_db(sc, segments):
    """Read data from database into Spark DataFrame."""
    pass

def convert_df(sc, data):
    """Transform dataframe into the format that can be used by MLlib."""
    sqlContext = SQLContext(sc)
    input_data = data.map(lambda x: (x[0], DenseVector(x[1:])))
    df = sqlContext.createDataFrame(input_data, ["id", "features"])
    return df

def rescale_df(data):
    """Rescale the data."""
    standardScaler = StandardScaler(inputCol="features", outputCol="features_scaled")
    scaler = standardScaler.fit(data)
    scaled_df = scaler.transform(data)
    return scaled_df

def assign_cluster(data):
    """Train kmeans on rescaled data and then label the rescaled data."""
    kmeans = KMeans(k=2, seed=1, featuresCol="features_scaled", predictionCol="label")
    model = kmeans.fit(data)
    label_df = model.transform(data)
    return label_df

def save_to_hdfs(sc):
    """Save results to HDFS."""
    pass

if __name__ == "__main__":
    sc = SparkContext()

    sc.stop()
