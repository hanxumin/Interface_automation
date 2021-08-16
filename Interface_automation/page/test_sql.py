from Base.collect_sql import connect_sql, show_database, show_table, desc_table, insert_into, select_table, \
    delete_table, num2


class sql_frame():
    """
    # 连接数据库并创建游标
    conn = connect_sql("books")
    cursor = conn.cursor()
    # 查看所有的数据库
    cursor.execute(show_database())
    print('1、查看所有数据库:', cursor.fetchall())
    print(num2)
    # 查看所有的数据表
    cursor.execute(show_table())
    print('2、查看所有数据表:', cursor.fetchall())
    print(num2)
    # 查看表结构
    cursor.execute(desc_table('han'))
    print('3、查看数据表的表结构:', cursor.fetchall())
    print(num2)
    # 插入数据
    cursor.execute(insert_into("han", 1))
    conn.commit()
    print(num2)
    # 查询整表
    cursor.execute("select * from han ;")
    num_list = []
    for i in cursor.fetchall():
        num_list.append(i)
    print('4、查看数据:', num_list)
    print(num2)
    # 查询整表并筛选id
    cursor.execute(select_table("id", "han where id = 1"))
    print('5、查看数据:', cursor.fetchall())
    print(num2)
    # 删除数据表
    print(num2)
    cursor.execute(delete_table("han", where=" where id = 1"))
    conn.commit()
    print(num2)
    # 查询表
    cursor.execute(select_table("id", "han"))
    conn.commit()
    print('6、查看数据:', cursor.fetchall())
    conn.commit()
    print(num2)
    # 关闭游标，关闭数据库连接
    cursor.close()
    conn.close()
    """
    def __init__(self,database,table):
        self.database=database
        self.table=table

    def run_sql(self):
        # 连接数据库并创建游标
        conn = connect_sql(self.database)
        cursor = conn.cursor()
        # 查看所有的数据库
        cursor.execute(show_database())
        print('1、查看所有数据库:', cursor.fetchall())
        print(num2)
        # 查看所有的数据表
        cursor.execute(show_table())
        print('2、查看所有数据表:', cursor.fetchall())
        print(num2)
        # 查看表结构
        cursor.execute(desc_table(self.table))
        print('3、查看数据表的表结构:', cursor.fetchall())
        print(num2)
        # 插入数据
        cursor.execute(insert_into("han", str(67)))
        conn.commit()
        print(num2)

        # 查询整表
        cursor.execute("select * from han ;")
        num_list = []
        for i in cursor.fetchall():
            num_list.append(i)
        print('4、查看数据:', num_list)
        print(num2)
        # 查询整表并筛选id
        cursor.execute(select_table("id", "han where id = 1"))
        print('5、查看数据:', cursor.fetchall())
        print(num2)
        # 删除数据表
        print(num2)
        cursor.execute(delete_table("han", where=" where id = 1"))
        conn.commit()
        print(num2)
        # 查询表
        cursor.execute(select_table("id", "han"))
        conn.commit()
        print('6、查看数据:', cursor.fetchall())
        conn.commit()
        print(num2)
        # 关闭游标，关闭数据库连接
        cursor.close()
        conn.close()



if __name__ == '__main__':
    sql = sql_frame('books','han')
    sql.run_sql()

