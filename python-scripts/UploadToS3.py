import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

data = open('C:/Users/rganjare/Desktop/EMI.zip', 'rb')
s3.Bucket('mycicdcopycodebucket').put_object(Key='EMI.zip', Body=data)