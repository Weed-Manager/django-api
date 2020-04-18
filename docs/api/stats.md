# Stats
Statistic route, query to get info on your consumption

## Getting total quantity consumed

**Request**

GET /api/stats/total/

No parameters

**Response**

```json
Content-Type application/json
200 OK 
{
  "total": "420"
}
```

## Getting total capsule operation done (gets the number of oepration where -0.16 < quantity < -0.14)

**Request**

GET /api/stats/total_caps/

No parameters

**Response**

```json
Content-Type application/json
200 OK 
{
  "total_caps": "420"
}
```
## Getting total operation done on a strain (useful for vaporizer users)

**Request**

GET /api/stats/total\_by\_strain/

No parameters

**Response**

```json
Content-Type application/json
200 OK 
{
	"strain_name": "Gorrila Glue N4",
	"total": 1
},
{
	"strain_name": "Lemon Haze",
	"total": 1
}
```
## Getting total capsule operation done on a strain (gets the number of oepration where -0.16 < quantity < -0.14)

**Request**

GET /api/stats/total\_caps\_by\_strain/

No parameters

**Response**

```json
Content-Type application/json
200 OK 
{
	"strain_name": "Gorrila Glue N4",
	"total_caps": 1
},
{
	"strain_name": "Lemon Haze",
	"total_caps": 1
}
```
