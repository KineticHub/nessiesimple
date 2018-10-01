import requests


class ApiUtil:

    def __init__(self, api_key="602abce44b0d745ba6b4dfbdf45459a6"):
        self._BASE_URL = "http://api.reimaginebanking.com"
        self._apiKey = api_key

    def _assemble_url(self, endpoint, with_key=True):
        request_url = self._BASE_URL + endpoint
        return request_url + "&key=" + self._apiKey if with_key else request_url

    def has_next_page(self, request):
        return request.get("paging") and len(request.get("data")) > 0

    def get_next_page(self, request):
        if request.get("paging"):
            request_url = self._assemble_url(request.get("paging").get("next"), False)
            print(request_url)
            return requests.get(request_url).json()
        return None

    def get_endpoint(self, endpoint):
        request_url = self._assemble_url(endpoint)
        print(request_url)
        return requests.get(request_url).json()

    def post_endpoint(self, endpoint, payload=None):
        request_url = self._assemble_url(endpoint)
        print(request_url)
        return requests.post(request_url, json=payload).json()

    def delete_endpoint(self, endpoint):
        request_url = self._assemble_url(endpoint)
        print(request_url)
        print("delete data status: " + str(requests.delete(request_url).status_code))

