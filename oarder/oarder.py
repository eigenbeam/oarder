import datetime as dt
from getpass import getpass, getuser
import sys

from harmony import BBox, Client, Collection, Request, Environment


def oarder():
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

    username = getuser()
    password = getpass()
    harmony_client = Client(auth=(username, password), env=Environment.UAT)

    collection = "atl03"

    request = Request(
        collection=collections[collection],
        spatial=bounding_boxes[collection],
        temporal=temporal_ranges[collection],
        skip_preview=True,
    )

    print("Request valid: " + str(request.is_valid()))
    print("Sending request: " + harmony_client.request_as_url(request))

    job_id = harmony_client.submit(request)
    results = harmony_client.result_json(job_id, show_progress=True)
    print(results)

    futures = harmony_client.download_all(job_id)
    filenames = [f.result() for f in futures]

    for filename in filenames:
        print(filename)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        oarder()
    else:
        print("Usage: oarder.py collection")
        exit(1)
