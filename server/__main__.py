from server import init_api


def main():
    app = init_api()
    app.run(host='localhost', port='8080')


if __name__ == "__main__":
    main()
