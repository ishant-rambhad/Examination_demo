from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['Examination_app']
print(db.list_collection_names())
# 

# migrations.AlterField(
#     model_name='studentdetails',
#     name='id',
#     field=models.BigAutoField(primary_key=True),
# ),