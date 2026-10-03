import boto3

BUCKET_NAME = "ai-resume-analyzer-2026-yourname"
REGION = "ap-south-1"

s3 = boto3.client(
    "s3",
    region_name=REGION
)


def upload_resume(file, filename):

    s3.upload_fileobj(
        file,
        BUCKET_NAME,
        filename,
        ExtraArgs={
            "ContentType": "application/pdf"
        }
    )

    return f"s3://{BUCKET_NAME}/{filename}"


def list_resumes():

    response = s3.list_objects_v2(
        Bucket=BUCKET_NAME
    )

    files = []

    if "Contents" in response:

        for item in response["Contents"]:
            files.append(item["Key"])

    return files


if __name__ == "__main__":

    print("AWS S3 connection successful!")

    files = list_resumes()

    print("Files in S3 bucket:")

    for file in files:
        print(file)
def upload_resume(file, filename):

    print("Uploading to S3:", filename)
    print("Bucket:", BUCKET_NAME)

    s3.upload_fileobj(
        file,
        BUCKET_NAME,
        filename,
        ExtraArgs={
            "ContentType": "application/pdf"
        }
    )

    print("Upload successful!")

    return f"s3://{BUCKET_NAME}/{filename}"