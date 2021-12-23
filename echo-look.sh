# ! /bin/bash
json=$(aws rekognition detect-text --image "S3Object-(Bucket-echo-look,Name=StyleCheckAge3.png}" --region "us-east-1")
echo $json > "alexa.json"
