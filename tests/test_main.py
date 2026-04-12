"""
Unit tests for User Management System
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import UserManager

def test_add_user():
    manager = UserManager()
    result = manager.add_user("alice", "alice@example.com")
    assert "successfully" in result
    assert "alice" in manager.users

def test_get_user():
    manager = UserManager()
    manager.add_user("bob", "bob@example.com")
    user = manager.get_user("bob")
    assert user["email"] == "bob@example.com"

if __name__ == "__main__":
    test_add_user()
    test_get_user()
    print("All tests passed!")
