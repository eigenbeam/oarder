from datetime import datetime
import json
from typing import Tuple

from pydantic import BaseModel

from oarder import order


class OrderRequest(BaseModel):
    collection_name: str
    start_datetime: datetime
    end_datetime: datetime
    spatial_bbox: Tuple[float, float, float, float]


def handler(event, context):
    body = event["body"]
    order_request = OrderRequest(**body)
    print(order_request.model_dump())

    collection_name = order_request.collection_name

    order.oarder({
        "collection": order.collections[collection_name],
        "spatial": order.bounding_boxes[collection_name],
        "temporal": order.temporal_ranges[collection_name],
    })

    return {
        "statusCode": 200,
        "body": json.dumps("Harmony order submitted successfully"),
    }


if __name__ == "__main__":
    print(handler(None, None))
