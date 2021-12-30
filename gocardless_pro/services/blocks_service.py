# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class BlocksService(base_service.BaseService):
    """Service class that provides access to the blocks
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.Block
    RESOURCE_NAME = 'blocks'


    def create(self,params=None, headers=None):
        """Create a block.

        Creates a new Block of a given type. By default it will be active.

        Args:
              params (dict, optional): Request body.

        Returns:
              Block
        """
        path = '/blocks'
        
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
        """Get a single block.

        Retrieves the details of an existing block.

        Args:
              identity (string): Unique identifier, beginning with "BLC".
              params (dict, optional): Query string parameters.

        Returns:
              Block
        """
        path = self._sub_url_params('/blocks/:identity', {
          
            'identity': identity,
          })
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def list(self,params=None, headers=None):
        """List multiple blocks.

        Returns a [cursor-paginated](#api-usage-cursor-pagination) list of your
        blocks.

        Args:
              params (dict, optional): Query string parameters.

        Returns:
              ListResponse of Block instances
        """
        path = '/blocks'
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)
    
  

    def disable(self,identity,params=None, headers=None):
        """Disable a block.

        Disables a block so that it no longer will prevent mandate creation.

        Args:
              identity (string): Unique identifier, beginning with "BLC".
              params (dict, optional): Request body.

        Returns:
              Block
        """
        path = self._sub_url_params('/blocks/:identity/actions/disable', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  

    def enable(self,identity,params=None, headers=None):
        """Enable a block.

        Enables a previously disabled block so that it will prevent mandate
        creation

        Args:
              identity (string): Unique identifier, beginning with "BLC".
              params (dict, optional): Request body.

        Returns:
              Block
        """
        path = self._sub_url_params('/blocks/:identity/actions/enable', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  

    def block_by_ref(self,params=None, headers=None):
        """Create blocks by reference.

        Creates new blocks for a given reference. By default blocks will be
        active.
        Returns 201 if at least one block was created. Returns 200 if there
        were no new
        blocks created.

        Args:
              params (dict, optional): Request body.

        Returns:
              ListResponse of Block instances
        """
        path = '/block_by_ref'
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  
