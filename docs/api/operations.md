# Strain operations
Supports getting a list, getting a detailed object and creating strainoperations

## Creating a new strain operation

**Request**:

POST /operations/

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
strain	   | id     | Yes      | The targeted strain id
quantity   | float  | Yes      | The operation quantity.

*Note:*

- Authorization protected
- Send a positive quantity to add and a negative to substract

**Response**:

```json
Content-Type application/json
201 Created

{
  "id": "1",
  "strain": "1",
  "quantity": "-0.15"
}
```

## Getting a single strainoperation

**Request**:

DELETE /operations/{operation_id}

Parameters:

None


*Note:*

- Authorization protected


**Response**:

```json
Content-Type application/json
204 NO CONTENT

{
    "id": 1,
    "strain": "1",
    "quantity": -0.15
}
```

