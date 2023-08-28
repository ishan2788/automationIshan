from datetime import datetime

import requests

GHOST_TOKEN = '6d86763b067ec953a49ddbd950e3c6a4'


class AccessCodes:
    url = "https://eu-prod.cara.care/v1/clinical-trials/qa-access-code/"
    url_stg = "https://eu-staging.cara.care/v1/clinical-trials/qa-access-code/"

    @staticmethod
    def get_study_code(url, study_name, code=None):
        payload = {'study_name': study_name}
        if code:
            payload['code'] = code

        response = requests.post(
            url,
            headers={'Ghost-Token': GHOST_TOKEN},
            json=payload,
        )
        response.raise_for_status()

        return response.json()['access_code']

    def anwender_test_ibd(self):
        return self.get_study_code(self.url, "🧑‍💻 Test Pre-Anwendertest IBD")

    def anwender_test_ibd_stg(self):
        return self.get_study_code(self.url_stg, "🧑‍💻 Test Pre-Anwendertest IBD")

    def anwender_test_hb_stg(self):
        return self.get_study_code(self.url_stg, "🧑‍💻 Test Anwendertest heartburn")

    def anwender_test_hb(self):
        return self.get_study_code(self.url, "🧑‍💻 Test Anwendertest heartburn")

    def pre_anwender_test_hb_stg(self):
        return self.get_study_code(self.url_stg, "🧑‍💻 Test Pre-Anwendertest heartburn")

    def pre_anwender_test_hb(self):
        return self.get_study_code(self.url, "🧑‍💻 Test Pre-Anwendertest heartburn")

    def test_doctors_ibd_stg(self):
        return self.get_study_code(self.url_stg, "🧑‍💻 Test Doctors – IBD")

    def anwender_test_ibs(self):
        return self.get_study_code(self.url, "🧑‍💻 Test Anwendertest IBS")

    def test_doctors_ibs(self):
        return self.get_study_code(self.url, "🧑‍💻 Test Doctors – IBS")

    def doctors_ibs(self):
        return self.get_study_code(self.url, "Doctors – IBS")

    def test_rct_intervention(self):
        return self.get_study_code(self.url, "🧑‍💻 Test RCT IBS", "INTERVENTION")

    def test_rct_control(self):
        return self.get_study_code(self.url, "🧑‍💻 Test RCT IBS", "CONTROL")

    def test_doctors_ibs_stg(self):
        return self.get_study_code(self.url_stg, "🧑‍💻 Test Doctors – IBS")

    def test_stg_rct_intervention(self):
        return self.get_study_code(self.url_stg, "🧑‍💻 Test RCT IBS", "INTERVENTION")

    def test_stg_rct_control(self):
        return self.get_study_code(self.url_stg, "🧑‍💻 Test RCT IBS", "CONTROL")

    @staticmethod
    def test_noventi_android():
        time = datetime.now()
        ct = time.strftime("%d%m%y%H%M%S")
        user_name = "ishan27588" + "+" + ct + "@gmail.com"
        name = "ishan" + "+" + ct
        access_code = "77AAAAAAAAAAAAAX"
        return access_code
        # return user_name, name, access_code

    @staticmethod
    def test_noventi_ios():
        time = datetime.now()
        ct = time.strftime("%d%m%y%H%M%S")
        user_name = "ishan" + "+" + ct + "@cara.care"
        name = "ishan" + "+" + ct
        access_code = "77AAAAAAAAAAAAAX"
        return user_name, name, access_code
