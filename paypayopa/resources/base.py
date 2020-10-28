class Resource(object):

    def __init__(self, client=None):
        self.client = client

    def all(self, data, **kwargs):
        return self.get_url(self.base_url, data, **kwargs)

    def fetch(self, id, url=None, data={}, api_id=None, **kwargs):
        if(url):
            self.url = url
        else:
            self.url = "{}/{}".format(self.base_url, id)
        return self.get_url(self.url, data, api_id, **kwargs)

    def get_url(self, url, data, api_id, **kwargs):
        return self.client.get(url, data, api_id, **kwargs)

    def patch_url(self, url, data, api_id, **kwargs):
        return self.client.patch(url, data, api_id, **kwargs)

    def post_url(self, url, data, api_id, **kwargs):
        return self.client.post(url, data, api_id, **kwargs)

    def put_url(self, url, data, api_id, **kwargs):
        return self.client.put(url, data, api_id, **kwargs)

    def delete_url(self, url, data, api_id, **kwargs):
        return self.client.delete(url, data, api_id, **kwargs)

    def delete(self, id, url=None, data={}, api_id=None, **kwargs):
        if(url):
            self.url = url
        else:
            self.url = "{}/{}/".format(self.base_url, id)
        return self.delete_url(self.url, data, api_id **kwargs)
