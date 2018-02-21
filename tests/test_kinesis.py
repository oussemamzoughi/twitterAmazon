import unittest
from TwitterAPI import TwitterAPI
import boto3
import json
import twitterCreds
import pytest
from sys import getsizeof


def test_api():
    """Test le fonctionnement de l api'."""
    consumer_key = twitterCreds.consumer_key
    consumer_secret = twitterCreds.consumer_secret
    access_token_key = twitterCreds.access_token_key
    access_token_secret = twitterCreds.access_token_secret
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    assert (getsizeof(api) > 0)

def test_requestapi():
    """Test le fonctionnement du request api ."""
    consumer_key = twitterCreds.consumer_key
    consumer_secret = twitterCreds.consumer_secret
    access_token_key = twitterCreds.access_token_key
    access_token_secret = twitterCreds.access_token_secret
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    r = api.request('statuses/filter', {'locations':'-90,-90,90,90'})
    assert (getsizeof(r) > 0)   

   
