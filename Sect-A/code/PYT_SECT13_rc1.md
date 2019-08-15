
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, 김진수</font></div>
<hr>

## <font color='brown'>데이터베이스, DB SQL</font>
>  
- 데이터베이스 및 테이블 생성
- 데이터 생성, INSERT
- 데이터 조회, SELECT
- 데이터 갱신, UPDATE
- 데이터 삭제, DELETE

## SQLITE3
<!--
# sqlite3 command

> pip install sqlite
> pip install dataset

> sqlite3 ./database/my_books.db

sqlite> .help
sqlite> .databases
sqlite> .tables
sqlite> .schema my_books
CREATE TABLE my_books (
    title text,
    published_date text,
    publisher text,
    pages integer,
    recommendation integer
);
sqlite> .quit
/-->


```python
import sqlite3  

db_name = './database/my_books.db'
```

### 테이블 생성


```python
def create_table(db_name, db_sql):
    """
    데이터베이스 테이블을 생성하는 함수
    Args:
        db_name : Database Name
        db_sql  : Query for creating Table
    Returns : 
        is_success : Boolean 
    """
    is_success = True
    
    try :
        # 데이터베이스 커넥션 생성
        conn = sqlite3.connect(db_name)  

        # 커서 확보
        cur = conn.cursor()  

        # 테이블 생성
        cur.execute(db_sql)
    
    # except OperationalError as e:
    #     is_success = False
    #     print('Error:', e)
        
    except:
        is_success = False
        print("Database Error!")
        
    finally :        
        if is_success:
            # 데이터베이스 반영
            conn.commit()  
        else:
            # 데이터베이스 철회
            conn.rollback()
            
        # 데이터베이스 커넥션 닫기
        # print('Finish process of function.')
        conn.close()
    
    return is_success

# if __name__ == "__main__":  # 외부에서 호출 시
#     create_table()          # 테이블 생성 함수 호출

```


```python
if create_table(db_name, db_sql=None):
    print('테이블이 성공적으로 생성되었습니다.')
else :
    print('테이블이 생성되지 않았습니다.')
```

    Database Error!
    테이블이 생성되지 않았습니다.
    


```python
db_sql  = '''
CREATE TABLE my_books (
    title text,
    published_date text,
    publisher text,
    pages integer,
    recommendation integer
)
'''

if create_table(db_name, db_sql):
    print('테이블이 성공적으로 생성되었습니다.')
else :
    print('테이블이 생성되지 않았습니다')
```

    테이블이 성공적으로 생성되었습니다.
    

### 데이터 등록


```python
import sqlite3  

# 데이터 입력 함수
def insert_books(db_name):
    """
    데이터베이스 테이블에 데이터를 등록하는 함수
    Args:
        db_name : Database Name
    Returns : 
        is_success : Boolean 
    """
    is_success = True
    
    try:
        # 데이터베이스 커넥션 생성
        conn = sqlite3.connect(db_name) 

        # 커서 확보
        cur = conn.cursor()  

        # 데이터 입력 SQL1
        db_sql = "INSERT INTO my_books VALUES ('메가트랜드', '2002.03.02','A', 200, 0)"
        cur.execute(db_sql)

        # 데이터 입력 SQL2
        db_sql = 'INSERT INTO my_books VALUES (?, ?, ?, ?, ?)'
        cur.execute(db_sql, ('인더스트리 4.0', '2016.07.09','B', 584, 1))

        # # 데이터 입력 SQL3
        books = [
            ('유니콘 스타트업', '2011.07.15','A', 248, 1),
            ('빅데이터 마케팅', '2012.08.25','A', 296, 1),
            ('사물인터넷 전망', '2013.08.22','B', 526, 0)
        ]
        cur.executemany(db_sql, books)
          
    except:
        is_success = False
        print("Database Error!")
        
    finally :      
        if is_success:
            # 데이터베이스 반영
            conn.commit()  
        else:
            # 데이터베이스 철회
            conn.rollback()
            
        # 데이터베이스 커넥션 닫기
        # print('Finish process of function.')
        conn.close()
    
    return is_success    
    
# if __name__ == "__main__":          # 외부에서 호출 시
#     insert_books()                  # 데이터 입력 함수 호출

```


```python
if insert_books(db_name):
    print('데이터가 성공적으로 등록되었습니다.')
else :
    print('데이터가 등록되지 않았습니다')
```

    데이터가 성공적으로 등록되었습니다.
    

### 데이터 조회
title          = list()
published_date = list()
publisher      = list()
pages          = list()
recommendation = list()

column_name = ['title', 'published_date', 'publisher', 'pages', 'recommendation']
for book in books:
    # print(book)
    # for value in book:
    #     print(value, end=" | ")
    title         .append(book[0])
    published_date.append(book[1])
    publisher     .append(book[2])
    pages         .append(book[3])
    recommendation.append(book[4])
    
data = {
    'title'          : title         ,
    'published_date' : published_date,
    'publisher'      : publisher     ,
    'pages'          : pages         ,
    'recommendation' : recommendation
}

ret_df = pd.DataFrame(data, columns=column_name)
ret_df

```python
import pandas as pd

def getBooksDF(books):
    ret_df = pd.DataFrame()
    
    title          = list()
    published_date = list()
    publisher      = list()
    pages          = list()
    recommendation = list()

    column_name = ['title', 'published_date', 'publisher', 'pages', 'recommendation']
    for book in books:
        # print(book)
        # for value in book:
        #     print(value, end=" | ")
        title         .append(book[0])
        published_date.append(book[1])
        publisher     .append(book[2])
        pages         .append(book[3])
        recommendation.append(book[4])

    data = {
        'title'          : title         ,
        'published_date' : published_date,
        'publisher'      : publisher     ,
        'pages'          : pages         ,
        'recommendation' : recommendation
    }

    ret_df = pd.DataFrame(data, columns=column_name)
    
    return ret_df

```


```python
import sqlite3
import pandas as pd

def select_all_books(db_name):
    """
    전체 데이터를 조회하는 함수
    Args:
        db_name : Database Name
    Returns :
        is_success : Boolean 
        ret_df : DataFrame of books
    """
    ret_df = pd.DataFrame()
    is_success = True
    
    try:
        # 데이터베이스 커넥션 생성
        conn = sqlite3.connect(db_name) 

        # 커서 확보
        cur = conn.cursor()  

        # 조회용 SQL 실행
        db_sql = "SELECT * FROM my_books"
        cur.execute(db_sql) 

        # 조회한 데이터 불러오기
        print('[1] 전체 데이터 출력하기')
        books = cur.fetchall()                          

        ret_df = getBooksDF(books)
        
        # 데이터 출력하기
        # for book in books:                              
        #     print(book)
     
    except:
        is_success = False
        print("Database Error!")
        
    finally : 
        # 데이터베이스 커넥션 닫기
        conn.close()
        
    return is_success, ret_df


# if __name__ == "__main__":       # 외부에서 호출 시
#     select_all_books()           # 전체 조회용 함수 호출
#     print('=============================================')

```


```python
is_success, books_df = select_all_books(db_name)
if is_success:
    print('조회된 데이터는 총 %d 건 입니다.'%len(books_df))
else :
    print('데이터를 조회하지 못했습니다')

books_df
```

    [1] 전체 데이터 출력하기
    조회된 데이터는 총 5 건 입니다.
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>published_date</th>
      <th>publisher</th>
      <th>pages</th>
      <th>recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>메가트랜드</td>
      <td>2002.03.02</td>
      <td>A</td>
      <td>200</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>인더스트리 4.0</td>
      <td>2016.07.09</td>
      <td>B</td>
      <td>584</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>유니콘 스타트업</td>
      <td>2011.07.15</td>
      <td>A</td>
      <td>248</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>빅데이터 마케팅</td>
      <td>2012.08.25</td>
      <td>A</td>
      <td>296</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>사물인터넷 전망</td>
      <td>2013.08.22</td>
      <td>B</td>
      <td>526</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 일부 조회용 함수
def select_some_books(db_name, number):
    """
    일부 데이터를 조회하는 함수
    Args:
        db_name : Database Name
        number  : Count of data to query
    Returns : 
        is_success : Boolean 
        ret_df : DataFrame of books
    """
    ret_df = pd.DataFrame()
    is_success = True
    
    try:
        # 데이터베이스 커넥션 생성
        conn = sqlite3.connect(db_name) 

        # 커서 확보
        cur = conn.cursor()  

        # 조회용 SQL 실행
        db_sql = "SELECT * FROM my_books"
        cur.execute(db_sql) 

        # 조회한 데이터 일부 불러오기
        print('[2] 데이터 일부 출력하기')
        books = cur.fetchmany(number)                   

        ret_df = getBooksDF(books)
     
    except:
        is_success = False
        print("Database Error!")
        
    finally : 
        # 데이터베이스 커넥션 닫기
        conn.close()
        
    return is_success, ret_df                                

# if __name__ == "__main__":         # 외부에서 호출 시
#     select_some_books(3)           # 일부 조회용 함수 호출
#     print('=============================================')

```


```python
# select_some_books(db_name, number=3)

is_success, books_df = select_some_books(db_name, number=3)
if is_success:
    print('조회된 데이터는 총 %d 건 입니다.'%len(books_df))
else :
    print('데이터를 조회하지 못했습니다')

books_df

```

    [2] 데이터 일부 출력하기
    조회된 데이터는 총 3 건 입니다.
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>published_date</th>
      <th>publisher</th>
      <th>pages</th>
      <th>recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>메가트랜드</td>
      <td>2002.03.02</td>
      <td>A</td>
      <td>200</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>인더스트리 4.0</td>
      <td>2016.07.09</td>
      <td>B</td>
      <td>584</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>유니콘 스타트업</td>
      <td>2011.07.15</td>
      <td>A</td>
      <td>248</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 1개 조회용 함수
def select_one_book(db_name):
    """
    최상단 하나의 데이터를 조회하는 함수
    Args:
        db_name : Database Name
    Returns : 
        is_success : Boolean 
        ret_df : DataFrame of books
    """
    ret_df = pd.DataFrame()
    is_success = True
    
    try:
        # 데이터베이스 커넥션 생성
        conn = sqlite3.connect(db_name) 

        # 커서 확보
        cur = conn.cursor()  

        # 조회용 SQL 실행
        db_sql = "SELECT * FROM my_books "
        cur.execute(db_sql) 

        # 데이터 한개 출력하기
        print('[3] 1개 데이터 출력하기')
        # print(cur.fetchone())                          
        book = cur.fetchone()
        books = [book]
        ret_df = getBooksDF(books)
     
    except:
        is_success = False
        print("Database Error!")
        
    finally : 
        # 데이터베이스 커넥션 닫기
        conn.close()
        
    return is_success, ret_df                                      

# if __name__ == "__main__":        # 외부에서 호출 시
#     select_one_book()             # 1개 조회용 함수 호출
#     print('=============================================')


```


```python
# select_one_book(db_name) 

is_success, books_df = select_one_book(db_name) 
if is_success:
    print('하나의 데이터를 성공적으로 조회하였습니다.')
else :
    print('데이터를 조회하지 못했습니다')

books_df

```

    [3] 1개 데이터 출력하기
    하나의 데이터를 성공적으로 조회하였습니다.
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>published_date</th>
      <th>publisher</th>
      <th>pages</th>
      <th>recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>메가트랜드</td>
      <td>2002.03.02</td>
      <td>A</td>
      <td>200</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 쪽수 많은 책 조회용 함수
def find_big_books(db_name):
    """
    조건에 맞는 데이터를 조회하는 함수
    조건 : 페이지수가 300쪽보다 큰 데이터
    Args:
        db_name : Database Name
    Returns : 
        is_success : Boolean 
        ret_df : DataFrame of books
    """
    ret_df = pd.DataFrame()
    is_success = True
    
    try:
        # 데이터베이스 커넥션 생성
        conn = sqlite3.connect(db_name) 

        # 커서 확보
        cur = conn.cursor()  

        # 조회용 SQL 실행
        # db_sql = "SELECT title, pages FROM my_books "
        db_sql = "SELECT * FROM my_books "
        db_sql+= "WHERE pages > 300"
        cur.execute(db_sql) 

        # 조회한 데이터 불러오기
        print('[4] 페이지 많은 책 출력하기')
        books = cur.fetchall()
        
        ret_df = getBooksDF(books)

    except:
        is_success = False
        print("Database Error!")
        
    finally : 
        # 데이터베이스 커넥션 닫기
        conn.close()
        
    return is_success, ret_df                                   

# if __name__ == "__main__":          # 외부에서 호출 시
#     find_big_books()                # 쪽수 많은 책 조회용 함수 호출
#     print('=============================================')
```


```python
# find_big_books(db_name)

is_success, books_df = find_big_books(db_name)
if is_success:
    print('조건에 맞는 데이터는 총 %d 건 입니다.(조건:pages>300)'%len(books_df))
else :
    print('데이터를 조회하지 못했습니다')

books_df
```

    [4] 페이지 많은 책 출력하기
    조건에 맞는 데이터는 총 2 건 입니다.(조건:pages>300)
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>published_date</th>
      <th>publisher</th>
      <th>pages</th>
      <th>recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>인더스트리 4.0</td>
      <td>2016.07.09</td>
      <td>B</td>
      <td>584</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>사물인터넷 전망</td>
      <td>2013.08.22</td>
      <td>B</td>
      <td>526</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### 데이터 갱신


```python
import sqlite3 

def update_books(db_name):
    """
    데이터를 수정하는 함수
    Args:
        db_name : Database Name
    Returns : 
        is_success : Boolean 
    """
    is_success = True
    
    try:
        # 데이터베이스 커넥션 생성
        conn = sqlite3.connect(db_name) 

        # 커서 확보
        cur = conn.cursor()  

        # 데이터 수정 SQL ( 제목이 ? 인 책의 추천 유무를 ? 로 변경하라 )
        db_sql = "UPDATE my_books SET recommendation=? WHERE title=? "

        # 수정 SQL 실행
        cur.execute(db_sql, (1, '메가트랜드'))

    except:
        is_success = False
        print("Database Error!")
        
    finally :      
        if is_success:
            # 데이터베이스 반영
            conn.commit()  
        else:
            # 데이터베이스 철회
            conn.rollback()
            
        # 데이터베이스 커넥션 닫기
        conn.close()
    
    return is_success   

# if __name__ == "__main__":        # 외부에서 호출 시
#     select_one_book()
#     update_books()                # 데이터 수정 함수 호출
#     print('[데이터 수정 완료] ================== ')
#     select_one_book()

```


```python
# select_one_book(db_name)
# update_books(db_name)
# print('[데이터 수정 완료] ================== ')
# select_one_book(db_name)

is_success, books_df1 = select_one_book(db_name) 

if update_books(db_name):
    print('데이터가 성공적으로 수정되었습니다.')
else :
    print('데이터가 수정되지 않았습니다')
    
is_success, books_df2 = select_one_book(db_name) 

books_df = pd.concat([books_df1, books_df2], axis=0)
books_df['update'] = ['수정전', '수정후']
books_df.set_index('update', inplace=True)
books_df

```

    [3] 1개 데이터 출력하기
    데이터가 성공적으로 수정되었습니다.
    [3] 1개 데이터 출력하기
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>published_date</th>
      <th>publisher</th>
      <th>pages</th>
      <th>recommendation</th>
    </tr>
    <tr>
      <th>update</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>수정전</th>
      <td>메가트랜드</td>
      <td>2002.03.02</td>
      <td>A</td>
      <td>200</td>
      <td>0</td>
    </tr>
    <tr>
      <th>수정후</th>
      <td>메가트랜드</td>
      <td>2002.03.02</td>
      <td>A</td>
      <td>200</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

### 데이터 삭제


```python
import sqlite3 

# 데이터 삭제용 함수
def delete_books_by_title(db_name, title):
    """
    책제목에 해당하는 데이터를 삭제하는 함수
    Args:
        db_name : Database Name
        title   : Title of the book to be removed
    Returns : 
        is_success : Boolean 
    """
    is_success = True
    
    try:    
        # 데이터베이스 커넥션 생성
        conn = sqlite3.connect(db_name) 

        # 커서 확보
        cur = conn.cursor()  

        # 데이터 삭제 SQL
        db_sql = "DELETE FROM my_books "
        db_sql+= "WHERE title = ?      "

        # 수정 SQL 실행
        # print('db_sql:', db_sql)
        # print('title:', title)
        cur.execute(db_sql, (title,))
        # count = cur.execute(db_sql, (title,))
        # print('count:', type(count), count)
        
    except:
        is_success = False
        print("Database Error!")
        
    finally :      
        if is_success:
            # 데이터베이스 반영
            conn.commit()  
        else:
            # 데이터베이스 철회
            conn.rollback()
            
        # 데이터베이스 커넥션 닫기
        conn.close()
    
    return is_success   

```


```python
title = '메가트랜드'
if delete_books_by_title(db_name, title):
    print('데이터가 성공적으로 삭제되었습니다.')
else :
    print('데이터가 삭제되지 않았습니다')

is_success, books_df = select_all_books(db_name) 
books_df
```

    데이터가 성공적으로 삭제되었습니다.
    [1] 전체 데이터 출력하기
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>published_date</th>
      <th>publisher</th>
      <th>pages</th>
      <th>recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>인더스트리 4.0</td>
      <td>2016.07.09</td>
      <td>B</td>
      <td>584</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>유니콘 스타트업</td>
      <td>2011.07.15</td>
      <td>A</td>
      <td>248</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>빅데이터 마케팅</td>
      <td>2012.08.25</td>
      <td>A</td>
      <td>296</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>사물인터넷 전망</td>
      <td>2013.08.22</td>
      <td>B</td>
      <td>526</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
def delete_books(db_name, col_name, col_val):
    """
    조건에 맞는 데이터를 삭제하는 함수
    Args:
        db_name  : Database Name
        col_name : Column Name
        col_val  : Column Value
    Returns : 
        is_success : Boolean 
    """
    is_success = True
    
    try: 
        # 데이터베이스 커넥션 생성
        conn = sqlite3.connect(db_name) 

        # 커서 확보
        cur = conn.cursor()  


        # 데이터 삭제 SQL
        # db_sql = "DELETE FROM my_books "
        # db_sql+= "WHERE {} = '{}' "
        # db_sql = db_sql.format(col_name, col_val)
        # cur.execute(db_sql)    

        # # 데이터 삭제 SQL
        db_sql = 'DELETE FROM my_books '
        db_sql+= 'WHERE {} = ? '
        db_sql = db_sql.format(col_name)

        # 수정 SQL 실행
        cur.execute(db_sql, (col_val,))

    except:
        is_success = False
        print("Database Error!")
        
    finally :      
        if is_success:
            # 데이터베이스 반영
            conn.commit()  
        else:
            # 데이터베이스 철회
            conn.rollback()
            
        # 데이터베이스 커넥션 닫기
        conn.close()
    
    return is_success   
    
    
# if __name__ == "__main__":     # 외부에서 호출 시
#     select_all_books()         # 테이블 전체 데이터 확인
#     delete_books()             # 데이터 삭제 함수 호출
#     print('[데이터 삭제 완료] ================== ')
#     select_all_books()         # 테이블 전체 데이터 확인

```


```python
is_success, books_df = select_all_books(db_name) 
books_df
```

    [1] 전체 데이터 출력하기
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>published_date</th>
      <th>publisher</th>
      <th>pages</th>
      <th>recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>인더스트리 4.0</td>
      <td>2016.07.09</td>
      <td>B</td>
      <td>584</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>유니콘 스타트업</td>
      <td>2011.07.15</td>
      <td>A</td>
      <td>248</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>빅데이터 마케팅</td>
      <td>2012.08.25</td>
      <td>A</td>
      <td>296</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>사물인터넷 전망</td>
      <td>2013.08.22</td>
      <td>B</td>
      <td>526</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
col_name = 'publisher'
col_val  = 'A'
if delete_books(db_name, col_name, col_val):
    print('데이터가 성공적으로 삭제되었습니다.')
else :
    print('데이터가 삭제되지 않았습니다')

is_success, books_df = select_all_books(db_name) 
books_df
```

    데이터가 성공적으로 삭제되었습니다.
    [1] 전체 데이터 출력하기
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>published_date</th>
      <th>publisher</th>
      <th>pages</th>
      <th>recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>인더스트리 4.0</td>
      <td>2016.07.09</td>
      <td>B</td>
      <td>584</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>사물인터넷 전망</td>
      <td>2013.08.22</td>
      <td>B</td>
      <td>526</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
col_name = 'title'
col_val  = '사물인터넷 전망'
if delete_books(db_name, col_name, col_val):
    print('데이터가 성공적으로 삭제되었습니다.')
else :
    print('데이터가 삭제되지 않았습니다')

is_success, books_df = select_all_books(db_name) 
books_df
```

    데이터가 성공적으로 삭제되었습니다.
    [1] 전체 데이터 출력하기
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>published_date</th>
      <th>publisher</th>
      <th>pages</th>
      <th>recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>인더스트리 4.0</td>
      <td>2016.07.09</td>
      <td>B</td>
      <td>584</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
reset
```

    Once deleted, variables cannot be recovered. Proceed (y/[n])? 
    Nothing done.
    


```python

```


```python

```


```python

```

## Python SQL
> [Python SQL 드라이버](https://docs.microsoft.com/ko-kr/sql/connect/python/python-driver-for-sql-server?view=sql-server-2017)
- Python SQL 드라이버-pyodbc  : [Python SQL 드라이버 pyodbc](https://docs.microsoft.com/ko-kr/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-2017)
- Python SQL 드라이버-pymssql : [Python SQL 드라이버 - pymssql](https://docs.microsoft.com/ko-kr/sql/connect/python/pymssql/python-sql-driver-pymssql?view=sql-server-2017)


```python
! conda install MySQLdb
```

    Solving environment: failed
    
    PackagesNotFoundError: The following packages are not available from current channels:
    
      - mysqldb
    
    Current channels:
    
      - https://repo.anaconda.com/pkgs/main/osx-64
      - https://repo.anaconda.com/pkgs/main/noarch
      - https://repo.anaconda.com/pkgs/free/osx-64
      - https://repo.anaconda.com/pkgs/free/noarch
      - https://repo.anaconda.com/pkgs/r/osx-64
      - https://repo.anaconda.com/pkgs/r/noarch
      - https://repo.anaconda.com/pkgs/pro/osx-64
      - https://repo.anaconda.com/pkgs/pro/noarch
    
    To search for alternate channels that may provide the conda package you're
    looking for, navigate to
    
        https://anaconda.org
    
    and use the search bar at the top of the page.
    
    
    


```python
! pip list
```

    Package                            Version  
    ---------------------------------- ---------
    absl-py                            0.4.0    
    alabaster                          0.7.10   
    anaconda-client                    1.6.14   
    anaconda-navigator                 1.8.7    
    anaconda-project                   0.8.2    
    appnope                            0.1.0    
    appscript                          1.0.1    
    asn1crypto                         0.24.0   
    astor                              0.7.1    
    astroid                            1.6.3    
    astropy                            3.0.2    
    attrs                              18.1.0   
    Babel                              2.5.3    
    backcall                           0.1.0    
    backports.shutil-get-terminal-size 1.0.0    
    beautifulsoup4                     4.6.0    
    bitarray                           0.8.1    
    bkcharts                           0.2      
    blaze                              0.11.3   
    bleach                             2.1.3    
    bokeh                              0.12.16  
    boto                               2.48.0   
    Bottleneck                         1.2.1    
    branca                             0.3.0    
    certifi                            2018.4.16
    cffi                               1.11.5   
    chardet                            3.0.4    
    click                              6.7      
    cloudpickle                        0.5.3    
    clyent                             1.2.2    
    colorama                           0.3.9    
    conda                              4.5.10   
    conda-build                        3.10.5   
    conda-verify                       2.0.0    
    contextlib2                        0.5.5    
    cryptography                       2.2.2    
    cycler                             0.10.0   
    Cython                             0.28.2   
    cytoolz                            0.9.0.1  
    dask                               0.17.5   
    datashape                          0.5.4    
    decorator                          4.3.0    
    distributed                        1.21.8   
    docutils                           0.14     
    entrypoints                        0.2.3    
    et-xmlfile                         1.0.1    
    fastcache                          1.0.2    
    filelock                           3.0.4    
    Flask                              1.0.2    
    Flask-Cors                         3.0.4    
    folium                             0.6.0    
    gast                               0.2.0    
    gevent                             1.3.0    
    glob2                              0.6      
    gmpy2                              2.0.8    
    greenlet                           0.4.13   
    grpcio                             1.14.1   
    h5py                               2.7.1    
    heapdict                           1.0.0    
    html5lib                           1.0.1    
    idna                               2.6      
    imageio                            2.3.0    
    imagesize                          1.0.0    
    ipykernel                          4.8.2    
    ipython                            6.4.0    
    ipython-genutils                   0.2.0    
    ipywidgets                         7.2.1    
    isort                              4.3.4    
    itsdangerous                       0.24     
    jdcal                              1.4      
    jedi                               0.12.0   
    Jinja2                             2.10     
    jsonschema                         2.6.0    
    jupyter                            1.0.0    
    jupyter-client                     5.2.3    
    jupyter-console                    5.2.0    
    jupyter-core                       4.4.0    
    jupyterlab                         0.32.1   
    jupyterlab-launcher                0.10.5   
    kiwisolver                         1.0.1    
    lazy-object-proxy                  1.3.1    
    llvmlite                           0.23.1   
    locket                             0.2.0    
    lxml                               4.2.1    
    Markdown                           2.6.11   
    MarkupSafe                         1.0      
    matplotlib                         2.2.2    
    mccabe                             0.6.1    
    mistune                            0.8.3    
    mkl-fft                            1.0.0    
    mkl-random                         1.0.1    
    more-itertools                     4.1.0    
    mpmath                             1.0.0    
    msgpack-python                     0.5.6    
    multipledispatch                   0.5.0    
    navigator-updater                  0.2.1    
    nbconvert                          5.3.1    
    nbformat                           4.4.0    
    networkx                           2.1      
    nltk                               3.3      
    nose                               1.3.7    
    notebook                           5.5.0    
    numba                              0.38.0   
    numexpr                            2.6.5    
    numpy                              1.14.3   
    numpydoc                           0.8.0    
    odo                                0.5.1    
    olefile                            0.45.1   
    openpyxl                           2.5.3    
    packaging                          17.1     
    pandas                             0.23.0   
    pandocfilters                      1.4.2    
    parso                              0.2.0    
    partd                              0.3.8    
    path.py                            11.0.1   
    pathlib2                           2.3.2    
    patsy                              0.5.0    
    pep8                               1.7.1    
    pexpect                            4.5.0    
    pickleshare                        0.7.4    
    Pillow                             5.1.0    
    pip                                18.0     
    pkginfo                            1.4.2    
    pluggy                             0.6.0    
    ply                                3.11     
    prompt-toolkit                     1.0.15   
    protobuf                           3.6.1    
    psutil                             5.4.5    
    ptyprocess                         0.5.2    
    py                                 1.5.3    
    pycodestyle                        2.4.0    
    pycosat                            0.6.3    
    pycparser                          2.18     
    pycrypto                           2.6.1    
    pycurl                             7.43.0.1 
    pyflakes                           1.6.0    
    Pygments                           2.2.0    
    pylint                             1.8.4    
    pyodbc                             4.0.23   
    pyOpenSSL                          18.0.0   
    pyparsing                          2.2.0    
    PySocks                            1.6.8    
    pytest                             3.5.1    
    pytest-arraydiff                   0.2      
    pytest-astropy                     0.3.0    
    pytest-doctestplus                 0.1.3    
    pytest-openfiles                   0.3.0    
    pytest-remotedata                  0.2.1    
    python-dateutil                    2.7.3    
    pytz                               2018.4   
    PyWavelets                         0.5.2    
    PyYAML                             3.12     
    pyzmq                              17.0.0   
    QtAwesome                          0.4.4    
    qtconsole                          4.3.1    
    QtPy                               1.4.1    
    requests                           2.18.4   
    rope                               0.10.7   
    ruamel-yaml                        0.15.35  
    scikit-image                       0.13.1   
    scikit-learn                       0.19.1   
    scipy                              1.1.0    
    seaborn                            0.8.1    
    Send2Trash                         1.5.0    
    setuptools                         39.1.0   
    simplegeneric                      0.8.1    
    singledispatch                     3.4.0.3  
    six                                1.11.0   
    snowballstemmer                    1.2.1    
    sortedcollections                  0.6.1    
    sortedcontainers                   1.5.10   
    Sphinx                             1.7.4    
    sphinxcontrib-websupport           1.0.1    
    spyder                             3.2.8    
    SQLAlchemy                         1.2.7    
    statsmodels                        0.9.0    
    sympy                              1.1.1    
    tables                             3.4.3    
    tblib                              1.3.2    
    tensorboard                        1.10.0   
    tensorflow                         1.9.0    
    termcolor                          1.1.0    
    terminado                          0.8.1    
    testpath                           0.3.1    
    toolz                              0.9.0    
    tornado                            5.0.2    
    tqdm                               4.25.0   
    traitlets                          4.3.2    
    typing                             3.6.4    
    unicodecsv                         0.14.1   
    urllib3                            1.22     
    wcwidth                            0.1.7    
    webencodings                       0.5.1    
    Werkzeug                           0.14.1   
    wheel                              0.31.1   
    widgetsnbextension                 3.2.1    
    wrapt                              1.10.11  
    xlrd                               1.1.0    
    XlsxWriter                         1.0.4    
    xlwings                            0.11.8   
    xlwt                               1.2.0    
    zict                               0.1.3    
    
import pandas as pd
import MySQLdb

db_info = MySQLdb.connect(
    "db.fastcamp.us",  # DATABASE_HOST
    "root",            # DATABASE_USERNAME
    "dkstncks",        # DATABASE_PASSWORD
    "sakila",          # DATABASE_NAME
    charset='utf8',
)

sql_query = "SELECT * FROM table_name ;"

pd.read_sql(sql_query, db_info)


```python
sql_query = "SELECT * FROM customer;"
pd.read_sql(sql_query, db_info)
```


```python
# sql_query = "SELECT * FROM customer;"
# pd.read_sql(sql_query, db_info)

# 데이터베이스 vs Pandas
# 병목 :: 연산 << 네트워크
```


```python
# 모든 테이블 => DataFrame

# 어떻게 하면, 모든 테이블들을 일괄적으로, + 쉽게 한번에 DataFrame 으로 만들 수 있을까?
# 함수
# input: "데이터베이스 명", output: "새로운 폴더"(데이터베이스명), 테이블.csv
#                       sakila/customer.csv, payment.csv, .....
```


```python
sql_query = "SHOW Tables;"
pd.read_sql(sql_query, db_info)
```


```python

```


```python
table_df = pd.read_sql(sql_query, db_info)
table_df
```


```python
table_df.shape
```


```python
sql_query = "SELECT * FROM customer;"
pd.read_sql(sql_query, db_info)
```


```python

```


```python
import os 
import shutil
```


```python
# 데이터베이스 연결은 되어있는 상태

def table_to_csv(database, table):
    """
    데이터베이스 테이블의 모든 데이터 조회결과를 csv파일로 생성
    """
    sql_query = "SELECT * FROM {table};"
    sql_query = sql_query.format(table=table)
    
    df = pd.read_sql(sql_query, db_info)
    df.to_csv(
        os.path.join(database, table + ".csv")
    )

    
def database_to_csv(database):
    
    # 데이터베이스명이 없는 경우, 데이터베이스명 폴더 생성하기
    if database in os.listdir():
        shutil.rmtree(database)
    else:
        pass
    
    os.makedirs(database)
    
    sql_query = "SHOW Tables;"
    tables_df = pd.read_sql(sql_query, db_info)  
    # Tables_in_sakila
    tables_df.iloc[:, 0]
    
    return tables_df

    
database_to_csv("sakila")
```


```python
# 데이터베이스 연결은 되어있는 상태

def table_to_csv(database, table):
    """
    데이터베이스 테이블의 모든 데이터 조회결과를 csv파일로 생성
    """
    sql_query = "SELECT * FROM {table};"
    sql_query = sql_query.format(table=table)
    
    df = pd.read_sql(sql_query, db_info)
    df.to_csv(
        os.path.join(database, table + ".csv")
    )
    
    
def database_to_csv(database):
    
    # 데이터베이스명이 없는 경우, 데이터베이스명 폴더 생성하기
    if database in os.listdir():
        shutil.rmtree(database)
    else:
        pass
    
    os.makedirs(database)
    
    sql_query = "SHOW Tables;"
    tables_df = pd.read_sql(sql_query, db_info)  
    # Tables_in_sakila
    tables_df.iloc[:, 0].apply(lambda table: table_to_csv(database, table))
    # pandas 데이터 분석 ( 기능적으로 사용할 수 있는 부분도 많다! )
    
    return tables_df

    
database_to_csv("sakila")
```


```python
tables_df.iloc[:, 0].apply(
    lambda table_name: "SELECT * FROM {table_name};".format(
        table_name=table_name,
    )
)
```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
