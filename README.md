# Flask S3 Video Player

A simple Flask web application that streams videos from AWS S3 using presigned URLs for secure access.

## Features

- 🎥 Stream videos directly from AWS S3
- 🔒 Secure access using presigned URLs
- 🚀 Simple Flask web interface
- 📱 Responsive video player
- ⚡ Production-ready deployment scripts

## Files Overview

- `app.py` - Development version of the Flask application
- `app_prod.py` - Production version with enhanced logging and error handling
- `requirements.txt` - Python dependencies
- `deploy.sh` - EC2 deployment script
- `bucket-policy.json` - S3 bucket policy template
- `index.html` - Static HTML version (alternative)
- `load_test.py` - Load testing script for performance evaluation

## Setup

### Prerequisites

- Python 3.x
- AWS Account with S3 access
- AWS CLI configured or IAM role with S3 permissions

### Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure AWS credentials:
   ```bash
   aws configure
   ```

4. Update configuration in `app.py`:
   ```python
   BUCKET_NAME = 'your-bucket-name'
   VIDEO_KEY = 'your-video-file.mp4'
   REGION = 'your-aws-region'
   ```

### Running the Application

**Development:**
```bash
python app.py
```

**Production:**
```bash
python app_prod.py
```

The application will be available at `http://localhost:8080`

## AWS S3 Setup

1. Create an S3 bucket
2. Upload your video files
3. Configure bucket policy using `bucket-policy.json` (optional, for public access)
4. Ensure your AWS credentials have `s3:GetObject` permissions

## Deployment

### EC2 Deployment

Use the provided deployment script:

```bash
chmod +x deploy.sh
./deploy.sh
```

### Manual Deployment

1. Upload files to your server
2. Install Python dependencies
3. Configure AWS credentials
4. Run the production version

## Load Testing

Test your deployment performance:

```bash
python load_test.py
```

Update the `base_url` in the script to match your deployment URL.

## Security Notes

- Presigned URLs expire after 1 hour by default
- Configure appropriate S3 bucket policies
- Use IAM roles for EC2 deployments when possible
- Consider implementing authentication for production use

## License

MIT License - feel free to use and modify as needed.