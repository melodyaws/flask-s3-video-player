import boto3
from flask import Flask, render_template_string

app = Flask(__name__)

# Configure these
BUCKET_NAME = 'aaatesttttting'
VIDEO_KEY = 'demo.MP4'
REGION = 'us-east-1'

session = boto3.Session(profile_name='ab3_profile')
s3 = session.client('s3', region_name=REGION)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head><title>S3 Video Player</title></head>
<body>
    <h1>Video Player</h1>
    <video controls width="800">
        <source src="{{ video_url }}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</body>
</html>
'''

@app.route('/')
def index():
    video_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': BUCKET_NAME, 'Key': VIDEO_KEY},
        ExpiresIn=3600  # 1 hour
    )
    return render_template_string(HTML_TEMPLATE, video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
