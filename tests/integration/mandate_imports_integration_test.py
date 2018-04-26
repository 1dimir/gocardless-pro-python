# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import json

import requests
import responses
from nose.tools import (
  assert_equal,
  assert_is_instance,
  assert_is_none,
  assert_is_not_none,
  assert_not_equal,
  assert_raises
)

from gocardless_pro.errors import MalformedResponseError
from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers
  

@responses.activate
def test_mandate_imports_create():
    fixture = helpers.load_fixture('mandate_imports')['create']
    helpers.stub_response(fixture)
    response = helpers.client.mandate_imports.create(*fixture['url_params'])
    body = fixture['body']['mandate_imports']

    assert_is_instance(response, resources.MandateImport)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.scheme, body.get('scheme'))
    assert_equal(response.status, body.get('status'))

@responses.activate
def test_mandate_imports_create_new_idempotency_key_for_each_call():
    fixture = helpers.load_fixture('mandate_imports')['create']
    helpers.stub_response(fixture)
    helpers.client.mandate_imports.create(*fixture['url_params'])
    helpers.client.mandate_imports.create(*fixture['url_params'])
    assert_not_equal(responses.calls[0].request.headers.get('Idempotency-Key'),
                     responses.calls[1].request.headers.get('Idempotency-Key'))

def test_timeout_mandate_imports_create_idempotency_conflict():
    create_fixture = helpers.load_fixture('mandate_imports')['create']
    get_fixture = helpers.load_fixture('mandate_imports')['get']
    with helpers.stub_timeout_then_idempotency_conflict(create_fixture, get_fixture) as rsps:
      response = helpers.client.mandate_imports.create(*create_fixture['url_params'])
      assert_equal(2, len(rsps.calls))

    assert_is_instance(response, resources.MandateImport)

@responses.activate
def test_timeout_mandate_imports_create_retries():
    fixture = helpers.load_fixture('mandate_imports')['create']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.mandate_imports.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['mandate_imports']

    assert_is_instance(response, resources.MandateImport)

def test_502_mandate_imports_create_retries():
    fixture = helpers.load_fixture('mandate_imports')['create']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.mandate_imports.create(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['mandate_imports']

    assert_is_instance(response, resources.MandateImport)
  

@responses.activate
def test_mandate_imports_get():
    fixture = helpers.load_fixture('mandate_imports')['get']
    helpers.stub_response(fixture)
    response = helpers.client.mandate_imports.get(*fixture['url_params'])
    body = fixture['body']['mandate_imports']

    assert_is_instance(response, resources.MandateImport)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.scheme, body.get('scheme'))
    assert_equal(response.status, body.get('status'))

@responses.activate
def test_timeout_mandate_imports_get_retries():
    fixture = helpers.load_fixture('mandate_imports')['get']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.mandate_imports.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['mandate_imports']

    assert_is_instance(response, resources.MandateImport)

def test_502_mandate_imports_get_retries():
    fixture = helpers.load_fixture('mandate_imports')['get']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.mandate_imports.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['mandate_imports']

    assert_is_instance(response, resources.MandateImport)
  

@responses.activate
def test_mandate_imports_submit():
    fixture = helpers.load_fixture('mandate_imports')['submit']
    helpers.stub_response(fixture)
    response = helpers.client.mandate_imports.submit(*fixture['url_params'])
    body = fixture['body']['mandate_imports']

    assert_is_instance(response, resources.MandateImport)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.scheme, body.get('scheme'))
    assert_equal(response.status, body.get('status'))

def test_timeout_mandate_imports_submit_doesnt_retry():
    fixture = helpers.load_fixture('mandate_imports')['submit']
    with helpers.stub_timeout(fixture) as rsps:
      with assert_raises(requests.ConnectTimeout):
        response = helpers.client.mandate_imports.submit(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))

def test_502_mandate_imports_submit_doesnt_retry():
    fixture = helpers.load_fixture('mandate_imports')['submit']
    with helpers.stub_502(fixture) as rsps:
      with assert_raises(MalformedResponseError):
        response = helpers.client.mandate_imports.submit(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))
  

@responses.activate
def test_mandate_imports_cancel():
    fixture = helpers.load_fixture('mandate_imports')['cancel']
    helpers.stub_response(fixture)
    response = helpers.client.mandate_imports.cancel(*fixture['url_params'])
    body = fixture['body']['mandate_imports']

    assert_is_instance(response, resources.MandateImport)
    assert_is_not_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.scheme, body.get('scheme'))
    assert_equal(response.status, body.get('status'))

def test_timeout_mandate_imports_cancel_doesnt_retry():
    fixture = helpers.load_fixture('mandate_imports')['cancel']
    with helpers.stub_timeout(fixture) as rsps:
      with assert_raises(requests.ConnectTimeout):
        response = helpers.client.mandate_imports.cancel(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))

def test_502_mandate_imports_cancel_doesnt_retry():
    fixture = helpers.load_fixture('mandate_imports')['cancel']
    with helpers.stub_502(fixture) as rsps:
      with assert_raises(MalformedResponseError):
        response = helpers.client.mandate_imports.cancel(*fixture['url_params'])
      assert_equal(1, len(rsps.calls))
  
