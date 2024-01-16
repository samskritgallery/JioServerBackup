import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb_SanskritGallery1 = myclient["SanskritGallery"]
mycol_granthapp_treemenu = mydb_SanskritGallery1["granthapp_treemenu"]
mycol_test = mydb_SanskritGallery1["test"]
mycol_test_menu = mydb_SanskritGallery1["test-menu"]
mycol_test_meta = mydb_SanskritGallery1["test-meta"]
      
"""mycol_granthapp_treemenu.delete_many({})
with open('granthapp_treemenu.json') as file0:
	file_data = json.load(file0)
    
mycol_granthapp_treemenu.insert_many(file_data)
file0.close()
"""

x=mycol_test.delete_many({})
print(x.deleted_count, "documents deleted")

with open('testcollection_v3.json') as file1:
	file_data1 = json.load(file1)
    
mycol_test.insert_many(file_data1)
file1.close()

"""
mycol_test_menu.delete_many({})
with open('testcollection_menu_v1.json') as file2:
	file_data2 = json.load(file2)
    
mycol_test_menu.insert_many(file_data2)
file2.close()

mycol_test_meta.delete_many({})
with open('testcollection_meta_v1.json') as file3:
	file_data3 = json.load(file3)
    
mycol_test_meta.insert_many(file_data3)
file3.close()
"""

for db in myclient.list_databases():
	print(db)
    	


for coll in mydb_SanskritGallery1.list_collection_names():
	print(coll)

myclient.close()
