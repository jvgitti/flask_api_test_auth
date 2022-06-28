from server import init_api


def main():
    app = init_api()
    app.run(host='0.0.0.0')


if __name__ == "__main__":
    main()

