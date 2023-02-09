# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class BillingRequest(object):
    """A thin wrapper around a billing_request, providing easy access to its
    attributes.

    Example:
      billing_request = client.billing_requests.get()
      billing_request.id
    """

    def __init__(self, attributes, api_response):
        self.attributes = attributes
        self.api_response = api_response

    @property
    def actions(self):
        return self.attributes.get('actions')
  

    @property
    def created_at(self):
        return self.attributes.get('created_at')
  

    @property
    def fallback_enabled(self):
        return self.attributes.get('fallback_enabled')
  

    @property
    def id(self):
        return self.attributes.get('id')
  

    @property
    def links(self):
        return self.Links(self.attributes.get('links'))
  

    @property
    def mandate_request(self):
        return self.MandateRequest(self.attributes.get('mandate_request'))
  

    @property
    def metadata(self):
        return self.attributes.get('metadata')
  

    @property
    def payment_request(self):
        return self.PaymentRequest(self.attributes.get('payment_request'))
  

    @property
    def purpose_code(self):
        return self.attributes.get('purpose_code')
  

    @property
    def resources(self):
        return self.Resources(self.attributes.get('resources'))
  

    @property
    def status(self):
        return self.attributes.get('status')
  


  

  

  

  

  
    class Links(object):
        """Wrapper for the response's 'links' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def bank_authorisation(self):
            return self.attributes.get('bank_authorisation')
    
        @property
        def creditor(self):
            return self.attributes.get('creditor')
    
        @property
        def customer(self):
            return self.attributes.get('customer')
    
        @property
        def customer_bank_account(self):
            return self.attributes.get('customer_bank_account')
    
        @property
        def customer_billing_detail(self):
            return self.attributes.get('customer_billing_detail')
    
        @property
        def mandate_request(self):
            return self.attributes.get('mandate_request')
    
        @property
        def mandate_request_mandate(self):
            return self.attributes.get('mandate_request_mandate')
    
        @property
        def organisation(self):
            return self.attributes.get('organisation')
    
        @property
        def payment_request(self):
            return self.attributes.get('payment_request')
    
        @property
        def payment_request_payment(self):
            return self.attributes.get('payment_request_payment')
    
  

  
    class MandateRequest(object):
        """Wrapper for the response's 'mandate_request' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def authorisation_source(self):
            return self.attributes.get('authorisation_source')
    
        @property
        def constraints(self):
            return self.attributes.get('constraints')
    
        @property
        def currency(self):
            return self.attributes.get('currency')
    
        @property
        def description(self):
            return self.attributes.get('description')
    
        @property
        def links(self):
            return self.attributes.get('links')
    
        @property
        def metadata(self):
            return self.attributes.get('metadata')
    
        @property
        def scheme(self):
            return self.attributes.get('scheme')
    
        @property
        def verify(self):
            return self.attributes.get('verify')
    
  

  

  
    class PaymentRequest(object):
        """Wrapper for the response's 'payment_request' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def amount(self):
            return self.attributes.get('amount')
    
        @property
        def app_fee(self):
            return self.attributes.get('app_fee')
    
        @property
        def currency(self):
            return self.attributes.get('currency')
    
        @property
        def description(self):
            return self.attributes.get('description')
    
        @property
        def links(self):
            return self.attributes.get('links')
    
        @property
        def metadata(self):
            return self.attributes.get('metadata')
    
        @property
        def scheme(self):
            return self.attributes.get('scheme')
    
  

  

  
    class Resources(object):
        """Wrapper for the response's 'resources' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def customer(self):
            return self.attributes.get('customer')
    
        @property
        def customer_bank_account(self):
            return self.attributes.get('customer_bank_account')
    
        @property
        def customer_billing_detail(self):
            return self.attributes.get('customer_billing_detail')
    
  

  

