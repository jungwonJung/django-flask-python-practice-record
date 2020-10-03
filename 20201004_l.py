import pymysql
#데이터 삭제 쿼리문
conn = pymysql.connect(host="localhost", user="root", password="111111", db="youtube", charset="utf8")
#db작업이 끝나면 무적권 삭제
try:
    curs = conn.cursor()
    sql = """delete from user where region=%s"""
    curs.execute(sql, '금산')
    conn.commit()


    sql2= "select * from user order by no"
    curs.execute(sql2)
    rows = curs.fetchall()
    print(rows)
finally:
    conn.close()
#exit()

##############################################
#데이터 업데이트 쿼리문

# conn = pymysql.connect(host="localhost", user="root", password="111111", db="youtube", charset="utf8")
# curs = conn.cursor()
# sql = """update user set region='서울특별시' where region='서울'"""
# curs.execute(sql)
# conn.commit()
#
#
# sql2= "select * from user order by no"
# curs.execute(sql2)
# rows = curs.fetchall()
# print(rows)
# conn.close()
# exit()
#

##############################################


# 데이터 입력 방법

# conn = pymysql.connect(host="localhost", user="root", password="111111", db="youtube", charset="utf8")
# curs = conn.cursor()
# sql = """insert into user(id, name, region, insdt)
#         values (%s, %s, %s, now())"""
# curs.execute(sql, ('test10', '테스트10', '천안'))
# curs.execute(sql, ('test11', '테스트11', '아산'))
# curs.execute(sql, ('test12', '테스트12', '금산'))
# conn.commit()
#
#
# sql2= "select * from user order by no"
# curs.execute(sql2)
# rows = curs.fetchall()
# print(rows)
# conn.close()
# exit()
########################################################

#데이터 확인 읽는법


# curs = conn.cursor(pymysql.cursors.DictCursor)
# sql ="select * from user where region=%s"
# curs.execute(sql, '서울')
# rows = curs.fetchall()
# print(rows)
#
# for row in rows:
#     print(row)
#     print(row['no'], row['id'], row['name'])
#
# conn.close()