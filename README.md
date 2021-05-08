# Instructions
#### Prerequisite
- python 3.7
- pip 21.x.x
#### Installation
```
cd tcb_homework
pip install -r requirements.txt   //install project's dependencies
python server.py   //run server
```
Output something like:  **Running on http://127.0.0.1:7777/ (Press CTRL+C to quit)**

#### Testing
- Using terminal command line
```
 curl -X POST http://127.0.0.1:7777/append  -H 'Content-Type: application/json' -H 'Accept: application/json' -d '{"poolId": 123456, "poolValues": [11,21,31,45]}'
 [Output]: {"data":"inserted","success":true} or {"data":"appended","success":true}
 
 curl -s -X POST http://127.0.0.1:7777/query  -H 'Content-Type: application/json' -H 'Accept: application/json' -d '{"poolId": 123456, "percentile": 50}'
 [Output]: {"data":{"poolCount":4,"quantile":31},"success":true}
```


- Using python command follow syntax:  python client.py <endpoint> <post_data> 
```
python client.py append '{"poolId": 123456, "poolValues": [11,21,31,45]}'
```
