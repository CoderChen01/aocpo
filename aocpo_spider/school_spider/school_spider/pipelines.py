import pymongo

class SchoolSpiderPipeline(object):
    def __init__(self, mongo_url, mongo_db, mongo_col):
        self._mongo_url = mongo_url
        self._mongo_db = mongo_db
        self._mongo_col = mongo_col
        self._db = None
        self._client = None
        self._col = None

    @classmethod
    def from_crawler(cls, crawler):
        """
        实例化数据库
        """
        return cls(crawler.settings.get('MONGO_URI'), crawler.settings.get('MONGO_DATABASE_SCHOOL_NAME'),
                   crawler.settings.get('MONGO_DATABASE_SCHOOL_COLLECTION_NAME'))

    def open_spider(self, spider):
        self._client = pymongo.MongoClient(self._mongo_url)
        self._db = self._client[self._mongo_db]
        self._col = self._db[self._mongo_col]
        self._col.create_index([('school', pymongo.ASCENDING), ('ranking', pymongo.ASCENDING)], name = 'school_1')


    def process_item(self, item, spider):
        print(self._col.update_one({'school':item.get('school')}, {'$setOnInsert':item}, True).upserted_id)
        return item

    def close_spider(self, spider):
        self._client.close()