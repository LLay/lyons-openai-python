# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from openaix.lib.azure import AzureOpenAI
from typing import Iterator
import contextlib

import os as _os

import httpx
import pytest
from httpx import URL

import openaix
from openaix import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES


def reset_state() -> None:
    openaix._reset_client()
    openaix.api_key = None or "My API Key"
    openaix.organization = None
    openaix.base_url = None
    openaix.timeout = DEFAULT_TIMEOUT
    openaix.max_retries = DEFAULT_MAX_RETRIES
    openaix.default_headers = None
    openaix.default_query = None
    openaix.http_client = None
    openaix.api_type = _os.environ.get("OPENAI_API_TYPE")  # type: ignore
    openaix.api_version = None
    openaix.azure_endpoint = None
    openaix.azure_ad_token = None
    openaix.azure_ad_token_provider = None


@pytest.fixture(autouse=True)
def reset_state_fixture() -> None:
    reset_state()


def test_base_url_option() -> None:
    assert openaix.base_url is None
    assert openaix.completions._client.base_url == URL(
        "https://api.openaix.com/v1/")

    openaix.base_url = "http://foo.com"

    assert openaix.base_url == URL("http://foo.com")
    assert openaix.completions._client.base_url == URL("http://foo.com")


def test_timeout_option() -> None:
    assert openaix.timeout == openaix.DEFAULT_TIMEOUT
    assert openaix.completions._client.timeout == openaix.DEFAULT_TIMEOUT

    openaix.timeout = 3

    assert openaix.timeout == 3
    assert openaix.completions._client.timeout == 3


def test_max_retries_option() -> None:
    assert openaix.max_retries == openaix.DEFAULT_MAX_RETRIES
    assert openaix.completions._client.max_retries == openaix.DEFAULT_MAX_RETRIES

    openaix.max_retries = 1

    assert openaix.max_retries == 1
    assert openaix.completions._client.max_retries == 1


def test_default_headers_option() -> None:
    assert openaix.default_headers == None

    openaix.default_headers = {"Foo": "Bar"}

    assert openaix.default_headers["Foo"] == "Bar"
    assert openaix.completions._client.default_headers["Foo"] == "Bar"


def test_default_query_option() -> None:
    assert openaix.default_query is None
    assert openaix.completions._client._custom_query == {}

    openaix.default_query = {"Foo": {"nested": 1}}

    assert openaix.default_query["Foo"] == {"nested": 1}
    assert openaix.completions._client._custom_query["Foo"] == {"nested": 1}


def test_http_client_option() -> None:
    assert openaix.http_client is None

    original_http_client = openaix.completions._client._client
    assert original_http_client is not None

    new_client = httpx.Client()
    openaix.http_client = new_client

    assert openaix.completions._client._client is new_client


@contextlib.contextmanager
def fresh_env() -> Iterator[None]:
    old = _os.environ.copy()

    try:
        _os.environ.clear()
        yield
    finally:
        _os.environ.update(old)


def test_only_api_key_results_in_openai_api() -> None:
    with fresh_env():
        openaix.api_type = None
        openaix.api_key = "example API key"

        assert type(openaix.completions._client).__name__ == "_ModuleClient"


def test_azure_api_key_env_without_api_version() -> None:
    with fresh_env():
        openaix.api_type = None
        _os.environ["AZURE_OPENAI_API_KEY"] = "example API key"

        with pytest.raises(
            ValueError,
            match=r"Must provide either the `api_version` argument or the `OPENAI_API_VERSION` environment variable",
        ):
            openaix.completions._client  # noqa: B018


def test_azure_api_key_and_version_env() -> None:
    with fresh_env():
        openaix.api_type = None
        _os.environ["AZURE_OPENAI_API_KEY"] = "example API key"
        _os.environ["OPENAI_API_VERSION"] = "example-version"

        with pytest.raises(
            ValueError,
            match=r"Must provide one of the `base_url` or `azure_endpoint` arguments, or the `AZURE_OPENAI_ENDPOINT` environment variable",
        ):
            openaix.completions._client  # noqa: B018


def test_azure_api_key_version_and_endpoint_env() -> None:
    with fresh_env():
        openaix.api_type = None
        _os.environ["AZURE_OPENAI_API_KEY"] = "example API key"
        _os.environ["OPENAI_API_VERSION"] = "example-version"
        _os.environ["AZURE_OPENAI_ENDPOINT"] = "https://www.example"

        openaix.completions._client  # noqa: B018

        assert openaix.api_type == "azure"


def test_azure_azure_ad_token_version_and_endpoint_env() -> None:
    with fresh_env():
        openaix.api_type = None
        _os.environ["AZURE_OPENAI_AD_TOKEN"] = "example AD token"
        _os.environ["OPENAI_API_VERSION"] = "example-version"
        _os.environ["AZURE_OPENAI_ENDPOINT"] = "https://www.example"

        client = openaix.completions._client
        assert isinstance(client, AzureOpenAI)
        assert client._azure_ad_token == "example AD token"


def test_azure_azure_ad_token_provider_version_and_endpoint_env() -> None:
    with fresh_env():
        openaix.api_type = None
        _os.environ["OPENAI_API_VERSION"] = "example-version"
        _os.environ["AZURE_OPENAI_ENDPOINT"] = "https://www.example"
        openaix.azure_ad_token_provider = lambda: "token"

        client = openaix.completions._client
        assert isinstance(client, AzureOpenAI)
        assert client._azure_ad_token_provider is not None
        assert client._azure_ad_token_provider() == "token"
