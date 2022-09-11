import io;
import pandas;
import boto3;

BASE_URL = "https://summer-project.s3.amazonaws.com/";
BUCKET_NAME = "summer-project";

def getS3Bucket(credentials):
    '''
        Input credential text and return bucket object.
    '''
    CREDENTIAL = {
    'aws_access_key_id': None,
    'aws_secret_access_key': None,
    'aws_session_token': None
    };

    for item in credentials.split('\n'):
        if item.startswith('aws_access_key_id'):
            CREDENTIAL['aws_access_key_id'] = item.split('=')[1];
            continue;
        if item.startswith('aws_secret_access_key'):
            CREDENTIAL['aws_secret_access_key'] = item.split('=')[1];
            continue;
        if item.startswith('aws_session_token'):
            CREDENTIAL['aws_session_token'] = item.split('=')[1];
            continue;
    
    session = boto3.Session(
        aws_access_key_id=CREDENTIAL["aws_access_key_id"],
        aws_secret_access_key=CREDENTIAL["aws_secret_access_key"],
        aws_session_token=CREDENTIAL["aws_session_token"]
    );
    
    s3 = session.resource('s3');
    bucket = s3.Bucket(BUCKET_NAME);
    
    return bucket;

def loadDataByCSV(obj, **args):
    return pandas.read_csv(io.BytesIO(obj.get()['Body'].read()), **args);

def loadDataByJson(obj, **args):
    return pandas.read_json(io.BytesIO(obj.get()['Body'].read()), **args);

def loadDataByParquet(obj, **args):
    return pandas.read_parquet(io.BytesIO(obj.get()['Body'].read()), **args);

def objectExists(obj):
    try:
        obj.load();
        return True;
    except:
        return False;

if __name__ == '__main__':
    input = '''[default]
aws_access_key_id=ASIAWLUGPLQ4CABB5XXZ
aws_secret_access_key=3i3dreKJn+FKuWa3SrAYnODo0cnlVSXgtbYCywJ4
aws_session_token=FwoGZXIvYXdzELP//////////wEaDNTPT9voVtD0NFormiK5AWlUjaR4W7p3UXBhJpQxMc6NvMm2VVgY9+nTAOtkcuz0nrBZi1AWFjYb+IJwmKlsBF8mP1CGjVvXZonMK4wiyv6dhrYQNTUxFBUkyv5BNPPQc9T9CMimh6WHhrCF3OkKMk5NT1IJX3GMTzPQVRADtV7K1d+1BvBdgb97EYAkiJQvO7PnrqBXHBf+qupNxT5l2mWk7jAu0D3lGiCn5TR01fj0xfubBwax+g2A1Bl5v0uloHekt5bcLbv4KLaXj5MGMi2YnahZKYM6w2k8eN8B955hhAcekw00fC8InTKh0FE0i8bJXS6bjJI/FC5Cw9A=''';
    bucket = getS3Bucket(input);
    objects = list(bucket.objects.all());
    sample = objects[3];
    df = loadDataByCSV(sample);
    print(df.head());