# from flask import Flask
# import asyncio
#
# app = Flask(__name__)
#
# async def update_value():
#     await asyncio.sleep(5)  # wait for 5 seconds
#     return "updated value"
#
# @app.get('/get_value')
# async def get_value():
#     # return the initial value immediately
#     value = "initial value"
#     # update the value asynchronously after a delay of 5 seconds
#     task = asyncio.ensure_future(update_value())
#     updated_value = await task
#     value = updated_value
#     return value
#
# if __name__ == '__main__':
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.create_task(asyncio.start_server(app, 'localhost', 5000))
#     try:
#         loop.run_forever()
#     finally:
#         loop.close()
#
#
# import asyncio
# from flask import Flask
#
# app1 = Flask(__name__)
#
#
# async def async_get_data():
#     await asyncio.sleep(5)
#     return 'Done!'
#
#
# @app1.route("/data")
# async def get_data():
#     data = await async_get_data()
#     return data
#
# if __name__ == '__main__':
#     app1.run(debug=True)

import time
from threading import Thread
from flask import Flask, request, jsonify

app = Flask(__name__)


def wait_status():
    print("Sleep started")
    count = 0
    while count <= 10:
        print(count)
        count += 1
        time.sleep(1)


update_status_thread = None


@app.route('/', methods=["POST", "GET"])
def method_msg():
    if request.method == "POST":
        global update_status_thread
        update_status_thread = Thread(target=wait_status)
        print("--",update_status_thread)
        # update_status_thread.start()
        print("**",update_status_thread.start())
        return jsonify(msg="POST Method Called")
    elif request.method == "GET":
        print(update_status_thread.is_alive())
        print("--", update_status_thread)
        if update_status_thread and not update_status_thread.is_alive():
            return jsonify(msg="Updated Get Method")
        print(update_status_thread.is_alive())
        print("--", update_status_thread)
        return jsonify(msg="Get Method Called")


if __name__ == "__main__":
    app.run(debug=True)
