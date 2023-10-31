from website import create_app

#Checking For Commit
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)