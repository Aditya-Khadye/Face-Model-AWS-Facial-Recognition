import boto3
import os

# AWS Rekognition client
rekognition = boto3.client('rekognition', region_name='us-east-1')

# Replace these with your S3 bucket name and image file paths
exampleBUCKET_NAME = "your-bucket-name"  # Replace with your S3 bucket name
exampleBUCKET_NAMESOURCE_IMAGE = "source_image.jpg"  # Replace with your source image filename
exampleBUCKET_NAMETARGET_IMAGE = "target_image.jpg"  # Replace with your target image filename


def detect_faces(bucket, image):
    """
    Detects faces in the specified image using AWS Rekognition.
    """
    try:
        response = rekognition.detect_faces(
            Image={'S3Object': {'Bucket': bucket, 'Name': image}},
            Attributes=['ALL']
        )
        print(f"Detected faces in {image}:")
        for face in response['FaceDetails']:
            print(f"- Confidence: {face['Confidence']:.2f}%")
            print(f"  Smile: {face['Smile']['Value']} (Confidence: {face['Smile']['Confidence']:.2f}%)")
            emotions = [e['Type'] for e in face['Emotions'] if e['Confidence'] > 75]
            print(f"  Emotions: {', '.join(emotions) if emotions else 'None'}")
            print("-" * 30)
    except Exception as e:
        print(f"Error detecting faces: {e}")


def compare_faces(bucket, source_image, target_image):
    """
    Compares two faces using AWS Rekognition.
    """
    try:
        response = rekognition.compare_faces(
            SourceImage={'S3Object': {'Bucket': bucket, 'Name': source_image}},
            TargetImage={'S3Object': {'Bucket': bucket, 'Name': target_image}}
        )
        print(f"Comparing {source_image} and {target_image}:")
        for match in response['FaceMatches']:
            print(f"- Similarity: {match['Similarity']:.2f}%")
            print(f"  Bounding Box: {match['Face']['BoundingBox']}")
            print("-" * 30)

        if not response['FaceMatches']:
            print("No matching faces found.")
    except Exception as e:
        print(f"Error comparing faces: {e}")


if __name__ == "__main__":
    # Ensure AWS credentials are configured
    if "AWS_ACCESS_KEY_ID" not in os.environ or "AWS_SECRET_ACCESS_KEY" not in os.environ:
        print("Error: AWS credentials not found. Set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.")
        exit(1)

    # Run facial detection and comparison
    print("Running facial recognition...\n")
    detect_faces(exampleBUCKET_NAME, exampleBUCKET_NAMESOURCE_IMAGE)
    compare_faces(exampleBUCKET_NAME, exampleBUCKET_NAMESOURCE_IMAGE, exampleBUCKET_NAMETARGET_IMAGE)