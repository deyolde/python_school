from mysql.connector import pooling, Error

class connectionMySQL:
    DATABASE = 'on_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT  = '3306'
    HOST     = 'localhost'
    POOL_SIZE= 5
    POOL_NAME= 'pool_on_fit'
    pool     = None
    
    @classmethod
    def get_pool(cls):
        
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    pool_reset_session=True,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                    database=cls.DATABASE
                )
                return cls.pool
                
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
        
        else:
            return cls.pool

# obtener una conexión del pool
    @classmethod
    def get_connection(cls):
        return cls.get_pool().get_connection()
    
# liberamos la conexión del pool
    @classmethod
    def release_connection(cls, conn):
        conn.close()