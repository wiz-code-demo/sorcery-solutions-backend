import sqlite3
from typing import Optional

def get_user_by_id(user_id: str) -> Optional[dict]:
    """Vulnerable function with SQL injection"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # SQL injection vulnerability - directly concatenating user input
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return {"id": result[0], "name": result[1], "email": result[2]}
    return None