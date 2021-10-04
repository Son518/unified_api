from unified import unified

if __name__ == "__main__":
    unified.run()

# to start server with gunicorn

# gunicorn --bind 0.0.0.0:5000 wsgi:unified