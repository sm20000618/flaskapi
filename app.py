#employee department details
from flask import Flask, render_template, request, redirect
import MySQLdb
app = Flask(__name__)

#Database configuration 

connectiondb=MySQLdb.connect(
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
        emp_department = emplDetails['emp_department']
        #connection eshtablished by using cursor()
        cursor = connectiondb.cursor()
        cursor.execute("INSERT INTO new_table(emp_id, emp_name, emp_department) VALUES(%s, %s, %s)",(emp_id, emp_name, emp_department))
        connectiondb.commit() cursor.close()
        return redirect('/users')
    return render_template('index.html')
#get the count along with department name
#get method
@app.route('/users')
def users():
    cursor = connectiondb.cursor()
    countdepartment= cursor.execute("SELECT emp_department, COUNT(*) FROM new_table GROUP BY emp_department ")
    if countdepartment > 0:
        Details= cursor.fetchall()
        return render_template('users.html',Details=Details)
#get the name  which is matching with the given pattern
#get method
@app.route('/find')
def findEmployee():
    cursor=connectiondb.cursor()
    findemp=cursor.execute("SELECT emp_name FROM new_table where emp_name like '%na'")
    Details=cursor.fetchall()
    return render_template('users.html',Details=Details)
#get methods
@app.route('/casesensitive)
def caseSensitive():
    cursor=connectiondb.cursor()
    findcs=cursor.execute("SELECT emp_name, COUNT(*) FROM new_table GROUP BY emp_name")
    Details=cursor.fetchall()
    return render_template('users.html',Details=Details)

#main method
if __name__ == '__main__':
    app.run(debug=True)

    
