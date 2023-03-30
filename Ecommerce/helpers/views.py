from rest_framework.views import APIView
from rest_framework.response import Response

class BaseView(APIView):
    required_post_fields= set()
    def post(self, reqest, format=None):
        for fields in self.required_post_fields:
            if not fields:
                resp = {
                    "code":404,
                    "message": f"Field '{fields}' not found!"
                }
                return Response(resp, 404)