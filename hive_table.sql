CREATE TABLE amazon_reviews (
  review_id STRING,
  product_id STRING,
  star_rating INT,
  review_body STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;

LOAD DATA INPATH '/user/student/amazon_reviews/amazon_reviews.tsv' INTO TABLE amazon_reviews;
