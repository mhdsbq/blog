import datetime


def get_all_blogs(connection):
    cursor = connection.cursor()
    query = ("SELECT blog_id, title, body, datetime FROM blogs")
    cursor.execute(query)

    response = []
    for (blog_id, title, body, datetime) in cursor:
        response.append(
            {
               "blog_id" : blog_id,
                "title" : title,
                "body" : body,
                "datetime" : datetime
            }
        )

    return response

def get_blog_by_id(connection, blog_id):
    cursor = connection.cursor()
    query = (f"SELECT blog_id, title, body, datetime FROM blogs where blog_id={blog_id}")
    cursor.execute(query)

    response = []
    for (blog_id, title, body, datetime) in cursor:
        response.append(
            {
               "blog_id" : blog_id,
                "title" : title,
                "body" : body,
                "datetime" : datetime
            }
        )

    return response

def insert_new_blog(connection, blog):
    cursor = connection.cursor()
    query = ("INSERT INTO blogs "
             "(title, body, datetime)"
             "VALUES (%s, %s, %s)")

    data = (blog['title'], blog['body'], datetime.datetime.today())
    cursor.execute(query, data)
    connection.commit()

    inserted_blog_id = cursor.lastrowid
    response = get_blog_by_id(connection, blog_id=inserted_blog_id) 

    return response

def delete_blog(connection, blog_id):
    cursor = connection.cursor()
    query = (f"DELETE FROM blogs where blog_id={blog_id}")
    cursor.execute(query)
    connection.commit()
    
    response = blog_id
    return response

def update_blog_by_id(connection, blog):
    cursor = connection.cursor()
    query =(f"UPDATE blogs SET title='{blog['title']}', body='{blog['body']}' WHERE blog_id ='{blog['blog_id']}'")
    cursor.execute(query)
    connection.commit()

    response = blog['blog_id']
    return response
    

if __name__ == "__main__":
    from sql_connection import sql_connection

    connection = sql_connection()

    # print(get_all_blogs(connection))

    # # blog = {
    #     "title" : "3rd_blog",
    #     "body" : "this is my 3nd ever blog in this website",
    #     "datetime" : "2021-09-04 00:00:00"
    # }
    # print(insert_new_blog(connection, blog))


    # print(delete_blog(connection, 1))
    # print(datetime.datetime.today)

    # print(get_blog_by_id(connection, 7))

    # print(update_blog_by_id(connection))