import requests
from django.conf import settings

class EmailJSService:
    def __init__(self):
        self.service_id = settings.EMAILJS_SERVICE_ID
        self.user_id = settings.EMAILJS_USER_ID
        self.api_url = 'https://api.emailjs.com/api/v1.0/email/send'

    def send_email(self,  template_id, template_params):
        email_data = {
            'service_id': self.service_id,
            'template_id': template_id,
            'user_id': self.user_id,
            'template_params': template_params
        }
        try:
            headers = {
                'Content-Type': 'application/json',
                # 'Host': 'algofact.tech',
                # 'Authorization': f'Bearer {settings.EMAILJS_API_KEY}'
            }
            response = requests.post(self.api_url, json=email_data, headers=headers)
            response.raise_for_status()
        
            return response
         
        except Exception as e:
            print(f"Error sending email: {e}")
            return None


    def send_verification_code_email(self, to_email,name, verification_code):
        template_id = "luwian_verification_code"
        template_params = {
            'email': to_email,
            'code': f"{verification_code}",
            'name': f"{name}",
        }
        return self.send_email(template_id, template_params)

    def send_account_verification(self, to_email, token):
        template_id = "account_verification"
        template_params = {
            'email': to_email,
            'token': token,
            'url':f"{settings.FRONTEND_URL}/account-verification/",
            
        }
        return self.send_email(template_id, template_params)

    
    def send_account_credentials(self, to_email, password):
        template_id = "account_credential"
        template_params = {
            'email': to_email,
            'password': password,
            'url':f"{settings.FRONTEND_URL}",
        }
        return self.send_email(template_id, template_params)