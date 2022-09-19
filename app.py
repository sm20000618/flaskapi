#employee department details
from flask import Flask, render_template, request, redirect
import MySQLdb
app = Flask(__name__)

# Configure database

conn=MySQLdb.connect(
        host='localhost',
        user='root',
        password = 'Honeyprema@0218',
        db='db1',
        )

@app.route('/', methods=['GET', 'POST'])
def index():
    # request is used to fetch post or get methods
    if request.method == 'POST':
        # Fetch form data
        emplDetails = request.form
        emp_id = emplDetails['emp_id']
        emp_name = emplDetails['emp_name']
        emp_dept = emplDetails['emp_dept']
        # cur = mysql.connection.cursor()
        #connection eshtablished by using cursor()
        cur = conn.cursor()
        cur.execute("INSERT INTO new_table(emp_id, emp_name, emp_dept) VALUES(%s, %s, %s)",(emp_id, emp_name, emp_dept))
        conn.commit()

        cur.close()
        return redirect('/users')
    return render_template('index.html')
#get the count along with department name
#get method
@app.route('/users')
def users():
    cur = conn.cursor()
    countdepartment= cur.execute("SELECT emp_dept, COUNT(*) FROM new_table GROUP BY emp_dept ")
    if countdepartment > 0:
        Details= cur.fetchall()
        return render_template('users.html',Details=Details)
#get the name  which is matching with the given pattern
#get method
@app.route('/find')
def findEmployee():
    cur=conn.cursor()
    findemp=cur.execute("SELECT emp_name FROM new_table where emp_name like '%na'")
    Details=cur.fetchall()
    return render_template('users.html',Details=Details)
#main method
if __name__ == '__main__':
    app.run(debug=True)

    