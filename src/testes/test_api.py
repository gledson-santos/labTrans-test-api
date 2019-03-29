import unittest
from api import Api
from config import *


class TestApi(unittest.TestCase):

    def setUp(self):
        self.api = Api()

    def test_get_token_with_permission(self):
        result = self.api.get_token(VALIDE_USER, VALIDE_PASSWORD)
        expect_result = {'user', 'token', 'expirationTime'}
        self.assertEqual(result.keys(), expect_result)

    def test_get_token_withou_permission(self):
        result = self.api.get_token('ssssss@gmail.com', 'dddddddd')
        expect_result = {'name': 'AuthenticationError', 'message': 'E-mail ou senha incorreto'}
        self.assertEqual(result, expect_result)

    def test_get_token_with_format_email_incorrect(self):
        result = self.api.get_token('ssssss', 'dddddddd')
        expect_result = {'name': 'InvalidBodyError', 'message': 'email não possui um formato correto', 'details': {'message': 'email não possui um formato correto', 'field': 'email'}}
        self.assertEqual(result, expect_result)

    def test_get_manifestations(self):
        result = self.api.get_manifestations(VALIDE_USER, VALIDE_PASSWORD)
        if len(result) > 1:
            result = result[0]
        expect_result = {'id', 'title', 'description', 'startDate', 'endDate', 'private', 'portFacilityId', 'statusManifestation', 'portFacility', 'statistics'}
        self.assertEqual(result.keys(), expect_result)

    def test_get_profile_list(self):
        result = self.api.get_profile_list(VALIDE_USER, VALIDE_PASSWORD)
        expect_result = [{'id': 'CDB8359B-9FB5-42E8-A0E7-8E6F6DE79B37', 'title': 'Área técnica SNP', 'code': 'technical-area-snp'}, {'id': '9771027E-06B4-E711-80E1-00155DB12305', 'title': 'Autoridade Portuária', 'code': 'port-authority'}, {'id': 'B23DF240-47FD-4B26-B335-9B6F055DE8B2', 'title': 'Cidadão', 'code': 'citizen'}, {'id': 'B2FFC902-06B4-E711-80E1-00155DB12305', 'title': 'LabTrans/UFSC', 'code': 'admin-labtrans'}, {'id': '8F3A8E5D-06B4-E711-80E1-00155DB12305', 'title': 'SNP', 'code': 'admin-snp'}, {'id': '2CACBCF9-711F-43AD-B8CD-6341DF03912F', 'title': 'Usuário não confirmado', 'code': 'user-not-confirmed'}]
        self.assertEqual(result, expect_result)

    def test_get_manifest_file(self):
        manifest = self.api.get_manifestations(VALIDE_USER, VALIDE_PASSWORD)
        if len(manifest) > 1:
            for mani in manifest:
                result = self.api.get_manifest_file(VALIDE_USER, VALIDE_PASSWORD, mani['id'])
                self.assertEqual(result.status_code, 200)
        else:
            result = self.api.get_manifest_file(VALIDE_USER, VALIDE_PASSWORD, mani['id'])
            self.assertEqual(result.req.status_code, 200)


if __name__ == '__main__':
    unittest.main()
