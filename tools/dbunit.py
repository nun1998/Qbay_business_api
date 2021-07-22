import pymysql


class DBUnit:
    __conn = None
    __cursor = None

    @classmethod
    def __get_conn(cls):
        if cls.__conn is None:
            cls.__conn = pymysql.connect(
                host="rm-bp14kd81y04x5ks05no.mysql.rds.aliyuncs.com",
                port=3306,
                user="test123",
                password='!Qwer1234',
                database='test_case_business'
            )
        return cls.__conn

    @classmethod
    def __get_cursor(cls):
        if cls.__cursor is None:
            cls.__cursor = cls.__get_conn().cursor()
        return cls.__cursor

    # 执行sql
    @classmethod
    def exe_sql(cls, sql):
        try:
            # 获取游标对象
            cursor = cls.__get_cursor()
            # 调用游标对象的execute方法，执行sql
            cursor.execute(sql)
            # 如果是查询
            if sql.split()[0].lower() == "select":
                # 返回所有数据
                return cursor.fetchall()
            # 否则
            else:
                cls.__conn.commit()
                return cursor.rowsount
        except Exception as e:
            cls.__conn.rollback()
            print(e)
        finally:
            cls.__close_cursor()
            cls.__close_conn()

    @classmethod
    def __close_cursor(cls):
        if cls.__cursor:
            cls.__cursor.close()
            cls.__cursor = None

    @classmethod
    def __close_conn(cls):
        if cls.__conn:
            cls.__conn.close()
            cls.__conn = None


if __name__ == "__main__":
    sql = "select * from sub_account"
    data = DBUnit.exe_sql(sql)
    print(data)
