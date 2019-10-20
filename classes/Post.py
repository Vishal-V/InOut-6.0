from DBWrapper import DBWrapper
# from ServerSide.AI.sentiment_analyzer import predict

class Post(DBWrapper):
    TABLE_NAME = "POST"

    def __init__(self, username, title, content, posted, picture, profile_pic, likes=0, post_id=None):
        super().__init__()
        self.username = username
        self.title = title
        self.content = content
        self.posted = posted
        self.picture = picture
        self.profile_pic = profile_pic
        self.likes = likes
        self.post_id = post_id
        sentiment = predict(self.content)
        self.sentiment = list(sentiment.keys())[0]
        self.sentiment_score = sentiment[self.sentiment]

    def upload(self):
        self.cursor.execute('''
            INSERT INTO POST(username, title, content, posted, picture, profile_pic, likes, sentiment, sentiment_score) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);

        ''', (self.username, self.title, self.content, self.posted, self.picture, self.profile_pic, self.likes, self.sentiment, self.sentiment_score))

    @staticmethod
    def create_table():
        DBWrapper.exec_query('''
           create table POST(
                username varchar(15),
                title varchar(120) not null,
                content text,
                posted varchar(40),
                picture varchar(150),
                profile_pic varchar(150),
                likes integer,
                post_id serial primary key,
                sentiment varchar(3),
                sentiment_score real,
                constraint fk_post foreign key(username)
                    references USERS(username)
                    on delete cascade
            );
        ''')

    @staticmethod
    def drop_table():
        DBWrapper.exec_query('''
            DROP TABLE POST;
        ''')
