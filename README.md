# Instructions
### Prerequisite
- python 3.7
- pip 21.x.x
### Installation
```
git clone -b master https://github.com/ngunq/tcb_homework.git
cd tcb_homework
```
- Install dependencies
```
pip install -r requirements.txt
```
- Run server
```
python server.py
```
Output something like:  **Running on http://127.0.0.1:7777/ (Press CTRL+C to quit)**

### Testing
- Using terminal command
 ```
 curl -X POST http://127.0.0.1:7777/append  -H 'Content-Type: application/json' -H 'Accept: application/json' -d '{"poolId": 123456, "poolValues": [11,21,31,45]}'
 ```
 **Output:** 
 ```json
 {
  "data": "inserted",
  "success": true
}
 ```
 or
  ```json
 {
  "data": "appended",
  "success": true
}
 ```
 
 ```
 curl -s -X POST http://127.0.0.1:7777/query  -H 'Content-Type: application/json' -H 'Accept: application/json' -d '{"poolId": 123456, "percentile": 50}'
 ```
  **Output:**
  ```json
  {
  "data": {
    "poolCount": 4,
    "quantile": 31
  },
  "success": true
}
  ```

- Using python command follow syntax:  `python client.py [endpoint] [post_data]`

  **Example:**
```
python client.py append '{"poolId": 123456, "poolValues": [11,21,31,45]}'
python client.py query '{"poolId": 123456, "percentile": 50}'
```



