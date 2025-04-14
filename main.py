from user_profiles import users
from newsletter_generator import generate_newsletter

if __name__ == "__main__":
    for user in users:
        print(f"Generating newsletter for {user['name']}...")
        generate_newsletter(user)
    print("All newsletters saved in /output")
