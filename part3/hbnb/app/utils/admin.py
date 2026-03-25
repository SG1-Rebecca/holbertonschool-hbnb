import os
from app.services import facade


def create_admin_user():
    """
    Create an admin user in the system if it doesn't exist

    Environment variables:
        ADMIN_EMAIL (str): The email address for the admin user
        ADMIN_PASSWORD (str): The password for the admin user
    """
    admin_email = os.getenv('ADMIN_EMAIL')
    admin_password = os.getenv('ADMIN_PASSWORD')

    if admin_email and admin_password:
        if not facade.get_user_by_email(admin_email):
            facade.create_user({
                'first_name': 'Admin',
                'last_name': 'User',
                'email': admin_email,
                'password': admin_password,
                'is_admin': True
            })
            print(f'Admin user created with email: {admin_email}')
        else:
            print(f'Admin user {admin_email} already exists')
    else:
        print('Admin credentials not found in environment variables')
