import datetime as dt
import json

import boto3
from botocore.exceptions import ClientError

from harmony import BBox, Client, Collection, Request, Environment

collections = {
    "atl03": Collection(id="C1256407609-NSIDC_CUAT"),
    "atl06": Collection(id="C1256358217-NSIDC_CUAT"),
    "atl07": Collection(id="C1256535488-NSIDC_CUAT"),
    "atl08": Collection(id="C1256432189-NSIDC_CUAT"),
    "atl10": Collection(id="C1256535487-NSIDC_CUAT"),
    "atl12": Collection(id="C1256476536-NSIDC_CUAT"),
    "atl13": Collection(id="C1257810199-NSIDC_CUAT"),
}

bounding_boxes = {
    "atl03": BBox(96, -72, 109, -64),
    "atl06": BBox(-120.4, 58.3, -120.1, 58.7),
    "atl07": BBox(-100.2, 70.5, -99.8, 71.0),
    "atl08": BBox(-94, 80, -93.5, 80.1),
    "atl10": BBox(-106.9, 80.1, -106.2, 80.3),
    "atl12": BBox(-95.5, 78.6, -94.6, 79.2),
    "atl13": BBox(-97.6, 75.9, -96.6, 76.7),
}

temporal_ranges = {
    "atl03": {
        "start": dt.datetime(2020, 1, 1, 0, 0, 0),
        "stop": dt.datetime(2020, 1, 2, 23, 59, 59),
    },
    "atl06": {
        "start": dt.datetime(2020, 1, 1, 0, 0, 0),
        "stop": dt.datetime(2020, 1, 2, 23, 59, 59),
    },
    "atl07": {
        "start": dt.datetime(2020, 1, 1, 0, 0, 0),
        "stop": dt.datetime(2020, 1, 2, 23, 59, 59),
    },
    "atl08": {
        "start": dt.datetime(2020, 1, 1, 0, 0, 0),
        "stop": dt.datetime(2020, 1, 2, 23, 59, 59),
    },
    "atl10": {
        "start": dt.datetime(2020, 1, 1, 0, 0, 0),
        "stop": dt.datetime(2020, 1, 2, 23, 59, 59),
    },
    "atl12": {
        "start": dt.datetime(2020, 1, 1, 0, 0, 0),
        "stop": dt.datetime(2020, 1, 2, 23, 59, 59),
    },
    "atl13": {
        "start": dt.datetime(2020, 1, 1, 0, 0, 0),
        "stop": dt.datetime(2020, 1, 2, 23, 59, 59),
    },
}


def oarder(order_request):
    collection = order_request["collection"]
    spatial = order_request["spatial"]
    temporal = order_request["temporal"]

    harmony_client = Client(token=edl_token(), env=Environment.UAT)

    request = Request(
        collection=collection, spatial=spatial, temporal=temporal, skip_preview=True
    )

    print("Request valid: " + str(request.is_valid()))
    print("Sending request: " + harmony_client.request_as_url(request))

    job_id = harmony_client.submit(request)
    print("Successfully submitted Harmony job: " + job_id)

    # results = harmony_client.result_json(job_id, show_progress=True)
    # futures = harmony_client.download_all(job_id)
    # filenames = [f.result() for f in futures]
    # for filename in filenames:
    #     print(filename)


# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/


def edl_token():
    secret_name = "oa_edl"
    region_name = "us-west-2"

    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e

    value = get_secret_value_response["SecretString"]
    secret = json.loads(value)

    return secret.get("token")
