from rest_framework.views import APIView
from rest_framework.responce import Responce


class HelloAPIView(APIView):
    """Test api view"""

    def get(self, request,format=None):
        """Returns a list of apiview features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional django view',
            'Gived you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Rsponce({'message' : 'Hello !','an_apiview' : an_apiview})
