from config.api_config import ApiUrls
from functional_api_test.FunctionalParam import FunctionalParam
from utils.common_utils import CommonUtility


def test_url():
    # url=FunctionalParam.get_base_end_point()
    # print(url)

    # get_url = ApiUrls.GET_USER
    # print(get_url)
    # get_url_by_id = ApiUrls.get_user_by_id(123)
    # print(get_url_by_id)

    # headers=CommonUtility.get_custom_header()
    # print("headers",headers)

    email=CommonUtility.get_unique_email()
    print(email)

test_url()