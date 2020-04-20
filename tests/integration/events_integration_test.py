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
def test_events_list():
    fixture = helpers.load_fixture('events')['list']
    helpers.stub_response(fixture)
    response = helpers.client.events.list(*fixture['url_params'])
    body = fixture['body']['events']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Event)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal([r.action for r in response.records],
                 [b.get('action') for b in body])
    assert_equal([r.created_at for r in response.records],
                 [b.get('created_at') for b in body])
    assert_equal([r.customer_notifications for r in response.records],
                 [b.get('customer_notifications') for b in body])
    assert_equal([r.id for r in response.records],
                 [b.get('id') for b in body])
    assert_equal([r.metadata for r in response.records],
                 [b.get('metadata') for b in body])
    assert_equal([r.resource_type for r in response.records],
                 [b.get('resource_type') for b in body])

@responses.activate
def test_timeout_events_list_retries():
    fixture = helpers.load_fixture('events')['list']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.events.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['events']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Event)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

def test_502_events_list_retries():
    fixture = helpers.load_fixture('events')['list']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.events.list(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['events']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Event)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

@responses.activate
def test_events_all():
    fixture = helpers.load_fixture('events')['list']

    def callback(request):
        if 'after=123' in request.url:
          fixture['body']['meta']['cursors']['after'] = None
        else:
          fixture['body']['meta']['cursors']['after'] = '123'
        return [200, {}, json.dumps(fixture['body'])]

    url = 'http://example.com' + fixture['path_template']
    responses.add_callback(fixture['method'], url, callback)

    all_records = list(helpers.client.events.all())
    assert_equal(len(all_records), len(fixture['body']['events']) * 2)
    for record in all_records:
      assert_is_instance(record, resources.Event)
    
  

@responses.activate
def test_events_get():
    fixture = helpers.load_fixture('events')['get']
    helpers.stub_response(fixture)
    response = helpers.client.events.get(*fixture['url_params'])
    body = fixture['body']['events']

    assert_is_instance(response, resources.Event)
    assert_is_none(responses.calls[-1].request.headers.get('Idempotency-Key'))
    assert_equal(response.action, body.get('action'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.customer_notifications, body.get('customer_notifications'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.resource_type, body.get('resource_type'))
    assert_equal(response.details.bank_account_id,
                 body.get('details')['bank_account_id'])
    assert_equal(response.details.cause,
                 body.get('details')['cause'])
    assert_equal(response.details.currency,
                 body.get('details')['currency'])
    assert_equal(response.details.description,
                 body.get('details')['description'])
    assert_equal(response.details.origin,
                 body.get('details')['origin'])
    assert_equal(response.details._property,
                 body.get('details')['property'])
    assert_equal(response.details.reason_code,
                 body.get('details')['reason_code'])
    assert_equal(response.details.scheme,
                 body.get('details')['scheme'])
    assert_equal(response.details.will_attempt_retry,
                 body.get('details')['will_attempt_retry'])
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])
    assert_equal(response.links.instalment_schedule,
                 body.get('links')['instalment_schedule'])
    assert_equal(response.links.mandate,
                 body.get('links')['mandate'])
    assert_equal(response.links.new_customer_bank_account,
                 body.get('links')['new_customer_bank_account'])
    assert_equal(response.links.new_mandate,
                 body.get('links')['new_mandate'])
    assert_equal(response.links.organisation,
                 body.get('links')['organisation'])
    assert_equal(response.links.parent_event,
                 body.get('links')['parent_event'])
    assert_equal(response.links.payment,
                 body.get('links')['payment'])
    assert_equal(response.links.payout,
                 body.get('links')['payout'])
    assert_equal(response.links.previous_customer_bank_account,
                 body.get('links')['previous_customer_bank_account'])
    assert_equal(response.links.refund,
                 body.get('links')['refund'])
    assert_equal(response.links.subscription,
                 body.get('links')['subscription'])

@responses.activate
def test_timeout_events_get_retries():
    fixture = helpers.load_fixture('events')['get']
    with helpers.stub_timeout_then_response(fixture) as rsps:
      response = helpers.client.events.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['events']

    assert_is_instance(response, resources.Event)

def test_502_events_get_retries():
    fixture = helpers.load_fixture('events')['get']
    with helpers.stub_502_then_response(fixture) as rsps:
      response = helpers.client.events.get(*fixture['url_params'])
      assert_equal(2, len(rsps.calls))
      assert_equal(rsps.calls[0].request.headers.get('Idempotency-Key'),
                   rsps.calls[1].request.headers.get('Idempotency-Key'))
    body = fixture['body']['events']

    assert_is_instance(response, resources.Event)
  
