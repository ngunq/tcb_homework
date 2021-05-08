# API Reference

# Insert/Append pool values

Insert new values into a pool, if poolId exists, append values

**URL** : `/append`

**Method** : `POST`

### Request constraints 
```json
{
    "poolId": <numberic>,
    "poolValues": <list<numberic>>
}
```
**Request examples**
```json
{
    "poolId": 123456,
    "poolValues": [11, 21, 31, 41]
}
```
### Success responses
```json
{
    "success": <bool>,
    "data": <string> (inserted/appended)
}
```
**Response examples**
```json
{
    "success": true,
    "data": "inserted"
}
```

## Query a pool

Query a pool values by poolId then return pool's value count and a quantile (in percentile form)

**URL** : `/query`

**Method** : `POST`

### Request constraints 
```json
{
    "poolId": <numberic>,
    "percentile": <numberic>
}
```
**Request examples**
```json
{
    "poolId": 123456,
    "percentile": 50
}
```
### Success responses
```json
{
    "success": <bool>,
    "data": <object>
}
```
**Response examples**
```json
{
    "success": true,
    "data": {
      "poolCount": 4,
      "quantile": 31
    }
}
```
