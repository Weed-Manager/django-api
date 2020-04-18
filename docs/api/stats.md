# Stats
Statistic route, query to get info on your consumption

## Getting total operation done (useful for vaporizer users)

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
