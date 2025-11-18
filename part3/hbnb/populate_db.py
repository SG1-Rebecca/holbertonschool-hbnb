from app import create_app
from app.services import facade

def populate_test_data():
    app = create_app()
    
    with app.app_context():
        print("Creating test users...")
        
        # Liste des utilisateurs de test
        test_users = [
            {
                'email': 'john.doe@example.com',
                'password': 'password123',
                'first_name': 'John',
                'last_name': 'Doe',
                'is_admin': False
            },
            {
                'email': 'jane.smith@example.com',
                'password': 'password123', 
                'first_name': 'Jane',
                'last_name': 'Smith',
                'is_admin': False
            },
            {
                'email': 'admin@example.com',
                'password': 'admin123',
                'first_name': 'Admin',
                'last_name': 'User',
                'is_admin': True
            }
        ]
        
        for user_data in test_users:
            try:
                # Vérifier si l'utilisateur existe déjà
                existing_user = facade.get_user_by_email(user_data['email'])
                if existing_user:
                    print(f"User {user_data['email']} already exists")
                    continue
                    
                # Créer l'utilisateur
                user = facade.create_user(user_data)
                print(f"✓ User created: {user.email} (ID: {user.id})")
                
            except Exception as e:
                print(f"✗ Error creating user {user_data['email']}: {e}")

if __name__ == '__main__':
    populate_test_data()