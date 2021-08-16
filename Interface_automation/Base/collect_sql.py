import pymysql
import time

time1 = time.strftime('%Y/%m/%d-%H:%M:%S')
print(time1)


def connect_sql(database, user='root', password='123456', port=3306, host='localhost', charset='utf8',
                autocommit=False):
    conn = pymysql.connect(database=database, user=user, password=password, port=port, host=host, charset=charset,
                           autocommit=autocommit)
    return conn


def show_database():
    "查询数据库"
    sql = "show databases;"
    num = '-' * 30 + '>'
    print("show_database {}成功。".format(num), sql)
    return sql


def create_database(database):
    "创建数据库"
    sql = "create database {};".format(database)
    num = '-' * 30 + '>'
    print("create_database {} {}成功。".format(database, num), sql)
    return sql


def drop_database(database):
    "删除数据库"
    sql = "drop database {};".format(database)
    num = '-' * 30 + '>'
    print("drop_database {} {}成功。".format(database, num), sql)
    return sql


def alter_database(database, character_set='utf8mb4', proof_rule='utf8mb4_general_ci'):
    "修改数据库编码格式"
    sql = "alter database {} default character set {} default collate {};".format(database, character_set, proof_rule)
    num = '-' * 30 + '>'
    print("alter_database {}{}{} {}成功。".format(database, character_set, proof_rule, num), sql)
    return sql


def create_table(table, values):
    "创建数据表"
    sql = "create table {}({});".format(table, values)
    # create table liyafeng(name varchar(5),age int(3),sex varchar(2));
    num = '-' * 30 + '>'
    print("create_table {}{} {}成功。".format(table, values, num), sql)
    return sql


def show_table():
    "查询数据"
    sql = "show tables;"
    num = '-' * 30 + '>'
    print("show_table {}成功。".format(num), sql)
    return sql


def desc_table(table):
    "查询表结构"
    sql = "desc {};".format(table)
    num = '-' * 30 + '>'
    print("desc_table {} {}成功。".format(table, num), sql)
    return sql


def insert_into(database_table, values):
    "插入数据"
    sql = f'INSERT INTO ' + str(database_table) + ' VALUES(' + values + ');'
    # sql = f"INSERT INTO `books`.`hanxumin` (`name`, `age`, `sex`) VALUES {values};"
    # sql = "insert into {} values{};".format(database_table, tuple(values))
    num = '-' * 30 + '>'
    print("insert_into {}({}) {}成功。".format(database_table, values, num), sql)
    return sql


def update_table(table, old_values, new_values):
    "修改数据"
    sql = "update {} set {} ".format(table, old_values, new_values)
    num = '-' * 30 + '>'
    print("update_table {} {}成功。".format(table, old_values, new_values, num), sql)
    return sql


def select_table(find, select_num, where="", group_by="", having="", order_by="", limit=""):
    "查询数据"
    # sql = "select {}".format(select_num) + "from {}".format(args) + ";"
    sql = "select {} from {} {} {} {};".format(find, select_num, where, group_by, having, order_by, limit)
    num = '-' * 30 + '>'
    print(
        "查询：{},\n 表:{},\n查询条件:{},\n分组对象:{},\n分组后筛选条件:{},\n排序条件:{},\n取多少行:{},\n{}成功。".format(find, select_num, where,
                                                                                            group_by, having, order_by,
                                                                                            limit, num), sql)
    return sql


def drop_table(table):
    "删除表"
    sql = "drop table {};".format(table)
    num = '-' * 30 + '>'
    print("drop_table {} {}成功".format(table, num), sql)
    return sql


def delete_table(table, where=""):
    "删除表数据：自增长字段不会从头开始计数"
    sql = "delete from {} {};".format(table, where)
    num = '-' * 30 + '>'
    print("delete_table {} {}成功。".format(table, where, num), sql)
    return sql


def num_print(num3):
    if num3 == '-':
        num = '-' * 30 + '>'
        print(num)
    elif num3 == '*':
        num = "*" * 100
        print(num)
    else:
        pass
    return


num = '-' * 30 + '>'
num2 = "*" * 100
f"""
只查看第一条数据 {num}print(cursor.fetchone())
查看所有数据 {num}print(cursor.fetchall())
"""


class sql_frame():
    #     """
    #     # 连接数据库并创建游标
    #     conn = connect_sql("books")
    #     cursor = conn.cursor()
    #     # 查看所有的数据库
    #     cursor.execute(show_database())
    #     print('1、查看所有数据库:', cursor.fetchall())
    #     print(num2)
    #     # 查看所有的数据表
    #     cursor.execute(show_table())
    #     print('2、查看所有数据表:', cursor.fetchall())
    #     print(num2)
    #     # 查看表结构
    #     cursor.execute(desc_table('han'))
    #     print('3、查看数据表的表结构:', cursor.fetchall())
    #     print(num2)
    #     # 插入数据
    #     cursor.execute(insert_into("han", 1))
    #     conn.commit()
    #     print(num2)
    #     # 查询整表
    #     cursor.execute("select * from han ;")
    #     num_list = []
    #     for i in cursor.fetchall():
    #         num_list.append(i)
    #     print('4、查看数据:', num_list)
    #     print(num2)
    #     # 查询整表并筛选id
    #     cursor.execute(select_table("id", "han where id = 1"))
    #     print('5、查看数据:', cursor.fetchall())
    #     print(num2)
    #     # 删除数据表
    #     print(num2)
    #     cursor.execute(delete_table("han", where=" where id = 1"))
    #     conn.commit()
    #     print(num2)
    #     # 查询表
    #     cursor.execute(select_table("id", "han"))
    #     conn.commit()
    #     print('6、查看数据:', cursor.fetchall())
    #     conn.commit()
    #     print(num2)
    #     # 关闭游标，关闭数据库连接
    #     cursor.close()
    #     conn.close()
    #     """
    def __init__(self, database):
        self.database = database

    def show(self):
        # 连接数据库并创建游标
        self.conn = connect_sql(self.database)
        self.cursor = self.conn.cursor()
        # 查看所有的数据库
        self.cursor.execute(show_database())
        print('1、查看所有数据库:', self.cursor.fetchall())
        print(num2)
        # 查看所有的数据表
        self.cursor.execute(show_table())
        print('2、查看所有数据表:', self.cursor.fetchall())
        print(num2)
        return

    def desc_table(self, table):
        # 查看表结构
        self.cursor.execute(desc_table(table))
        print('3、查看数据表的表结构:', self.cursor.fetchall())
        print(num2)
        return

    def drop_table(self, table):
        # 删除整表
        self.cursor.execute(drop_table(table))
        self.conn.commit()
        print(num2)
        return

    def create_table(self, table, values):
        self.cursor.execute(create_table(table, values))
        self.conn.commit()
        print(num2)
        return

    def input_table(self, table, values_list):
        # 插入数据
        # print(values_list)
        self.cursor.execute(insert_into(self.database + '.' + table, tuple(values_list)))
        self.conn.commit()
        print(num2)
        return

    def run_sql(self, table):
        # 查询整表
        self.cursor.execute("select * from {} ;".format(table))
        num_list = []
        for i in self.cursor.fetchall():
            num_list.append(i)
        print('5、查看数据:', num_list)
        print(num2)
        return

    def delete_sql(self, table, where=""):
        """删除数据表"""
        self.cursor.execute(delete_table(table, where))
        self.conn.commit()
        print('7、', num2)

    def select_sql(self, find, select_num, where="", group_by="", having="", order_by="", limit=""):
        """查询表 示例：sql.select_table('*', 'hanxumin',where="where 'name=hanxumin'")"""
        self.cursor.execute(select_table(find, select_num, where, group_by, having, order_by, limit))
        self.conn.commit()
        print('8、查看数据:', self.cursor.fetchall())
        self.conn.commit()
        print(num2)
        return

    def conn_close(self):
        # 关闭游标，关闭数据库连接
        self.cursor.close()
        self.conn.close()
        return

    def sql(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        print('7、', sql, "\n", num2)


if __name__ == '__main__':
    sql = sql_frame("books")
    sql.show()
    sql.drop_table('hanxumin')
    sql.create_table('hanxumin', 'name varchar(5),age int(3),sex varchar(2)')
    sql.desc_table('hanxumin')
    sql.sql('INSERT INTO books.hanxumin VALUES (NULL, NULL, NULL);')
    sql.input_table('hanxumin(name,age)', ['han', 1])
    # sql.delete_sql('hanxumin', 'where name is not null')
    sql.run_sql('hanxumin')
    sql.select_sql('*', 'hanxumin', where="where name='han'")
    sql.conn_close()
# # 连接数据库并创建游标
# conn = connect_sql("books")
# cursor = conn.cursor()
# # 查看所有的数据库
# cursor.execute(show_database())
# print('1、查看所有数据库:', cursor.fetchall())
# print(num2)
# # 查看所有的数据表
# cursor.execute(show_table())
# print('2、查看所有数据表:', cursor.fetchall())
# print(num2)
# # 查看表结构
# cursor.execute(desc_table('han'))
# print('3、查看数据表的表结构:', cursor.fetchall())
# print(num2)
# # 插入数据
# cursor.execute(insert_into("han", 1))
# conn.commit()
# print(num2)
# # 查询整表
# cursor.execute("select * from han ;")
# num_list = []
# for i in cursor.fetchall():
#     num_list.append(i)
# print('4、查看数据:', num_list)
# print(num2)
# # 查询整表并筛选id
# cursor.execute(select_table("id", "han where id = 1"))
# print('5、查看数据:', cursor.fetchall())
# print(num2)
# # 删除数据表
# print(num2)
# cursor.execute(delete_table("han", where=" where id = 1"))
# conn.commit()
# print(num2)
# # 查询表
# cursor.execute(select_table("id", "han"))
# conn.commit()
# print('6、查看数据:', cursor.fetchall())
# conn.commit()
# print(num2)
# # 关闭游标，关闭数据库连接
# cursor.close()
# conn.close()
# INSERT INTO `books`.`hanxumin` (`name`, `age`, `sex`) VALUES (NULL, NULL, NULL);
