import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('instance/library.db')
cursor = conn.cursor()

# Admin details
admin_name = 'Admin'
admin_email = 'sritadmin@gmail.com'
admin_password = 'admin123'
admin_role = 'admin'  # Added role field

# Check if admin already exists
cursor.execute("SELECT * FROM users WHERE email = ?", (admin_email,))
existing = cursor.fetchone()

if existing:
    # Update existing admin record
    cursor.execute(
        "UPDATE users SET name = ?, password = ?, role = ? WHERE email = ?",
        (admin_name, admin_password, admin_role, admin_email)
    )
    print("🔁 Admin user updated.")
else:
    # Insert new admin user with all required fields
    cursor.execute(
        "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
        (admin_name, admin_email, admin_password, admin_role)
    )
    print("✅ Admin user inserted successfully.")

# Save and close
conn.commit()
conn.close()
