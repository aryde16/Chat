from datetime import datetime
from settings import MESSAGES


class Message():
    def __init__(self,db,**kw):
        self.collection = db[MESSAGES]
    
    async def save(self,user,msg,**kw):
        result = await self.collection.insert_one({'user':user,'msg':msg,'time':datetime.now()})
        return result

    async def get_messages(self):
        messages = self.collection.find().sort([('time',1)])
        return await messages.to_list(length = None)