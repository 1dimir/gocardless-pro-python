# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class PayoutItemsService(base_service.BaseService):
    """Service class that provides access to the payout_items
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.PayoutItem
    RESOURCE_NAME = 'payout_items'


    def list(self,params=None, headers=None):
        """Get all payout items in a single payout.

        Returns a [cursor-paginated](#api-usage-cursor-pagination) list of
        items in the payout.
        
        <div class="notice notice--warning u-block">
          <p><strong>Note</strong>: This endpoint is changing:</p>
        
          <ul>
            <li>For payouts created from 1 November 2022, the payout items will
        be sorted by payout item ID. For more details, see <a
        href="https://hub.gocardless.com/s/article/FAQ-page-about-payout-items-API-change">this
        FAQ page on the customer hub</a>.</li>
            <li>From 1 March 2023 onwards, we will only serve requests for
        payout items created in the last 6 months. Requests for older payouts
        will return an HTTP status <code>410 Gone</code>.</li>
          </ul>
        </div>
        

        Args:
              params (dict, optional): Query string parameters.

        Returns:
              ListResponse of PayoutItem instances
        """
        path = '/payout_items'
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)
    
  
