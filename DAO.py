import sqlite3
from cryptography.fernet import Fernet

# Connect to or create a database
def connect_db():
    conn = sqlite3.connect("mydatabase.db")
    return conn

# ================ main user panel ================ #
def get_user_panel():
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * from user_panel;")
        rows = cursor.fetchall()
    except Exception as e:
        return [0,e]
    conn.close()
    print(rows)
    return [1,rows]

def set_user_panel(user_info):
    conn = connect_db()
    cursor = conn.cursor()
    # pass_key = Fernet.generate_key()
    # fernet = Fernet(pass_key)
    # user_info[1] = fernet.encrypt(user_info[1].encode())
    #     command = f"INSERT INTO user_panel values('{user_info[0]}',\
    # '{user_info[1]}','{user_info[1]}','{user_info[2]}','{user_info[3]}');"
    command = "INSERT INTO user_panel values(?,?,?,?,?);"
    print(command)
    user_info.insert(1,user_info[1])
    try:
        cursor.execute(command,user_info)
        conn.commit()
        return [1,"Successfully added a new member"]
    except Exception as e:
        return [0,e]
def updater_user_panel(user_info):
    conn = connect_db()
    cursor = conn.cursor()
    command = f"UPDATE user_panel SET user_name='{user_info[0]}', hash_key='{user_info[1]}',user_password='{user_info[1]}',full_name='{user_info[2]}',role='{user_info[3]}' WHERE user_name = '{user_info[0]}';"
    print(command)
    # user_info.insert(1,user_info[1])
    # user_info.insert(4,user_info[0])
    # print(user_info)
    try:
        cursor.execute(command)
        conn.commit()
        return [1,f"Successfully updated the user , user name = {user_info[0]}"]
    except Exception as e:
        return [0,e]
# --------------------- end --------------------- #

# ================ common method ================ #

def delete_row_of_a_table(table_name,condition_column_name,condion_column_value):
    conn = connect_db()
    cursor = conn.cursor()
    command = f"DELETE FROM {table_name} WHERE {condition_column_name} = '{condion_column_value}';"
    print(command)
    # user_info.insert(1,user_info[1])
    # user_info.insert(4,user_info[0])
    # print(user_info)
    try:
        cursor.execute(command)
        conn.commit()
        return [1,f"Successfully deleted the user , user name = {condion_column_value}"]
    except Exception as e:
        return [0,e]
def get_rows(command):
    conn = connect_db()
    cursor = conn.cursor()
    print(command)
    try:
        cursor.execute(command)
        rows = cursor.fetchall()
        # print(rows)
        return [1,rows]
    except Exception as e:
        print(e)
        return [0,e]
def set_rows(command,values):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(command,values)
        conn.commit()
        return [1,"Successfully added a new one"]
    except Exception as e:
        return [0,e]
def update_rows(command,values):
    print("update : ",values)
    conn = connect_db()
    cursor = conn.cursor()
    # user_info.insert(1,user_info[1])
    # user_info.insert(4,user_info[0])
    # print(user_info)
    try:
        cursor.execute(command,values)
        conn.commit()
        return [1,"Successfully updated"]
    except Exception as e:
        return [0,e]
def delete_rows(command,values):
    conn = connect_db()
    cursor = conn.cursor()
    # user_info.insert(1,user_info[1])
    # user_info.insert(4,user_info[0])
    # print(user_info)
    try:
        cursor.execute(command,values)
        conn.commit()
        return [1,"Successfully Deleted"]
    except Exception as e:
        return [0,e]

# =============== invoice table ==================== #
def get_new_invoice():
    conn = connect_db()
    cursor = conn.cursor()
    command = "SELECT MAX(invoice_number) from invoice;"
    try:
        cursor.execute(command)
        max_number = cursor.fetchall()
        conn.commit()
        return [1,max_number[0][0]]
    except Exception as e:
        return [0,e]
        