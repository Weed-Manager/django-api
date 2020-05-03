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

## Getting total capsule operation in a date range

**Request**

GET /api/stats/consumption/

Query parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
start_date | date   | Yes      | the start date 
end_date   | date   | Yes      | the end date

**Response**
```json
Content-Type application/json
200 OK 
{
	"quantity": 2,
	"items": [
		{
		  "id": "1",
		  "strain": "1",
		  "quantity": "-0.15"
		  "created_at": "2020-04-18T17:46:54+0000"
		},
		{
		  "id": "2",
		  "strain": "1",
		  "quantity": "-0.15"
		  "created_at": "2020-04-18T20:46:54+0000"
		}
	]
}
```

## Getting total capsule operation in a date range grouped_by day/week/month
**Request**

GET /api/stats/consumption_by_split/

Query parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
start_date | date   | Yes      | the start date 
end_date   | date   | Yes      | the end date
split      | string | Yes      | the desired split day/week/month 

**Response**
```json
Content-Type application/json
200 OK 
{
	"items": [
		{
		  "day": "2020-04-18T00:00:00Z"
		  "quantity": "-0.15"
		},
		{
		  "day": "2020-04-19T00:00:00Z"
		  "quantity": "-0.90"
		}
	]
}
```
