import psycopg2

def return_dbconnection():
    #return psycopg2.connect("host=localhost port=5432 dbname=ERP user=postgres password=Rematch2025! connect_timeout=10 sslmode=prefer")
    return psycopg2.connect("host=192.168.1.49 port=5432 dbname=ERP user=postgres password=admin connect_timeout=10 sslmode=prefer")
    #return psycopg2.connect("host=localhost port=5432 dbname=ERP user=postgres password=Sasukixx1! connect_timeout=10 sslmode=prefer")

#if __name__ == "__main__":
