# Face-Model: AWS Facial Recognition

This project demonstrates facial detection and comparison using AWS Rekognition. Images are stored in an S3 bucket and analyzed via Python.

## Features

- **Face Detection**: Detect faces in an image and return attributes like confidence, emotions, and smile detection.
- **Face Comparison**: Compare two images to find matching faces and calculate similarity.

## Requirements

- Python 3.7 or higher
- AWS CLI installed and configured
- An active AWS account with access to Rekognition and S3

## Why Sensitive Information Is Not Included in This Repository

This repository does **not** include sensitive information such as:

1. **AWS S3 Bucket Names**: The bucket name where your images are stored has been replaced with placeholders (e.g., `your-bucket-name`) to ensure the security of your AWS resources.
2. **Image File Paths**: The paths to images (e.g., `source_image.jpg`, `target_image.jpg`) have been replaced with placeholders to protect potentially personal or private image data.
3. **AWS Credentials**: No AWS Access Key ID or Secret Access Key is hardcoded in the code. Instead:
   - AWS credentials should be configured via the AWS CLI or stored in environment variables (e.g., `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`).
   - This prevents unauthorized access to your AWS account if the repository is made public.

By excluding these details, the repository remains safe and compliant with best practices for protecting sensitive data.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Face-Model.git
   cd Face-Model
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your AWS CLI:
   ```bash
   aws configure
   ```
   Ensure you use environment variables or AWS CLI credentials without hardcoding them into the code.

4. Upload your images to an S3 bucket:
   ```bash
   aws s3 mb s3://your-bucket-name
   aws s3 cp ./source_image.jpg s3://your-bucket-name/
   aws s3 cp ./target_image.jpg s3://your-bucket-name/
   ```

5. Replace placeholders in `main.py`:
   - **`your-bucket-name`**: Replace with your S3 bucket name.
   - **`source_image.jpg`**: Replace with your source image file name.
   - **`target_image.jpg`**: Replace with your target image file name.

## Usage

1. Run the project:
   ```bash
   python main.py
   ```

2. The script will detect faces in the source image and compare it with the target image.

## Notes

- **Do not hardcode sensitive information**: Use AWS CLI or environment variables for your credentials.
- Your AWS IAM user must have the `AmazonRekognitionFullAccess` and `AmazonS3FullAccess` policies attached.

## Contributing

Feel free to open issues or submit pull requests to enhance this project.
