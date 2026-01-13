import hashlib
import secrets
import hmac
from datetime import date

class AuthService:
    def __init__(self, db):
        self.db = db
        self.iterations = 200_000

    def hash_password(self, password: str, salt_hex: str) -> str:
        salt = bytes.fromhex(salt_hex)
        dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, self.iterations)
        return dk.hex()
    
    def register_user(self, username: str, password: str):
        username = username.strip()
        now = date.today().isoformat()

        if not username or not password:
            raise ValueError("Username and password are required.")

        # check uniqueness
        existing = self.db.fetchone("SELECT 1 FROM users WHERE username = ?", (username,))
        if existing:
            raise ValueError("Username already exists.")

        salt_hex = secrets.token_hex(16)  # 16 bytes salt
        password_hash = self.hash_password(password, salt_hex)

        self.db.execute("""
            INSERT INTO users (username, password_hash, password_salt, created_at)
            VALUES (?, ?, ?,?)
        """, (username, password_hash, salt_hex, now))
    
    
    def authenticate(self, username: str, password: str) -> dict | None:
        username = username.strip()

        row = self.db.fetchone("""
            SELECT user_id, username, password_hash, password_salt, is_active
            FROM users
            WHERE username = ?
        """, (username,))

        if not row or row["is_active"] != 1:
            return None

        expected = row["password_hash"]
        actual = self.hash_password(password, row["password_salt"])

        if not hmac.compare_digest(expected, actual):
            return None

        return {"user_id": row["user_id"], "username": row["username"]}
    

    