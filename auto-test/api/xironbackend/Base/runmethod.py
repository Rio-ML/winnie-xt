import requests


class RunMethod:

    def post_main(self, url, data, header=None):
        res = None
        if header is not None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        print(res.status_code)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header is not None:
            res = requests.get(url=url, params=data, headers=header)
        else:
            res = requests.get(url=url, params=data)
        return res.json()

    def delete_main(self, url, data=None, header=None):
        res = None
        if header is not None:
            res = requests.delete(url=url, data=data, headers=header)
        else:
            res = requests.delete(url=url, data=data)
        if res.text == '':  # 兼容有些delete处理后，返回结果为空的情况，直接返回 response 对象
            return res
        else:
            return res.json()

    def put_main(self, url, data, header=None):
        res = None
        if header is not None:
            res = requests.put(url=url, data=data, headers=header)
        else:
            res = requests.put(url=url, data=data)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, header)
        elif method == 'get':
            res = self.get_main(url, data, header)
        elif method == 'delete':
            res = self.delete_main(url, data, header)
        else:
            res = self.put_main(url, data, header)
        return res

