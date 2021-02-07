import pulumi, os, mimetypes
import pulumi_aws as aws

config = pulumi.Config()
site_dir = config.require("siteDir") # requiring the config variable

bucket = aws.s3.Bucket("my-bucket",
    website={
        "index_document": "index.html"
    }
)
# bucket = aws.s3.Bucket("my-bucket", bucket="this is a the name that AWS bucket is going to have")

for file in os.listdir(site_dir):
    filePath = os.path.join(site_dir, file) # getting the html from the folder
    mime_type, _ = mimetypes.guess_type(filePath)# guess the mimetype of the file, python library
    obj = aws.s3.BucketObject(file, # making the bucket object
        bucket=bucket.id,
        source=pulumi.FileAsset(filePath),
        acl="public-read", # making it so that public can see it
        content_type = mime_type
    )

pulumi.export("bucket_name", bucket.id) # this is to show the output
pulumi.export("bucket_endpoint", pulumi.Output.concat("http://", bucket.website_endpoint)) # this is way to interpolation of string value 