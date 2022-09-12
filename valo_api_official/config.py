from typing import List


class Config:
    NEAREST_CLUSTER: str = "europe"
    NEAREST_CLUSTER_SHORT: str = "eu"
    USER_AGENT: str = "Python Valorant API Wrapper"
    ALL_REGIONS: List[str] = ["eu", "na", "ap", "kr", "latam", "br"]
    ALL_LOCALS: List[str] = [
        "ar-AE",
        "de-DE",
        "en-US",
        "es-ES",
        "es-MX",
        "fr-FR",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "pl-PL",
        "pt-BR",
        "ru-RU",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ]
