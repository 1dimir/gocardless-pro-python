# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class MandateImportsService(base_service.BaseService):
    """Service class that provides access to the mandate_imports
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.MandateImport
    RESOURCE_NAME = 'mandate_imports'


    def create(self,params=None, headers=None):
        """Create a new mandate import.

        Mandate imports are first created, before mandates are added
        one-at-a-time, so
        this endpoint merely signals the start of the import process. Once
        you've finished
        adding entries to an import, you should
        [submit](#mandate-imports-submit-a-mandate-import) it.

        Args:
              params (dict, optional): Request body.

        Returns:
              MandateImport
        """
        path = '/mandate_imports'
        
        if params is not None:
            params = {self._envelope_key(): params}

        try:
          response = self._perform_request('POST', path, params, headers,
                                            retry_failures=True)
        except errors.IdempotentCreationConflictError as err:
          if self.raise_on_idempotency_conflict:
            raise err
          return self.get(identity=err.conflicting_resource_id,
                          params=params,
                          headers=headers)
        return self._resource_for(response)
  

    def get(self,identity,params=None, headers=None):
        """Get a mandate import.

        Returns a single mandate import.

        Args:
              identity (string): Unique identifier, beginning with "IM".
              params (dict, optional): Query string parameters.

        Returns:
              MandateImport
        """
        path = self._sub_url_params('/mandate_imports/:identity', {
          
            'identity': identity,
          })
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def submit(self,identity,params=None, headers=None):
        """Submit a mandate import.

        Submits the mandate import, which allows it to be processed by a member
        of the
        GoCardless team. Once the import has been submitted, it can no longer
        have entries
        added to it.
        
        In our sandbox environment, to aid development, we automatically
        process mandate
        imports approximately 10 seconds after they are submitted. This will
        allow you to
        test both the "submitted" response and wait for the webhook to confirm
        the
        processing has begun.

        Args:
              identity (string): Unique identifier, beginning with "IM".
              params (dict, optional): Request body.

        Returns:
              MandateImport
        """
        path = self._sub_url_params('/mandate_imports/:identity/actions/submit', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  

    def cancel(self,identity,params=None, headers=None):
        """Cancel a mandate import.

        Cancels the mandate import, which aborts the import process and stops
        the mandates
        being set up in GoCardless. Once the import has been cancelled, it can
        no longer have
        entries added to it. Mandate imports which have already been submitted
        or processed
        cannot be cancelled.

        Args:
              identity (string): Unique identifier, beginning with "IM".
              params (dict, optional): Request body.

        Returns:
              MandateImport
        """
        path = self._sub_url_params('/mandate_imports/:identity/actions/cancel', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  
