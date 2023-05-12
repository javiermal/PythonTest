import cx_Oracle
con = cx_Oracle.Connection('user1/pswd1@10.123.79.58/Georli03')
cur = cx_Oracle.Cursor(con)
list_of_Id=[100,102,103,104]
try:
    for id in list_of_Id:
        cur.execute("SELECT * FROM Computer WHERE CompId=:c_id",{"c_id":id})
        for CompId,Make,Model,MYear in cur:
            print(Make,CompId)
except cx_Oracle.DatabaseError as e:
    print(e)
finally:
    con.close()