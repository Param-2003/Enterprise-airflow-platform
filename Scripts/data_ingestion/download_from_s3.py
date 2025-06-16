import boto3
import os

# Define S3 config (normally you'd fetch these from env vars)
AWS_ACCESS_KEY = 'YOUR_ACCESS_KEY'
AWS_SECRET_KEY = 'YOUR_SECRET_KEY'
S3_BUCKET_NAME = 'your-bucket-name'
S3_PREFIX = 'raw_data/'  # folder inside your bucket (optional)

LOCAL_DEST = 'data/Input_data'

def download_files_from_s3():
    os.makedirs(LOCAL_DEST, exist_ok=True)

    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )

    response = s3.list_objects_v2(Bucket=S3_BUCKET_NAME, Prefix=S3_PREFIX)

    if 'Contents' not in response:
        print("❌ No files found in specified S3 location.")
        return

    for obj in response['Contents']:
        key = obj['Key']
        if key.endswith('/'):  # skip folders
            continue

        file_name = key.split('/')[-1]
        local_path = os.path.join(LOCAL_DEST, file_name)

        print(f"⬇️  Downloading {key} to {local_path}")
        s3.download_file(S3_BUCKET_NAME, key, local_path)

    print("✅ All files downloaded.")

if __name__ == '__main__':
    download_files_from_s3()
