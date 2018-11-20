import allure,pytest

class Test_001:
    @allure.step(title="练习例子")
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test001_1(self):
        allure.attach("登录用户名","用户名是lily")
        allure.attach("登录密码", "密码是123456")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test001_2(self):
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test001_3(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test001_4(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test001_5(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test001_6(self):
        assert True