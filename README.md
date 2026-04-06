# Dynamodb Client

DynamoDB utilities for AWS

## Features

- Zero external dependencies (stdlib only)
- Easy-to-use CLI interface
- Professional Python implementation
- MIT licensed

## Installation

```bash
pip install -e .
```

Or clone and install:

```bash
git clone https://github.com/Viprasol-Tech/dynamodb-client
cd dynamodb-client
pip install -e .
```

## Usage

### Python

```python
from dynamodb_client import DynamodbClient

result = DynamodbClient.process("data")
print(result)
```

### CLI

```bash
python -m dynamodb_client "your input here"
```

## Documentation

See the source code and docstrings for detailed API documentation.

## License

MIT License - see LICENSE file for details

## About

Part of Viprasol Utilities: https://viprasol.com

Created by Viprasol - Building AI-focused tools for developers.
