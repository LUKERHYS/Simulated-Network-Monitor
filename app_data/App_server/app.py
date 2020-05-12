from utils.app_factory import create_app

if __name__ == '__main__' : 
    app = create_app()
    print(app.url_map)
    app.run(port=5001, debug = True, host='0.0.0.0')
