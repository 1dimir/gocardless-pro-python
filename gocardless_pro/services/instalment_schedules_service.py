# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class InstalmentSchedulesService(base_service.BaseService):
    """Service class that provides access to the instalment_schedules
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.InstalmentSchedule
    RESOURCE_NAME = 'instalment_schedules'


    def create(self,params=None, headers=None):
        """Create an instalment schedule.

        Creates a new instalment schedule object, along with the associated
        payments.
        
        The `instalments` property can either be an array of payment properties
        (`amount`
        and `charge_date`) or a schedule object with `interval`,
        `interval_unit` and
        `amounts`.
        
        It can take quite a while to create the associated payments, so the API
        will return
        the status as `pending` initially. When processing has completed, a
        subsequent
        GET request for the instalment schedule will either have the status
        `success` and link to
        the created payments, or the status `error` and detailed information
        about the
        failures.

        Args:
              params (dict, optional): Request body.

        Returns:
              ListResponse of InstalmentSchedule instances
        """
        path = '/instalment_schedules'
        
        if params is not None:
            params = {self._envelope_key(): params}

        try:
          response = self._perform_request('POST', path, params, headers,
                                            retry_failures=True)
        except errors.IdempotentCreationConflictError as err:
          return self.get(identity=err.conflicting_resource_id,
                          params=params,
                          headers=headers)
        return self._resource_for(response)
  

    def list(self,params=None, headers=None):
        """List instalment schedules.

        Returns a [cursor-paginated](#api-usage-cursor-pagination) list of your
        instalment schedules.

        Args:
              params (dict, optional): Query string parameters.

        Returns:
              InstalmentSchedule
        """
        path = '/instalment_schedules'
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)
    
  

    def get(self,identity,params=None, headers=None):
        """Get a single instalment schedule.

        Retrieves the details of an existing instalment schedule.

        Args:
              identity (string): Unique identifier, beginning with "IS".
              params (dict, optional): Query string parameters.

        Returns:
              ListResponse of InstalmentSchedule instances
        """
        path = self._sub_url_params('/instalment_schedules/:identity', {
          
            'identity': identity,
          })
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  

    def cancel(self,identity,params=None, headers=None):
        """Cancel an instalment schedule.

        Immediately cancels an instalment schedule; no further payments will be
        collected for it.
        
        This will fail with a `cancellation_failed` error if the instalment
        schedule is already cancelled or has completed.

        Args:
              identity (string): Unique identifier, beginning with "IS".
              params (dict, optional): Request body.

        Returns:
              ListResponse of InstalmentSchedule instances
        """
        path = self._sub_url_params('/instalment_schedules/:identity/actions/cancel', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {'data': params}
        response = self._perform_request('POST', path, params, headers,
                                         retry_failures=False)
        return self._resource_for(response)
  