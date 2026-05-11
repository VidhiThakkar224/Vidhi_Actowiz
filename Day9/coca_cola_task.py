# username,ful name,imageurl,follwer,fooliwing,like & comments count,reel url,suggest accouts,post,profile pic photo
# Table1 - profile, Table2 -post , Table3 -Related post 
import json
from idlelib.iomenu import encoding

from rich import print
import jmespath

with open("C:\\Python Training\\Day9\\coca_cola_instagram.json","r",encoding="utf-8")as f:
    data = json.load(f)
    coca_cola_data = []

    # for id in jmespath.search("id[*]",data):
    coca_cola_data.append(
        {
            "Profile_Id":jmespath.search("data.user.id",data),
            "User_Name":jmespath.search("data.user.username",data),
            "Full_Name":jmespath.search("data.user.full_name",data),
            "Profile_page_URL":jmespath.search("data.user.profile_pic_url",data),
            "Followers_Count":jmespath.search("data.user.edge_followed_by.count",data),
            "Following_Count":jmespath.search("data.user.edge_follow.count",data),
            "Biography":jmespath.search("data.user.biography",data),
            "BioLinks":[
                {
                    "Bio_Title":jmespath.search("title",link),
                    "Bio_URL":jmespath.search("url",link)

                }   for link in jmespath.search("data.user.bio_links[*]",data)
            ],
            "Total_Post":jmespath.search("data.user.edge_owner_to_timeline_media.count",data),
            "Post":[
                {
                    "Post_id":jmespath.search("node.id",Post), 
                    "Post_URL":"https://www.instagram.com/cocacola/p/" + jmespath.search("node.shortcode",Post),
                    "Post_Like":jmespath.search("node.edge_liked_by",Post),
                    "Post_Commnets":jmespath.search("node.edge_media_to_comment",Post),
                }   for Post in jmespath.search("data.user.edge_owner_to_timeline_media.edges[*]",data)
            ],   
            "Suggested_id":[
                {
                    "Post_id":jmespath.search("node.id",id),
                    "Full_Name":jmespath.search("node.full_name",id),
                    "IS_Private":jmespath.search("node.is_private",id),
                    "IS_Verified":jmespath.search("node.is_verified",id),
                    "Profile_Pic_URL":jmespath.search("node.profile_pic_url",id),
                    "User_Name":jmespath.search("node.username",id)

                }   for id in jmespath.search("data.user.edge_related_profiles.edges[*]",data)
            ]
        }
    )
print(coca_cola_data)


with open('Coca_cola_Data.json', 'w', encoding='utf-8') as f:
    json.dump(coca_cola_data, f, indent=4)

