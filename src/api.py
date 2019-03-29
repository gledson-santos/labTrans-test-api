from config import URL
import requests

class Api(object):

    def get_token(self, user, pasword):
        req = requests.post(URL + "/authentication", data = {"email": user, "password": pasword})
        return req.json()

    def get_manifestations(self, user, password):
        token = self.get_token(user, password)
        token = 'Bearer ' + token['token']
        HEADERS = {"Authorization": token, "content-type": "text"}
        req = requests.get(URL + "/manifestations", headers=HEADERS)
        return req.json()

    def get_profile_list(self, user, password):
        token = self.get_token(user, password)
        token = 'Bearer ' + token['token']
        HEADERS = {"Authorization": token, "content-type": "text"}
        req = requests.get(URL + "/profile", headers=HEADERS)
        return req.json()

    def get_manifest_file(self, user, password, id_plan):
        token = self.get_token(user, password)
        token = 'Bearer ' + token['token']
        HEADERS = {"Authorization": token, "content-type": "text"}
        req = requests.get(URL + "/manifestations/" + id_plan + "/file", headers=HEADERS)
        return req