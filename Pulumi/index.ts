import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import * as fs from "fs";

// Create an AWS resource (S3 Bucket)
// Export the name of the bucket

const bucket = new aws.s3.Bucket("my-bucket", {
    website: {
        indexDocument: "index.html",
    },
});
export const bucketName = bucket.id;

const bucketObject = new aws.s3.BucketObject("index.html", {
    acl: "public-read",
    contentType: "text/html",
    bucket: bucket,
    content: fs.readFileSync("site/index.html").toString(),
});

export const bucketEndpoint = pulumi.interpolate`http://${bucket.websiteEndpoint}`;
