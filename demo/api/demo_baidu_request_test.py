import pytest
from httprunner import Parameters
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestBaiduRequestTestCase(HttpRunner):
    @pytest.mark.parametrize("param", Parameters(
        {"username": [111, 222, 333]}
    ))
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("get user list")
            .variables(
            **{
                "username": "${get_username()}"
            }
        )
            .base_url("https://www.baidu.com")
            .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("get info")
                .get("/")
                .with_params(**{"username": "$username"})
                .validate()
                .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    TestBaiduRequestTestCase().test_start()