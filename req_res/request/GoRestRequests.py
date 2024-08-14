from utils.common_utils import CommonUtility


class GoRestRequests:
    CREATE_USER = {
        "name": "Tenali Ramakrishna",
        "gender": "male",
        "email": f"{CommonUtility.get_unique_email()}",
        "status": "active"
    }
