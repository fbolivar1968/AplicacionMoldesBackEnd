import requests
from msal import ConfidentialClientApplication
from django.conf import settings


class MicrosoftGraphService:

    def __init__(self):

        self.client = ConfidentialClientApplication(
            client_id=settings.GRAPH_CLIENT_ID,
            authority=f"https://login.microsoftonline.com/{settings.GRAPH_TENANT_ID}",
            client_credential=settings.GRAPH_CLIENT_SECRET
        )

    def get_token(self):

        result = self.client.acquire_token_for_client(
            scopes=["https://graph.microsoft.com/.default"]
        )

        if "access_token" not in result:
            raise Exception(result)

        return result["access_token"]

    def search_op_pdf(self, consecutivo):
        token = self.get_token()

        headers = {
            "Authorization": f"Bearer {token}"
        }

        url = (
            "https://graph.microsoft.com/v1.0/drives/"
            f"{settings.GRAPH_DRIVE_ID}"
            f"/root/search(q='{consecutivo}')"
        )
        response = requests.get(
            url,
            headers=headers
        )
        response.raise_for_status()
        data = response.json()

        items = data.get("value", [])
        for item in items:
            name = item.get("name", "")
            if name.startswith(str(consecutivo)):
                return {
                    "name": name,
                    "url": item.get("webUrl")
                }

        return None
        