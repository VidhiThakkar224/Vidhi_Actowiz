import mysql.connector
import json
from rich import print

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="actowiz", 
    database="cocacola"
)

cursor = conn.cursor()

with open("C:\\Python Training\\Day9\\Coca_cola_Data.json","r",encoding="utf-8")as f:
    data = json.load(f)

    # for item in data:
    #     Profile_data = (item.get("Profile_Id"),item.get("User_Name"),item.get("Full_Name"),item.get("Profile_page_URL"),
    #                 item.get("Followers_Count"),item.get("Following_Count"),item.get("Biography"),item.get("Total_Post"))       
        
    # for item in data[0].get('Post'):
    #     Post_data = (item.get("Post_id"),item.get("Post_URL"),item.get("Post_Like").get('count'),
    #     item.get("Post_Commnets").get('count'))
    #     print (Post_data)

    for item in data[0].get('Suggested_id'):
        Suggested_id = (item.get("Post_id"),item.get("Full_Name"),item.get("IS_Private"),
                        item.get("IS_Verified"),item.get("Profile_Pic_URL"),item.get("User_Name"))
        print(Suggested_id)

        # try:
        #     cursor.execute("""
        #                 insert into cocacola_profile(
        #                    Profile_Id,
        #                    User_Name,
        #                    Full_Name,
        #                    Profile_page_URL,
        #                    Followers_Count,
        #                    Following_Count,
        #                    Biography,
        #                    Total_Post
        #                    ) values (%s, %s, %s, %s, %s, %s, %s ,%s)
        #                 """,Profile_data)
#         
# try:
#             cursor.execute("""
#                        insert into post(
#                            Post_id,
#                            Post_URL,
#                            Post_Like,
#                            Post_Comments
#                            ) values (%s, %s, %s, %s)

# """,Suggested_id) 

        try:
            cursor.execute("""
                        insert into Suggested_id(
                           Post_id,
                           Full_Name,
                           IS_Private,
                           IS_Verified,
                           Profile_Pic_URL,
                           User_Name
                           ) values (%s, %s, %s, %s, %s, %s)
""", Suggested_id)
            print("data inserted ")
            
        except Exception as e:
            print(" Error inserting:", e)

conn.commit()
cursor.close()
conn.close()