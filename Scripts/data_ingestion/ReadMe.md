# 🛢️ S3 Data Ingestion Simulation

This folder contains a **production-style Python script** that shows how data would be downloaded from an Amazon S3 bucket in a real-world data engineering pipeline.

Although this is a student project, the script demonstrates professional practices you'd use in production when fetching files securely from cloud storage.

---

## 📄 File: `download_from_s3.py`

```python
"""
NOTE: This is a production-style example of how data would be downloaded from S3.
In this student project, files are already placed manually in `data/Input_data/`.
"""

import os
import boto3
from dotenv import load_dotenv

# ✅ Load credentials securely
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
BUCKET_NAME = "my-demo-bucket"
PREFIX = "raw-files/"

# ✅ Configure S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

# ✅ Download all files under a specific prefix (folder)
def download_s3_folder(bucket_name, prefix, local_dir):
    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
        for obj in page.get("Contents", []):
            file_key = obj["Key"]
            if file_key.endswith("/"):  # skip folders
                continue

            file_path = os.path.join(local_dir, os.path.basename(file_key))
            print(f"Downloading {file_key} → {file_path}")
            s3.download_file(bucket_name, file_key, file_path)

# ✅ Destination directory
local_dir = "data/Input_data"
os.makedirs(local_dir, exist_ok=True)

# ✅ Run
download_s3_folder(BUCKET_NAME, PREFIX, local_dir)
