from .DBWrapper import DBWrapper
from flask_login import UserMixin, current_user

class User(DBWrapper, UserMixin):
    TABLE_NAME = "USERS"

    def __init__(self, username, password, email, profile_pic='default.jpg', misc='default.jpg', id=None):
        super().__init__()
        self.username = username
        self.password = password
        self.email = email
        self.profile_pic = profile_pic
        self.misc = misc
        self.id = id


    # Push current object onto DB
    def upload(self):
        self.cursor.execute('''
            INSERT INTO USERS(username, password, email, profile_pic, misc) VALUES (%s, %s, %s, %s, %s);
        ''', (self.username, self.password, self.email, self.profile_pic, self.misc))


    # Fetch an entry from DB, and return it as a python object of this class
    @staticmethod
    def fetch(email):
        DBWrapper.cursor.execute('''
            SELECT * FROM USERS WHERE email=(%s);
        ''', (email,))

        rec = DBWrapper.cursor.fetchone()
        if rec is None:
            return None

        return User(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5])


    @staticmethod
    def fetch_username(username):
        DBWrapper.cursor.execute('''
            SELECT * FROM USERS WHERE username=(%s);
        ''', (username,))

        rec = DBWrapper.cursor.fetchone()
        if rec is None:
            return None

        return User(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5])        

    @staticmethod
    def fetch_userid(user_id):
        DBWrapper.cursor.execute('''
            SELECT * FROM USERS WHERE id=(%s);
        ''', (user_id,))

        rec = DBWrapper.cursor.fetchone()
        if rec is None:
            return None

        return User(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5]) 


    def update_value(image, username):
        DBWrapper.cursor.execute('''
            UPDATE PROFILE
            SET profile_pic=(%s)
            WHERE username=(%s);
        ''', (image, username))


    #This method defies logic, but it works. It is an overrride
    def get_id(self):
        DBWrapper.cursor.execute('''
            SELECT * FROM USERS WHERE id=(%s);
        ''', (self.id,))

        rec = DBWrapper.cursor.fetchone()
        if rec is None:
            return None

        user1 = User(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5])  
        return (rec[5])


    @staticmethod
    def create_table():
        DBWrapper.exec_query('''
            create table USERS(
                username varchar(15) primary key,
                password varchar(100) not null,
                email varchar(30) not null unique,
                profile_pic varchar(150),
                misc varchar(30),
                id serial,
                constraint password_length check(length(password)>=5)
            );

        ''')

    @staticmethod
    def drop_table():
        DBWrapper.exec_query('''
            DROP TABLE USERS;
        ''')
