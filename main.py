from website import create_app

app = create_app()

# True allows changes while loading
# Remove before deployment

if __name__ == '__main__':
    app.run(debug=True)