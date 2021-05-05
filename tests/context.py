import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from autodesk_forge_sdk import AuthenticationClient, Scope, OAuthTokenProvider, SimpleTokenProvider
from autodesk_forge_sdk import OSSClient, ModelDerivativeClient, urnify

FORGE_CLIENT_ID = os.environ["FORGE_CLIENT_ID"]
FORGE_CLIENT_SECRET = os.environ["FORGE_CLIENT_SECRET"]
FORGE_BUCKET = os.environ["FORGE_BUCKET"]