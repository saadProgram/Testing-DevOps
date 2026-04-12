"""
Sample Application for GitFlow Demonstration
Simulates a simple web application with user management
"""

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email):
        """Add a new user to the system"""
        if username in self.users:
            raise ValueError(f"User {username} already exists")

        self.users[username] = {"email": email, "active": True}
        return f"User {username} added successfully"

    def get_user(self, username):
        """Retrieve user information"""
        return self.users.get(username, None)

    def list_users(self):
        """List all active users"""
        return [
            user for user, info in self.users.items()
            if info["active"]
        ]

if __name__ == "__main__":
    manager = UserManager()
    print("User Management System initialized")
