from typing import Generator

import json
import os


def generate_match_ids() -> Generator[str, None, None]:
    yield from [
        "33be7c4e-5057-4815-9397-83d18adceae5",
        "99cb44e3-1ae2-4ed3-91a5-060c15921290",
        "a8512901-d61f-4514-a043-8e5fff788117",
        "2dd68769-ee5f-47ff-bb99-9dd57e065e9a",
        "78b35b69-7550-4525-94a2-cb0254f5afe8",
        "eadbc382-3a6f-4663-9ed9-746e3fe9e9c0",
    ]


def generate_act_ids() -> Generator[str, None, None]:
    yield from [
        "3f61c772-4560-cd3f-5d3f-a7ab5abda6b3",
        "0530b9c4-4980-f2ee-df5d-09864cd00542",
        "46ea6166-4573-1128-9cea-60a15640059b",
        "97b6e739-44cc-ffa7-49ad-398ba502ceb0",
        "ab57ef51-4e59-da91-cc8d-51a5a2b9b8ff",
        "52e9749a-429b-7060-99fe-4595426a0cf7",
        "2a27e5d2-4d30-c9e2-b15a-93b8909a442c",
        "4cb622e1-4244-6da3-7276-8daaf1c01be2",
        "a16955a5-4ad0-f761-5e9e-389df1c892fb",
        "573f53ac-41a5-3a7d-d9ce-d6a6298e5704",
        "d929bc38-4ab6-7da4-94f0-ee84f8ac141e",
        "3e47230a-463c-a301-eb7d-67bb60357d4f",
        "67e373c7-48f7-b422-641b-079ace30b427",
        "7a85de9a-4032-61a9-61d8-f4aa2b4a84b6",
        "aca29595-40e4-01f5-3f35-b1b3d304c96e",
    ]


def get_mock_response(filename: str):
    path = os.path.join(os.path.dirname(__file__), "mock_responses", filename)
    with open(path) as f:
        return json.load(f)
