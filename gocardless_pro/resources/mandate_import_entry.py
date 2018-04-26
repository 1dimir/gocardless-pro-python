# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class MandateImportEntry(object):
    """A thin wrapper around a mandate_import_entry, providing easy access to its
    attributes.

    Example:
      mandate_import_entry = client.mandate_import_entries.get()
      mandate_import_entry.id
    """

    def __init__(self, attributes, api_response):
        self.attributes = attributes
        self.api_response = api_response

    @property
    def created_at(self):
        return self.attributes.get('created_at')
  

    @property
    def links(self):
        return self.Links(self.attributes.get('links'))
  

    @property
    def record_identifier(self):
        return self.attributes.get('record_identifier')
  


  

  
    class Links(object):
        """Wrapper for the response's 'links' attribute."""

        def __init__(self, attributes):
            self.attributes = attributes
    
        @property
        def customer(self):
            return self.attributes.get('customer')
    
        @property
        def customer_bank_account(self):
            return self.attributes.get('customer_bank_account')
    
        @property
        def mandate(self):
            return self.attributes.get('mandate')
    
        @property
        def mandate_import(self):
            return self.attributes.get('mandate_import')
    
  

  

