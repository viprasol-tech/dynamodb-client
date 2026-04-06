"""
dynamodb-client - DynamoDB utilities for AWS

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import DynamodbClient, scan, process, main

__all__ = ["DynamodbClient", "scan", "process", "main"]
